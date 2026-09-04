#!/usr/bin/env python3
"""Validate canonical revision metadata and its relative links."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import build_revision_indexes as indexes


ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "revision" / "problem_metadata.json"

REQUIRED_FIELDS = {
    "leetcode_id",
    "sync_id",
    "title",
    "slug",
    "difficulty",
    "topics",
    "current_approach",
    "target_pattern",
    "pattern_variant",
    "secondary_patterns",
    "solution_quality",
    "confidence",
    "last_revised",
    "redo",
}
ALLOWED_CONFIDENCE = {"red", "yellow", "green"}
ALLOWED_QUALITY = {
    "interview_ready",
    "valid_but_suboptimal",
    "shortcut_or_builtin",
    "needs_review",
    "alternate_approach",
}
ALLOWED_DIFFICULTY = {"Easy", "Medium", "Hard"}


def load_safe_metadata(errors: list[str]) -> dict[str, dict[str, object]]:
    def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                errors.append(f"revision/problem_metadata.json: duplicate JSON key {key!r}")
            result[key] = value
        return result

    try:
        value = json.loads(
            METADATA_PATH.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys
        )
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"revision/problem_metadata.json: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append("revision/problem_metadata.json: top-level value must be an object")
        return {}
    result: dict[str, dict[str, object]] = {}
    safe_fields = {"folder", "sync_id", "leetcode_id", "slug", "title", "difficulty"}
    for key, record in value.items():
        if not isinstance(key, str) or not isinstance(record, dict):
            errors.append("revision/problem_metadata.json: every entry must be an object keyed by slug")
            continue
        unknown = set(record) - safe_fields
        missing = safe_fields - set(record)
        if unknown:
            errors.append(f"metadata[{key!r}]: unsafe/unknown fields: {sorted(unknown)}")
        if missing:
            errors.append(f"metadata[{key!r}]: missing fields: {sorted(missing)}")
        if record.get("slug") != key:
            errors.append(f"metadata[{key!r}]: key must equal the canonical slug field")
        result[key] = record
    return result


def validate_revision(
    folder: Path,
    safe_metadata: dict[str, dict[str, object]],
    seen_slugs: dict[str, str],
    errors: list[str],
    warnings: list[str],
) -> None:
    revision = folder / "REVISION.md"
    label = str(revision.relative_to(ROOT))
    if not revision.is_file():
        errors.append(f"{label}: missing")
        return
    try:
        data = indexes.parse_frontmatter(revision)
    except (OSError, indexes.FrontmatterError) as exc:
        errors.append(f"{label}: {exc}")
        return

    missing = REQUIRED_FIELDS - set(data)
    if missing:
        errors.append(f"{label}: missing fields {sorted(missing)}")

    leetcode_id = data.get("leetcode_id")
    if isinstance(leetcode_id, bool) or not isinstance(leetcode_id, int) or leetcode_id <= 0:
        errors.append(f"{label}: leetcode_id must be a positive integer")

    sync_id = data.get("sync_id")
    if not isinstance(sync_id, str) or len(sync_id) != 4 or not sync_id.isdigit():
        errors.append(f"{label}: sync_id must be a four-character digit string")
    elif not folder.name.startswith(f"{sync_id}-"):
        errors.append(f"{label}: sync_id does not match the physical folder prefix")

    for field in ("title", "slug", "difficulty", "current_approach", "target_pattern", "pattern_variant"):
        if not isinstance(data.get(field), str) or not str(data.get(field)).strip():
            errors.append(f"{label}: {field} must be a non-empty string")

    slug = data.get("slug")
    if isinstance(slug, str):
        if slug in seen_slugs:
            errors.append(f"{label}: duplicate slug also used by {seen_slugs[slug]}")
        else:
            seen_slugs[slug] = label
        folder_slug = indexes.normalize_slug(indexes.FOLDER_RE.fullmatch(folder.name).group(2))  # type: ignore[union-attr]
        if indexes.normalize_slug(slug) != folder_slug:
            errors.append(f"{label}: slug does not match the normalized physical folder slug")

        source = safe_metadata.get(slug)
        if source is None:
            errors.append(f"{label}: slug is absent from revision/problem_metadata.json")
        else:
            expected = {
                "folder": folder.name,
                "sync_id": data.get("sync_id"),
                "leetcode_id": data.get("leetcode_id"),
                "slug": slug,
                "title": data.get("title"),
                "difficulty": data.get("difficulty"),
            }
            if source != expected:
                errors.append(f"{label}: identity fields disagree with revision/problem_metadata.json")

    if data.get("difficulty") not in ALLOWED_DIFFICULTY:
        errors.append(f"{label}: unknown difficulty {data.get('difficulty')!r}")
    if data.get("confidence") not in ALLOWED_CONFIDENCE:
        errors.append(f"{label}: unknown confidence {data.get('confidence')!r}")
    if data.get("solution_quality") not in ALLOWED_QUALITY:
        errors.append(f"{label}: unknown solution_quality {data.get('solution_quality')!r}")
    if data.get("target_pattern") not in indexes.PATTERNS:
        errors.append(f"{label}: unknown target_pattern {data.get('target_pattern')!r}")

    topics = data.get("topics")
    if not isinstance(topics, list) or not topics:
        errors.append(f"{label}: topics must be a non-empty list")
    elif any(not isinstance(topic, str) or topic not in indexes.TOPICS for topic in topics):
        errors.append(f"{label}: topics contains an unknown value")
    elif len(topics) != len(set(topics)):
        errors.append(f"{label}: topics contains duplicates")

    secondary = data.get("secondary_patterns")
    if not isinstance(secondary, list) or any(not isinstance(item, str) for item in secondary):
        errors.append(f"{label}: secondary_patterns must be a list of strings")
    elif len(secondary) != len(set(secondary)):
        errors.append(f"{label}: secondary_patterns contains duplicates")

    if not isinstance(data.get("redo"), bool):
        errors.append(f"{label}: redo must be true or false")
    if data.get("last_revised") is not None and not isinstance(data.get("last_revised"), str):
        errors.append(f"{label}: last_revised must be null or a string date")

    quality = data.get("solution_quality")
    if quality in {"valid_but_suboptimal", "shortcut_or_builtin", "needs_review"} and data.get("redo") is not True:
        errors.append(f"{label}: quality {quality!r} requires redo: true")
    if data.get("confidence") == "yellow":
        warnings.append(f"{label}: confidence has not been manually revised")

    if not (folder / "README.md").is_file():
        errors.append(f"{folder.name}: missing sync-managed README.md")
    if not any((folder / name).is_file() for name in ("solution.py", "solution.sql")):
        errors.append(f"{folder.name}: missing canonical solution.py or solution.sql")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    safe_metadata = load_safe_metadata(errors)
    folders = indexes.discover_canonical_folders()
    seen_slugs: dict[str, str] = {}

    folder_slug_owners: dict[str, str] = {}
    for folder in folders:
        folder_slug = indexes.normalize_slug(indexes.FOLDER_RE.fullmatch(folder.name).group(2))  # type: ignore[union-attr]
        previous = folder_slug_owners.get(folder_slug)
        if previous:
            errors.append(f"duplicate normalized physical slug: {previous} and {folder.name}")
        else:
            folder_slug_owners[folder_slug] = folder.name
        validate_revision(folder, safe_metadata, seen_slugs, errors, warnings)

    metadata_folders = [record.get("folder") for record in safe_metadata.values()]
    if len(metadata_folders) != len(set(metadata_folders)):
        errors.append("revision/problem_metadata.json: duplicate physical folder mapping")
    physical_names = {folder.name for folder in folders}
    if set(metadata_folders) != physical_names:
        missing = sorted(physical_names - set(metadata_folders))
        extra = sorted(set(metadata_folders) - physical_names)
        if missing:
            errors.append(f"revision/problem_metadata.json: missing physical folders {missing}")
        if extra:
            errors.append(f"revision/problem_metadata.json: non-physical folders {extra}")

    link_paths = [folder / "REVISION.md" for folder in folders]
    link_paths.extend((ROOT / "revision").rglob("*.md"))
    link_paths.extend((ROOT / name) for name in ("README.md", "archive/README.md"))
    broken = indexes.find_broken_relative_links(link_paths)
    errors.extend(f"broken relative link: {item}" for item in broken)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
    else:
        print(
            f"Validation passed for {len(folders)} physical folders and "
            f"{len(safe_metadata)} safe metadata records."
        )

    print(f"Warnings: {len(warnings)}")
    if warnings:
        print("- All Phase 1 confidence values remain yellow until manually revised.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
