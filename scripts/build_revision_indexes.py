#!/usr/bin/env python3
"""Build deterministic revision indexes from canonical REVISION.md files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REVISION_ROOT = ROOT / "revision"
FOLDER_RE = re.compile(r"^(\d{4})-(.+)$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

PATTERNS = [
    "Hashing",
    "Two Pointers",
    "Sliding Window",
    "Prefix Sum / Prefix-Suffix",
    "Binary Search",
    "Stack",
    "Monotonic Stack / Queue",
    "Linked List Techniques",
    "Tree DFS / Recursion",
    "Tree BFS",
    "BST",
    "Graph DFS / BFS",
    "Topological Sort",
    "Union Find",
    "Heap / Priority Queue",
    "Backtracking",
    "Greedy",
    "Dynamic Programming",
    "Bit Manipulation",
    "Intervals",
    "Trie",
    "Matrix / Grid",
    "Simulation / Math",
    "SQL / Database",
    "Design",
    "Other",
]

TOPICS = [
    "Array",
    "String",
    "Linked List",
    "Binary Tree",
    "BST",
    "Tree",
    "Graph",
    "Matrix",
    "Heap",
    "Trie",
    "Stack",
    "Queue",
    "Hash Table",
    "Math",
    "Bit Manipulation",
    "Dynamic Programming",
    "Database",
    "Design",
    "Concurrency",
    "Other",
]

PATTERN_GUIDANCE = {
    "Hashing": (
        "Fast membership, frequency, grouping, or complement lookup.",
        "Store the smallest state that turns repeated searches into average O(1) lookups.",
    ),
    "Two Pointers": (
        "Ordered data, paired choices, or an in-place partition/traversal.",
        "Move the side that cannot improve while preserving a clear pointer invariant.",
    ),
    "Sliding Window": (
        "A contiguous range whose condition can be updated at its boundaries.",
        "Expand to gain candidates and shrink only enough to restore the invariant.",
    ),
    "Prefix Sum / Prefix-Suffix": (
        "Repeated range totals or information needed from both sides of each index.",
        "Precompute or carry aggregates so each position combines reusable left/right state.",
    ),
    "Binary Search": (
        "A sorted domain or a monotone yes/no predicate.",
        "Maintain meaningful bounds and discard half of the remaining search space.",
    ),
    "Stack": (
        "Nested structure, deferred work, or last-in-first-out matching.",
        "Keep unfinished context on the stack and resolve the most recent dependency first.",
    ),
    "Monotonic Stack / Queue": (
        "Nearest greater/smaller queries or candidates that become permanently dominated.",
        "Discard dominated entries while preserving the order needed by future queries.",
    ),
    "Linked List Techniques": (
        "Pointer rewiring, relative node positions, or cycle structure.",
        "Name pointer roles and update links without losing access to the remaining list.",
    ),
    "Tree DFS / Recursion": (
        "Subtree answers combine at a node or path state flows from root to leaf.",
        "Define what each recursive call returns, then combine child results once.",
    ),
    "Tree BFS": (
        "Level order, minimum depth, or per-level aggregation.",
        "Treat the queue as the next frontier and process one complete level at a time.",
    ),
    "BST": (
        "Ordered subtrees allow pruning or sorted inorder traversal.",
        "Use the ordering invariant to avoid branches that cannot contain the answer.",
    ),
    "Graph DFS / BFS": (
        "Reachability, components, paths, or transitions between states.",
        "Model adjacency explicitly and mark a state before it can be scheduled twice.",
    ),
    "Topological Sort": (
        "Prerequisites or dependencies that require a directed ordering.",
        "Remove zero-indegree nodes or use three-state DFS; a cycle blocks a valid order.",
    ),
    "Union Find": (
        "Repeated connectivity checks while relationships are added.",
        "Represent each component by a root and merge roots with compression and rank/size.",
    ),
    "Heap / Priority Queue": (
        "Repeated access to the next extreme item or maintenance of a top-k set.",
        "Keep only live candidates and let the heap expose the next one to process.",
    ),
    "Backtracking": (
        "Enumerating constrained choices with reversible decisions.",
        "Choose, recurse, and undo, pruning a branch as soon as it cannot succeed.",
    ),
    "Greedy": (
        "A locally best choice leaves an equivalent smaller problem.",
        "Maintain the strongest feasible state and justify choices by dominance or exchange.",
    ),
    "Dynamic Programming": (
        "Overlapping subproblems with a compact reusable state.",
        "Define state, base cases, and transitions before choosing memoization or tabulation.",
    ),
    "Bit Manipulation": (
        "Parity, masks, powers of two, or cancellation identities.",
        "Reason per bit or apply a proven identity while respecting integer representation.",
    ),
    "Intervals": (
        "Ranges that overlap, cover, or compete for time.",
        "Sort by the useful endpoint and compare against one active boundary.",
    ),
    "Trie": (
        "Many prefix queries over the same collection of words.",
        "Each node represents a prefix; terminal state distinguishes a word from a prefix.",
    ),
    "Matrix / Grid": (
        "Neighbor relationships or row/column structure define the state space.",
        "Translate each cell to bounded neighbors or reusable row/column aggregates.",
    ),
    "Simulation / Math": (
        "Explicit process rules or a compact arithmetic identity.",
        "Translate rules to state updates, or prove the identity before replacing simulation.",
    ),
    "SQL / Database": (
        "A relational filter, join, grouping, or ranking operation.",
        "Build the correct row grain first, then filter, aggregate, or rank with NULLs in mind.",
    ),
    "Design": (
        "A sequence of operations with explicit per-operation complexity requirements.",
        "Choose state that makes the hardest operation direct and maintain its invariants.",
    ),
    "Other": (
        "A direct transformation or specialized invariant fits better than a broad family.",
        "State the problem-specific invariant and keep every update faithful to it.",
    ),
}


class FrontmatterError(ValueError):
    pass


def normalize_slug(value: str) -> str:
    return re.sub(r"-+", "-", value.strip().lower())


def slugify(value: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value.lower())).strip("-")


def discover_canonical_folders() -> list[Path]:
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and FOLDER_RE.fullmatch(path.name)
    )


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise FrontmatterError("missing opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise FrontmatterError("missing closing frontmatter delimiter") from exc

    data: dict[str, object] = {}
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        if ":" not in line:
            raise FrontmatterError(f"line {number} is not a key/value pair")
        key, raw = line.split(":", 1)
        key = key.strip()
        raw = raw.strip()
        if not key or key in data:
            raise FrontmatterError(f"line {number} has an empty or duplicate key")
        if raw == "":
            value: object = None
        else:
            try:
                value = json.loads(raw)
            except json.JSONDecodeError:
                value = raw
        data[key] = value
    return data


def load_entries() -> tuple[list[dict[str, object]], list[tuple[str, str]]]:
    entries: list[dict[str, object]] = []
    unclassified: list[tuple[str, str]] = []
    folder_slugs: dict[str, str] = {}
    metadata_slugs: dict[str, str] = {}

    for folder in discover_canonical_folders():
        folder_slug = normalize_slug(FOLDER_RE.fullmatch(folder.name).group(2))  # type: ignore[union-attr]
        if folder_slug in folder_slugs:
            raise ValueError(
                f"Duplicate normalized folder slug: {folder_slugs[folder_slug]} and {folder.name}"
            )
        folder_slugs[folder_slug] = folder.name

        revision = folder / "REVISION.md"
        if not revision.is_file():
            unclassified.append((folder.name, "missing REVISION.md"))
            continue
        try:
            data = parse_frontmatter(revision)
        except (OSError, FrontmatterError) as exc:
            unclassified.append((folder.name, str(exc)))
            continue

        slug = data.get("slug")
        if not isinstance(slug, str) or not slug:
            unclassified.append((folder.name, "missing valid slug metadata"))
            continue
        if slug in metadata_slugs:
            raise ValueError(
                f"Duplicate metadata slug {slug!r}: {metadata_slugs[slug]} and {folder.name}"
            )
        metadata_slugs[slug] = folder.name
        data = dict(data)
        data["folder"] = folder.name
        entries.append(data)

    entries.sort(key=lambda item: (int(item.get("leetcode_id", sys.maxsize)), str(item.get("slug", ""))))
    return entries, sorted(unclassified)


def md_cell(value: object) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def compact_cell(value: object, limit: int = 44) -> str:
    text = md_cell(value)
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def bool_cell(value: object) -> str:
    return "yes" if value is True else "no"


def render_tracker(entries: list[dict[str, object]]) -> str:
    lines = [
        "# Master Revision Tracker",
        "",
        "Generated from the 334 physical canonical problem folders. Edit each problem's `REVISION.md`, then rebuild the indexes.",
        "",
        "| LC | Problem | Topic | Current Approach | Target Pattern | Variant | Quality | Confidence | Redo | Revision |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        folder = str(entry["folder"])
        title = md_cell(entry["title"])
        topics = ", ".join(entry.get("topics", []))
        lines.append(
            "| {lc} | [{title}](../{folder}/README.md) | {topics} | {current} | {pattern} | {variant} | {quality} | {confidence} | {redo} | [notes](../{folder}/REVISION.md) |".format(
                lc=entry["leetcode_id"],
                title=title,
                folder=folder,
                topics=md_cell(topics),
                current=compact_cell(entry["current_approach"]),
                pattern=md_cell(entry["target_pattern"]),
                variant=compact_cell(entry["pattern_variant"]),
                quality=md_cell(entry["solution_quality"]),
                confidence=md_cell(entry["confidence"]),
                redo=bool_cell(entry["redo"]),
            )
        )
    return "\n".join(lines) + "\n"


def render_pattern_readme(entries: list[dict[str, object]]) -> str:
    counts = defaultdict(int)
    for entry in entries:
        counts[str(entry["target_pattern"])] += 1
    lines = [
        "# Pattern Index",
        "",
        "Use these major families for recognition practice. Specific techniques live as variants inside each page.",
        "",
        "| Pattern | Problems |",
        "| --- | ---: |",
    ]
    for pattern in PATTERNS:
        lines.append(f"| [{pattern}]({slugify(pattern)}.md) | {counts[pattern]} |")
    return "\n".join(lines) + "\n"


def render_pattern_page(pattern: str, entries: list[dict[str, object]]) -> str:
    relevant = [entry for entry in entries if entry.get("target_pattern") == pattern]
    variants = sorted({str(entry["pattern_variant"]) for entry in relevant})
    recognition, mental_model = PATTERN_GUIDANCE[pattern]
    lines = [
        f"# {pattern}",
        "",
        "[Pattern index](README.md) | [Revision dashboard](../README.md)",
        "",
        "## Recognition Signals",
        "",
        recognition,
        "",
        "## Mental Model",
        "",
        mental_model,
        "",
        "## Variants",
        "",
    ]
    if variants:
        lines.extend(f"- {variant}" for variant in variants)
    else:
        lines.append("No variants are represented by the current physical problem set.")
    lines += [
        "",
        "## Problems",
        "",
        "| LC | Problem | Variant | Quality | Confidence | Redo |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    if relevant:
        for entry in relevant:
            lines.append(
                "| {lc} | [{title}](../../{folder}/REVISION.md) | {variant} | {quality} | {confidence} | {redo} |".format(
                    lc=entry["leetcode_id"],
                    title=md_cell(entry["title"]),
                    folder=entry["folder"],
                    variant=md_cell(entry["pattern_variant"]),
                    quality=md_cell(entry["solution_quality"]),
                    confidence=md_cell(entry["confidence"]),
                    redo=bool_cell(entry["redo"]),
                )
            )
    else:
        lines.append("| - | No physical problems currently classified here | - | - | - | - |")
    return "\n".join(lines) + "\n"


def render_topic_page(topic: str, entries: list[dict[str, object]]) -> str:
    relevant = [entry for entry in entries if topic in entry.get("topics", [])]
    lines = [
        f"# {topic}",
        "",
        "[Revision dashboard](../README.md)",
        "",
        "| LC | Problem | Target Pattern | Quality | Confidence |",
        "| ---: | --- | --- | --- | --- |",
    ]
    if relevant:
        for entry in relevant:
            lines.append(
                "| {lc} | [{title}](../../{folder}/REVISION.md) | {pattern} | {quality} | {confidence} |".format(
                    lc=entry["leetcode_id"],
                    title=md_cell(entry["title"]),
                    folder=entry["folder"],
                    pattern=md_cell(entry["target_pattern"]),
                    quality=md_cell(entry["solution_quality"]),
                    confidence=md_cell(entry["confidence"]),
                )
            )
    else:
        lines.append("| - | No physical problems currently tagged with this topic | - | - | - |")
    return "\n".join(lines) + "\n"


def render_topic_readme(entries: list[dict[str, object]]) -> str:
    counts = defaultdict(int)
    for entry in entries:
        for topic in entry.get("topics", []):
            counts[str(topic)] += 1
    lines = [
        "# Topic Index",
        "",
        "Topics describe the data domain. Use the pattern pages to practice algorithm recognition.",
        "",
        "| Topic | Problems |",
        "| --- | ---: |",
    ]
    for topic in TOPICS:
        lines.append(f"| [{topic}]({slugify(topic)}.md) | {counts[topic]} |")
    return "\n".join(lines) + "\n"


def render_must_redo(entries: list[dict[str, object]]) -> str:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for entry in entries:
        if entry.get("redo") is True:
            groups[str(entry["target_pattern"])].append(entry)
    lines = [
        "# Must Redo",
        "",
        "Generated from `redo: true`. Work from recognition and the problem statement before opening the saved solution.",
    ]
    for pattern in PATTERNS:
        relevant = groups.get(pattern, [])
        if not relevant:
            continue
        lines += [
            "",
            f"## {pattern}",
            "",
            "| LC | Problem | Current Approach | Variant | Quality |",
            "| ---: | --- | --- | --- | --- |",
        ]
        for entry in relevant:
            lines.append(
                "| {lc} | [{title}](../../{folder}/REVISION.md) | {current} | {variant} | {quality} |".format(
                    lc=entry["leetcode_id"],
                    title=md_cell(entry["title"]),
                    folder=entry["folder"],
                    current=md_cell(entry["current_approach"]),
                    variant=md_cell(entry["pattern_variant"]),
                    quality=md_cell(entry["solution_quality"]),
                )
            )
    if not groups:
        lines += ["", "No problems are currently marked for redo."]
    return "\n".join(lines) + "\n"


def render_weak(entries: list[dict[str, object]]) -> str:
    weak = [entry for entry in entries if entry.get("confidence") == "red"]
    lines = [
        "# Weak Problems",
        "",
        "Generated from `confidence: red`. Every Phase 1 problem starts yellow, so this queue will populate as confidence is updated manually.",
        "",
        "| LC | Problem | Target Pattern | Variant | Redo |",
        "| ---: | --- | --- | --- | --- |",
    ]
    if weak:
        for entry in weak:
            lines.append(
                "| {lc} | [{title}](../../{folder}/REVISION.md) | {pattern} | {variant} | {redo} |".format(
                    lc=entry["leetcode_id"],
                    title=md_cell(entry["title"]),
                    folder=entry["folder"],
                    pattern=md_cell(entry["target_pattern"]),
                    variant=md_cell(entry["pattern_variant"]),
                    redo=bool_cell(entry["redo"]),
                )
            )
    else:
        lines.append("| - | No red-confidence problems yet | - | - | - |")
    return "\n".join(lines) + "\n"


def render_unclassified(unclassified: list[tuple[str, str]]) -> str:
    lines = [
        "# Unclassified Physical Problems",
        "",
        "Canonical folders missing usable `REVISION.md` metadata appear here after regeneration.",
        "",
        "| Folder | Reason |",
        "| --- | --- |",
    ]
    if unclassified:
        for folder, reason in unclassified:
            lines.append(f"| [{folder}](../{folder}/) | {md_cell(reason)} |")
    else:
        lines.append("| - | All physical canonical problems have readable revision metadata. |")
    return "\n".join(lines) + "\n"


def expected_outputs(
    entries: list[dict[str, object]], unclassified: list[tuple[str, str]]
) -> dict[Path, str]:
    outputs = {
        REVISION_ROOT / "tracker.md": render_tracker(entries),
        REVISION_ROOT / "unclassified.md": render_unclassified(unclassified),
        REVISION_ROOT / "patterns" / "README.md": render_pattern_readme(entries),
        REVISION_ROOT / "topics" / "README.md": render_topic_readme(entries),
        REVISION_ROOT / "queues" / "must-redo.md": render_must_redo(entries),
        REVISION_ROOT / "queues" / "weak-problems.md": render_weak(entries),
    }
    for pattern in PATTERNS:
        outputs[REVISION_ROOT / "patterns" / f"{slugify(pattern)}.md"] = render_pattern_page(
            pattern, entries
        )
    for topic in TOPICS:
        outputs[REVISION_ROOT / "topics" / f"{slugify(topic)}.md"] = render_topic_page(
            topic, entries
        )
    return outputs


def find_broken_relative_links(paths: list[Path]) -> list[str]:
    broken: list[str] = []
    for path in sorted(set(paths)):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8-sig")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            if not resolved.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {raw_target}")
    return broken


def build(check: bool) -> int:
    try:
        entries, unclassified = load_entries()
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    outputs = expected_outputs(entries, unclassified)
    stale: list[str] = []
    for path, content in sorted(outputs.items()):
        if check:
            actual = path.read_text(encoding="utf-8-sig") if path.is_file() else None
            if actual != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    if stale:
        print("Generated revision indexes are stale or missing:")
        for path in stale:
            print(f"- {path}")
        return 1

    link_paths = list(outputs)
    link_paths += [folder / "REVISION.md" for folder in discover_canonical_folders()]
    dashboard = REVISION_ROOT / "README.md"
    if dashboard.is_file():
        link_paths.append(dashboard)
    broken = find_broken_relative_links(link_paths)
    if broken:
        print("Broken relative links:", file=sys.stderr)
        for item in broken:
            print(f"- {item}", file=sys.stderr)
        return 1

    verb = "Checked" if check else "Generated"
    print(
        f"{verb} {len(outputs)} index files from {len(entries)} classified physical problems; "
        f"{len(unclassified)} unclassified."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files differ")
    args = parser.parse_args()
    return build(args.check)


if __name__ == "__main__":
    raise SystemExit(main())
