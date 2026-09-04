# Interview Revision Dashboard

This repository keeps each synced LeetCode problem in its original physical folder. The revision layer links those canonical folders by interview pattern and topic without copying or regrouping solutions.

## Start Here

- [Master tracker](tracker.md)
- [Pattern index](patterns/README.md)
- [Topic index](topics/README.md)
- [Must redo](queues/must-redo.md)
- [Weak problems](queues/weak-problems.md)
- [Unclassified physical problems](unclassified.md)

## Revision Loop

1. Open a pattern page and choose a problem without reading its saved code.
2. Explain the recognition signal, invariant, target complexity, and edge cases aloud.
3. Re-derive and implement the target approach under interview conditions.
4. Compare with the historical `solution.*` and the problem's `REVISION.md`.
5. Update `confidence`, `last_revised`, and `redo` in `REVISION.md`.
6. Run `python scripts/build_revision_indexes.py` to refresh every navigation page.

Confidence is intentionally personal: every migrated problem begins `yellow`. Use `red` when the approach cannot yet be derived reliably and `green` only after a clean independent redo.

## Metadata Meaning

- `current_approach` describes what the saved accepted code actually does.
- `target_pattern` and `pattern_variant` describe the interview technique worth knowing.
- `solution_quality` evaluates the saved implementation, not whether LeetCode once accepted it.
- `redo` identifies an algorithm, correctness, complexity, or code-cleanliness issue worth revisiting.
- `topics` describe the data domain; they are separate from algorithmic patterns.

## Practice Coverage

Build fluency across arrays and strings, linked structures, stacks and queues, trees and BSTs, graphs, heaps, tries, dynamic programming, backtracking, greedy reasoning, bit manipulation, matrix traversal, and database queries. For each family, practice recognizing the clue before memorizing an implementation.

## Sync Boundary

Problem-folder `README.md` and `solution.*` files are historical sync-managed artifacts. Custom interview knowledge belongs in `REVISION.md`. Folder prefixes are sync IDs, not reliable frontend LeetCode IDs; canonical identity comes from `slug` plus the checked-in [safe metadata map](problem_metadata.json).

Phase 1 covers only the 334 physical synced problem folders. The 209 accepted solutions embedded only in `dashboard/problems.json` are intentionally deferred to Phase 2.
