# LeetCode Reorganization Audit

Audit date: 2026-09-04

Scope: audit and planning only. No repository files were moved, renamed, deleted, committed, or pushed. The only intended local change is this uncommitted audit report.

Sources used: local repository at `C:\GithubRepos\Leetcode`, local `dashboard/problems.json`, local `.github/workflows/sync_leetcode.yml`, and the public `joshcai/leetcode-sync` README at https://github.com/joshcai/leetcode-sync. No live LeetCode account/API fetch was run during this audit.

## Executive Summary

- Synced problem directories found: 334.
- Root-level standalone legacy LeetCode Python solutions found: 26.
- De-duplicated solved problem records with code found in the repo: 543 by LeetCode slug.
- Physical canonical candidates among those records: 334.
- Dashboard-only embedded accepted solutions: 209.
- Stale dashboard folder-derived records without `leetcode_slug`: 109.
- Synced folders where directory sync ID differs from actual frontend LC ID: 125.
- Duplicate legacy mappings: A=22, B=1, C=3, D=0.

Primary recommendation: keep physical synced folders as canonical locations, add `REVISION.md` beside generated files, generate pattern/topic/tracker pages as links only, and treat all leading folder numbers as sync/internal IDs unless validated by slug metadata.

## Current Repository Structure Summary

- Root contains 334 `NNNN-slug/` problem directories. Every one has `README.md` and at least one `solution.*`.
- Root contains 26 old standalone problem files. All 26 map to a synced directory by actual title/slug.
- Root docs are `README.md`, `leetcode.md`, and `roadmap.md`; they are historical/reference material, not a generated revision system.
- `.github/workflows/sync_leetcode.yml` runs `joshcai/leetcode-sync@v1.7` weekly and manually, with no `destination-folder`, so output is expected at repo root.
- `dashboard/` is a separate dashboard/data system; its JSON includes API-enriched solved records and accepted code.
- `000/00000/aaaaa.md` is a placeholder-like pattern note, not a canonical problem directory.

## Sync Safety

- Observed sync-managed files are problem-folder `README.md` plus `solution.py` or `solution.sql`; custom notes should avoid editing them.
- `REVISION.md` appears safe because it is not part of the observed generated pair, but validate after the next sync run.
- `joshcai/leetcode-sync` documents accepted-solution syncing, optional `destination-folder`, and default-branch commits; this repo omits `destination-folder`.
- Sync/internal IDs are unsafe as frontend IDs. Examples: `0745-find-smallest-letter-greater-than-target` is LC 744, `0774-maximum-depth-of-n-ary-tree` is LC 559, `1397-search-suggestions-system` is LC 1268.
- The public issue list for the action includes an open `wrong problem number` issue, consistent with the local mismatch risk.

## Proposed Revision Architecture Evaluation

The proposed `revision/` architecture is sound: canonical problem folders stay sync-compatible, and pattern/topic pages are generated link indexes instead of duplicated solution copies.

```text
revision/
  README.md
  tracker.md
  unclassified.md
  patterns/
  topics/
  queues/
scripts/
  build_revision_indexes.py
  validate_revision_metadata.py
<problem-folder>/
  README.md          # sync-managed
  solution.py|sql    # sync-managed
  REVISION.md        # custom revision metadata and notes
  alternatives/      # only for distinct alternate approaches
```

## Per-Problem REVISION.md Format

```markdown
---
leetcode_id:
sync_id:
title:
slug:
difficulty:
topics: []
primary_pattern:
secondary_patterns: []
confidence: yellow
last_revised:
---

# <Problem>

## Recognition

## Core Idea

## Invariant / Mental Model

## Complexity
Time:
Space:

## Common Mistake

## Alternative Approaches

## What I Should Remember

## Redo Test
Can I derive this from scratch without seeing the saved solution?
```

Initial confidence should be `yellow` for every generated file. Do not infer confidence from solved status.

## Proposed Final Pattern Taxonomy

- Hashing
- Complement Lookup
- Two Pointers
- Fast & Slow Pointers
- Sliding Window
- Prefix Sum
- Prefix/Suffix Precomputation
- Binary Search
- Intervals
- Sorting
- Partitioning / Dutch National Flag
- Index Placement / Cyclic Sort
- Stack
- Monotonic Stack
- Monotonic Queue
- Queue
- BFS
- DFS
- Backtracking
- Greedy
- Heap / Priority Queue
- Trie
- Tree Traversal
- BST Search / Bounds
- Tree Postorder / Return Information
- Topological Sort
- Union Find
- Shortest Path
- 1D Dynamic Programming
- Grid Dynamic Programming
- String Dynamic Programming
- Knapsack / Take-Skip
- State Machine DP
- Bit Manipulation
- Divide and Conquer
- Simulation
- Design
- Reservoir Sampling / Randomized
- Matrix Traversal
- SQL Filtering
- SQL Join
- SQL Aggregation
- SQL Window/Ranking
- SQL Self Join
- Concurrency
- NEEDS_REVIEW

## Proposed Final Topic Taxonomy

- Array
- String
- Linked List
- Stack
- Queue
- Binary Tree
- BST
- Tree
- Graph
- Matrix
- Heap
- Trie
- Hash Table
- Math
- Bit Manipulation
- Dynamic Programming
- Greedy
- Design
- Database
- Concurrency
- Interactive
- Non-DSA / Language Basics

## Legacy File and Duplicate Mapping

Duplicate categories: A = exact/essentially identical solution, B = same algorithm with implementation differences, C = different valid algorithm/approach, D = uncertain match.

| Legacy file | LC | Title | Canonical synced directory | Category | Approach verdict |
| --- | --- | --- | --- | --- | --- |
| 1004. Max Consecutive Ones III.py | 1004 | Max Consecutive Ones III | 1046-max-consecutive-ones-iii | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 1071.Greatest Common Divisor of Strings.py | 1071 | Greatest Common Divisor of Strings | 1146-greatest-common-divisor-of-strings | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 111. Minimum Depth of Binary Tree.py | 111 | Minimum Depth of Binary Tree | 0111-minimum-depth-of-binary-tree | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 1161. Maximum Level Sum of a Binary Tree.py | 1161 | Maximum Level Sum of a Binary Tree | 1116-maximum-level-sum-of-a-binary-tree | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 1268 Search Suggestions System.py | 1268 | Search Suggestions System | 1397-search-suggestions-system | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 128. Longest Consecutive Sequence.py | 128 | Longest Consecutive Sequence | 0128-longest-consecutive-sequence | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 1431.  Kids With the Greatest Number of Candies.py | 1431 | Kids With the Greatest Number of Candies | 1528-kids-with-the-greatest-number-of-candies | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 1456. Maximum Number of Vowels in a Subs.py | 1456 | Maximum Number of Vowels in a Substring of Given Length | 1567-maximum-number-of-vowels-in-a-substring-of-given-length | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 16. 3Sum Closest.py | 16 | 3Sum Closest | 0016-3sum-closest | B | Same sorted two-pointer algorithm; synced code has small loop/sort/comment differences. |
| 208. Implement Trie (Prefix Tree).py | 208 | Implement Trie (Prefix Tree) | 0208-implement-trie-prefix-tree | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 2095. Delete the Middle Node of a Linked.py | 2095 | Delete the Middle Node of a Linked List | 2216-delete-the-middle-node-of-a-linked-list | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 222. Count Complete Tree Nodes.py | 222 | Count Complete Tree Nodes | 0222-count-complete-tree-nodes | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 328. Odd Even Linked List.py | 328 | Odd Even Linked List | 0328-odd-even-linked-list | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 33. Search in Rotated Sorted Array.py | 33 | Search in Rotated Sorted Array | 0033-search-in-rotated-sorted-array | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 35. Search Insert Position.py | 35 | Search Insert Position | 0035-search-insert-position | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 448. Find All Numbers Disappeared in an Array.py | 448 | Find All Numbers Disappeared in an Array | 0448-find-all-numbers-disappeared-in-an-array | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 543.Diameter of Binary Tree.py | 543 | Diameter of Binary Tree | 0543-diameter-of-binary-tree | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 605.Can Place Flowers.py | 605 | Can Place Flowers | 0605-can-place-flowers | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 724.Find Pivot Index.py | 724 | Find Pivot Index | 0724-find-pivot-index | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 744.Find Smallest Letter Greater Than Target.py | 744 | Find Smallest Letter Greater Than Target | 0745-find-smallest-letter-greater-than-target | A | Executable solution is exact/essentially identical after removing comments, docstrings, and whitespace. |
| 75. Sort Colors.py | 75 | Sort Colors | 0075-sort-colors | C | Legacy counts 0/1/2 in multiple passes; synced uses Dutch National Flag low/current/high pointers. |
| 81. Search in Rotated Sorted Array II.py | 81 | Search in Rotated Sorted Array II | 0081-search-in-rotated-sorted-array-ii | C | Legacy has duplicate-aware rotated binary search; synced executable is linear membership, with binary search only commented. |
| 83. Remove Duplicates from Sorted List.py | 83 | Remove Duplicates from Sorted List | 0083-remove-duplicates-from-sorted-list | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 872. Leaf-Similar Trees.py | 872 | Leaf-Similar Trees | 0904-leaf-similar-trees | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 901. Online Stock Span.py | 901 | Online Stock Span | 0937-online-stock-span | A | Executable solution is exact/essentially identical after removing comments and whitespace. |
| 977. Squares of a Sorted Array.py | 977 | Squares of a Sorted Array | 1019-squares-of-a-sorted-array | C | Legacy splits negatives/non-negatives then merges; synced uses two pointers from both ends. |

Category C legacy files should not be deleted. They should become alternate solutions under the canonical directory once migration begins.

## Complete Solved-Problem Classification Table - Physical Canonical Folders

This table also serves as the synced problem directory inventory. `Sync ID` is the numeric directory prefix; `LC` is the frontend problem number matched by slug from local API-enriched dashboard metadata.

| LC | Sync ID | Title | Current location | Solution file(s) | README | Topic(s) | Primary pattern | Secondary patterns | Duplicate/alternate status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0001 | Two Sum | 0001-two-sum | solution.py | yes | Array, Hash Table | Complement Lookup | Hashing | canonical folder |
| 2 | 0002 | Add Two Numbers | 0002-add-two-numbers | solution.py | yes | Linked List, Math | Simulation | Math | canonical folder |
| 3 | 0003 | Longest Substring Without Repeating Characters | 0003-longest-substring-without-repeating-characters | solution.py | yes | Hash Table, String | Sliding Window | Hashing | canonical folder |
| 4 | 0004 | Median of Two Sorted Arrays | 0004-median-of-two-sorted-arrays | solution.py | yes | Array | Binary Search | Divide and Conquer | canonical folder |
| 5 | 0005 | Longest Palindromic Substring | 0005-longest-palindromic-substring | solution.py | yes | String | Two Pointers | Dynamic Programming | canonical folder |
| 6 | 0006 | Zigzag Conversion | 0006-zigzag-conversion | solution.py | yes | String | Simulation | - | canonical folder |
| 7 | 0007 | Reverse Integer | 0007-reverse-integer | solution.py | yes | Math | Simulation | Math | canonical folder |
| 8 | 0008 | String to Integer (atoi) | 0008-string-to-integer-atoi | solution.py | yes | String | Simulation | - | canonical folder |
| 9 | 0009 | Palindrome Number | 0009-palindrome-number | solution.py | yes | Math | Simulation | Math | canonical folder |
| 10 | 0010 | Regular Expression Matching | 0010-regular-expression-matching | solution.py | yes | String | String Dynamic Programming | Dynamic Programming | canonical folder |
| 11 | 0011 | Container With Most Water | 0011-container-with-most-water | solution.py | yes | Array | Two Pointers | Greedy | canonical folder |
| 12 | 0012 | Integer to Roman | 0012-integer-to-roman | solution.py | yes | Hash Table, Math, String | Greedy | Hashing, Math | canonical folder |
| 13 | 0013 | Roman to Integer | 0013-roman-to-integer | solution.py | yes | Hash Table, Math, String | Hashing | Math | canonical folder |
| 14 | 0014 | Longest Common Prefix | 0014-longest-common-prefix | solution.py | yes | Array, String, Trie | String Scanning | Trie | canonical folder |
| 15 | 0015 | 3Sum | 0015-3sum | solution.py | yes | Array | Two Pointers | Sorting | canonical folder |
| 16 | 0016 | 3Sum Closest | 0016-3sum-closest | solution.py | yes | Array | Two Pointers | Sorting | legacy same algorithm variant: 16. 3Sum Closest.py |
| 17 | 0017 | Letter Combinations of a Phone Number | 0017-letter-combinations-of-a-phone-number | solution.py | yes | Hash Table, String | Backtracking | Hashing | canonical folder |
| 18 | 0018 | 4Sum | 0018-4sum | solution.py | yes | Array | Two Pointers | Sorting | canonical folder |
| 19 | 0019 | Remove Nth Node From End of List | 0019-remove-nth-node-from-end-of-list | solution.py | yes | Linked List | Fast & Slow Pointers | Two Pointers | canonical folder |
| 20 | 0020 | Valid Parentheses | 0020-valid-parentheses | solution.py | yes | String, Stack | Stack | - | canonical folder |
| 21 | 0021 | Merge Two Sorted Lists | 0021-merge-two-sorted-lists | solution.py | yes | Linked List | NEEDS_REVIEW | - | canonical folder |
| 22 | 0022 | Generate Parentheses | 0022-generate-parentheses | solution.py | yes | String | Backtracking | Dynamic Programming | canonical folder |
| 24 | 0024 | Swap Nodes in Pairs | 0024-swap-nodes-in-pairs | solution.py | yes | Linked List | NEEDS_REVIEW | - | canonical folder |
| 26 | 0026 | Remove Duplicates from Sorted Array | 0026-remove-duplicates-from-sorted-array | solution.py | yes | Array | Two Pointers | - | canonical folder |
| 27 | 0027 | Remove Element | 0027-remove-element | solution.py | yes | Array | Two Pointers | - | canonical folder |
| 28 | 0028 | Find the Index of the First Occurrence in a String | 0028-find-the-index-of-the-first-occurrence-in-a-string | solution.py | yes | String | String Scanning | Two Pointers, String Matching | canonical folder |
| 31 | 0031 | Next Permutation | 0031-next-permutation | solution.py | yes | Array | Two Pointers | - | canonical folder |
| 32 | 0032 | Longest Valid Parentheses | 0032-longest-valid-parentheses | solution.py | yes | String, Stack | Stack | Dynamic Programming | canonical folder |
| 33 | 0033 | Search in Rotated Sorted Array | 0033-search-in-rotated-sorted-array | solution.py | yes | Array | Binary Search | - | legacy exact duplicate: 33. Search in Rotated Sorted Array.py |
| 35 | 0035 | Search Insert Position | 0035-search-insert-position | solution.py | yes | Array | Binary Search | - | legacy exact duplicate: 35. Search Insert Position.py |
| 36 | 0036 | Valid Sudoku | 0036-valid-sudoku | solution.py | yes | Array, Hash Table, Matrix | Hashing | Matrix Traversal | canonical folder |
| 37 | 0037 | Sudoku Solver | 0037-sudoku-solver | solution.py | yes | Array, Hash Table, Matrix | Backtracking | Hashing, Matrix Traversal | canonical folder |
| 38 | 0038 | Count and Say | 0038-count-and-say | solution.py | yes | String | Simulation | - | canonical folder |
| 39 | 0039 | Combination Sum | 0039-combination-sum | solution.py | yes | Array | Backtracking | - | canonical folder |
| 42 | 0042 | Trapping Rain Water | 0042-trapping-rain-water | solution.py | yes | Array, Stack | Prefix/Suffix Precomputation | Two Pointers, Dynamic Programming, Stack, Monotonic Stack | canonical folder |
| 43 | 0043 | Multiply Strings | 0043-multiply-strings | solution.py | yes | Math, String | Simulation | Math | canonical folder |
| 44 | 0044 | Wildcard Matching | 0044-wildcard-matching | solution.py | yes | String | Greedy | Dynamic Programming | canonical folder |
| 45 | 0045 | Jump Game II | 0045-jump-game-ii | solution.py | yes | Array | Greedy | Dynamic Programming | canonical folder |
| 49 | 0049 | Group Anagrams | 0049-group-anagrams | solution.py | yes | Array, Hash Table, String | Hashing | Sorting | canonical folder |
| 50 | 0050 | Pow(x, n) | 0050-powx-n | solution.py | yes | Math | Math | - | canonical folder |
| 53 | 0053 | Maximum Subarray | 0053-maximum-subarray | solution.py | yes | Array | 1D Dynamic Programming | Divide and Conquer, Dynamic Programming | canonical folder |
| 55 | 0055 | Jump Game | 0055-jump-game | solution.py | yes | Array | Greedy | Dynamic Programming | canonical folder |
| 58 | 0058 | Length of Last Word | 0058-length-of-last-word | solution.py | yes | String | String Scanning | - | canonical folder |
| 61 | 0061 | Rotate List | 0061-rotate-list | solution.py | yes | Linked List | Fast & Slow Pointers | Two Pointers | canonical folder |
| 65 | 0065 | Valid Number | 0065-valid-number | solution.py | yes | String | NEEDS_REVIEW | - | canonical folder |
| 66 | 0066 | Plus One | 0066-plus-one | solution.py | yes | Array, Math | Simulation | Math | canonical folder |
| 67 | 0067 | Add Binary | 0067-add-binary | solution.py | yes | Math, String, Bit Manipulation | Simulation | Math, Bit Manipulation | canonical folder |
| 69 | 0069 | Sqrt(x) | 0069-sqrtx | solution.py | yes | Math | Binary Search | Math | canonical folder |
| 70 | 0070 | Climbing Stairs | 0070-climbing-stairs | solution.py | yes | Math | 1D Dynamic Programming | Math, Dynamic Programming | canonical folder |
| 71 | 0071 | Simplify Path | 0071-simplify-path | solution.py | yes | String, Stack | Stack | - | canonical folder |
| 74 | 0074 | Search a 2D Matrix | 0074-search-a-2d-matrix | solution.py | yes | Array, Matrix | Binary Search | Matrix Traversal | canonical folder |
| 75 | 0075 | Sort Colors | 0075-sort-colors | solution.py | yes | Array | Partitioning / Dutch National Flag | Two Pointers, Sorting | legacy alternate approach: 75. Sort Colors.py |
| 79 | 0079 | Word Search | 0079-word-search | solution.py | yes | Array, String, Matrix | Backtracking | DFS, Matrix Traversal | canonical folder |
| 80 | 0080 | Remove Duplicates from Sorted Array II | 0080-remove-duplicates-from-sorted-array-ii | solution.py | yes | Array | Two Pointers | - | canonical folder |
| 81 | 0081 | Search in Rotated Sorted Array II | 0081-search-in-rotated-sorted-array-ii | solution.py | yes | Array | NEEDS_REVIEW | Binary Search | legacy alternate approach: 81. Search in Rotated Sorted Array II.py |
| 83 | 0083 | Remove Duplicates from Sorted List | 0083-remove-duplicates-from-sorted-list | solution.py | yes | Linked List | Linked List Traversal | - | legacy exact duplicate: 83. Remove Duplicates from Sorted List.py |
| 86 | 0086 | Partition List | 0086-partition-list | solution.py | yes | Linked List | Two Pointers | - | canonical folder |
| 88 | 0088 | Merge Sorted Array | 0088-merge-sorted-array | solution.py | yes | Array | Two Pointers | Sorting | canonical folder |
| 89 | 0089 | Gray Code | 0089-gray-code | solution.py | yes | Math, Bit Manipulation | Backtracking | Math, Bit Manipulation | canonical folder |
| 92 | 0092 | Reverse Linked List II | 0092-reverse-linked-list-ii | solution.py | yes | Linked List | Linked List Reversal | - | canonical folder |
| 94 | 0094 | Binary Tree Inorder Traversal | 0094-binary-tree-inorder-traversal | solution.py | yes | Stack, Binary Tree | Tree Traversal | Stack, DFS | canonical folder |
| 98 | 0098 | Validate Binary Search Tree | 0098-validate-binary-search-tree | solution.py | yes | BST, Binary Tree | BST Search | DFS | canonical folder |
| 99 | 0099 | Recover Binary Search Tree | 0099-recover-binary-search-tree | solution.py | yes | BST, Binary Tree | Tree Traversal | DFS | canonical folder |
| 100 | 0100 | Same Tree | 0100-same-tree | solution.py | yes | Binary Tree | Tree Traversal | DFS, BFS | canonical folder |
| 101 | 0101 | Symmetric Tree | 0101-symmetric-tree | solution.py | yes | Binary Tree | Tree Traversal | DFS, BFS | canonical folder |
| 102 | 0102 | Binary Tree Level Order Traversal | 0102-binary-tree-level-order-traversal | solution.py | yes | Binary Tree | BFS | - | canonical folder |
| 103 | 0103 | Binary Tree Zigzag Level Order Traversal | 0103-binary-tree-zigzag-level-order-traversal | solution.py | yes | Binary Tree | BFS | - | canonical folder |
| 104 | 0104 | Maximum Depth of Binary Tree | 0104-maximum-depth-of-binary-tree | solution.py | yes | Binary Tree | Tree Traversal | DFS, BFS | canonical folder |
| 107 | 0107 | Binary Tree Level Order Traversal II | 0107-binary-tree-level-order-traversal-ii | solution.py | yes | Binary Tree | BFS | - | canonical folder |
| 110 | 0110 | Balanced Binary Tree | 0110-balanced-binary-tree | solution.py | yes | Binary Tree | Tree Postorder / Return Information | DFS | canonical folder |
| 111 | 0111 | Minimum Depth of Binary Tree | 0111-minimum-depth-of-binary-tree | solution.py | yes | Binary Tree | DFS | BFS | legacy exact duplicate: 111. Minimum Depth of Binary Tree.py |
| 112 | 0112 | Path Sum | 0112-path-sum | solution.py | yes | Binary Tree | DFS | BFS | canonical folder |
| 113 | 0113 | Path Sum II | 0113-path-sum-ii | solution.py | yes | Binary Tree | Backtracking | DFS | canonical folder |
| 114 | 0114 | Flatten Binary Tree to Linked List | 0114-flatten-binary-tree-to-linked-list | solution.py | yes | Linked List, Stack, Binary Tree | DFS | Stack | canonical folder |
| 116 | 0116 | Populating Next Right Pointers in Each Node | 0116-populating-next-right-pointers-in-each-node | solution.py | yes | Linked List, Binary Tree | DFS | BFS | canonical folder |
| 118 | 0118 | Pascal's Triangle | 0118-pascals-triangle | solution.py | yes | Array | Dynamic Programming | - | canonical folder |
| 121 | 0121 | Best Time to Buy and Sell Stock | 0121-best-time-to-buy-and-sell-stock | solution.py | yes | Array | Greedy | Dynamic Programming | canonical folder |
| 122 | 0122 | Best Time to Buy and Sell Stock II | 0122-best-time-to-buy-and-sell-stock-ii | solution.py | yes | Array | Greedy | Dynamic Programming | canonical folder |
| 125 | 0125 | Valid Palindrome | 0125-valid-palindrome | solution.py | yes | String | Two Pointers | - | canonical folder |
| 128 | 0128 | Longest Consecutive Sequence | 0128-longest-consecutive-sequence | solution.py | yes | Array, Hash Table | Hashing | - | legacy exact duplicate: 128. Longest Consecutive Sequence.py |
| 129 | 0129 | Sum Root to Leaf Numbers | 0129-sum-root-to-leaf-numbers | solution.py | yes | Binary Tree | DFS | - | canonical folder |
| 130 | 0130 | Surrounded Regions | 0130-surrounded-regions | solution.py | yes | Array, Matrix | DFS | BFS, Matrix Traversal | canonical folder |
| 133 | 0133 | Clone Graph | 0133-clone-graph | solution.py | yes | Hash Table, Graph | DFS | Hashing, BFS, Graph Traversal | canonical folder |
| 134 | 0134 | Gas Station | 0134-gas-station | solution.py | yes | Array | Greedy | - | canonical folder |
| 135 | 0135 | Candy | 0135-candy | solution.py | yes | Array | Greedy | - | canonical folder |
| 136 | 0136 | Single Number | 0136-single-number | solution.py | yes | Array, Bit Manipulation | Bit Manipulation | - | canonical folder |
| 139 | 0139 | Word Break | 0139-word-break | solution.py | yes | Array, Hash Table, String, Trie | 1D Dynamic Programming | Hashing, Dynamic Programming, Trie | canonical folder |
| 141 | 0141 | Linked List Cycle | 0141-linked-list-cycle | solution.py | yes | Hash Table, Linked List | Fast & Slow Pointers | Hashing, Two Pointers | canonical folder |
| 142 | 0142 | Linked List Cycle II | 0142-linked-list-cycle-ii | solution.py | yes | Hash Table, Linked List | Fast & Slow Pointers | Hashing, Two Pointers | canonical folder |
| 143 | 0143 | Reorder List | 0143-reorder-list | solution.py | yes | Linked List, Stack | Fast & Slow Pointers | Two Pointers, Stack | canonical folder |
| 144 | 0144 | Binary Tree Preorder Traversal | 0144-binary-tree-preorder-traversal | solution.py | yes | Stack, Binary Tree | Tree Traversal | Stack, DFS | canonical folder |
| 145 | 0145 | Binary Tree Postorder Traversal | 0145-binary-tree-postorder-traversal | solution.py | yes | Stack, Binary Tree | Tree Traversal | Stack, DFS | canonical folder |
| 146 | 0146 | LRU Cache | 0146-lru-cache | solution.py | yes | Hash Table, Linked List, Design | Design | Hashing | canonical folder |
| 150 | 0150 | Evaluate Reverse Polish Notation | 0150-evaluate-reverse-polish-notation | solution.py | yes | Array, Math, Stack | Stack | Math | canonical folder |
| 151 | 0151 | Reverse Words in a String | 0151-reverse-words-in-a-string | solution.py | yes | String | Two Pointers | - | canonical folder |
| 153 | 0153 | Find Minimum in Rotated Sorted Array | 0153-find-minimum-in-rotated-sorted-array | solution.py | yes | Array | Binary Search | - | canonical folder |
| 155 | 0155 | Min Stack | 0155-min-stack | solution.py | yes | Stack, Design | Design | Stack | canonical folder |
| 160 | 0160 | Intersection of Two Linked Lists | 0160-intersection-of-two-linked-lists | solution.py | yes | Hash Table, Linked List | Two Pointers | Hashing | canonical folder |
| 162 | 0162 | Find Peak Element | 0162-find-peak-element | solution.py | yes | Array | Binary Search | - | canonical folder |
| 167 | 0167 | Two Sum II - Input Array Is Sorted | 0167-two-sum-ii---input-array-is-sorted | solution.py | yes | Array | Two Pointers | Binary Search | canonical folder |
| 169 | 0169 | Majority Element | 0169-majority-element | solution.py | yes | Array, Hash Table | Hashing | Divide and Conquer, Sorting, Counting | canonical folder |
| 172 | 0172 | Factorial Trailing Zeroes | 0172-factorial-trailing-zeroes | solution.py | yes | Math | Math | - | canonical folder |
| 175 | 0175 | Combine Two Tables | 0175-combine-two-tables | solution.sql | yes | Database | SQL Join | - | canonical folder |
| 176 | 0176 | Second Highest Salary | 0176-second-highest-salary | solution.sql | yes | Database | SQL Aggregation | - | canonical folder |
| 178 | 0178 | Rank Scores | 0178-rank-scores | solution.sql | yes | Database | SQL Window/Ranking | - | canonical folder |
| 184 | 0184 | Department Highest Salary | 0184-department-highest-salary | solution.sql | yes | Database | SQL Join | - | canonical folder |
| 185 | 0185 | Department Top Three Salaries | 0185-department-top-three-salaries | solution.sql | yes | Database | SQL Window/Ranking | - | canonical folder |
| 189 | 0189 | Rotate Array | 0189-rotate-array | solution.py | yes | Array, Math | Two Pointers | Math | canonical folder |
| 190 | 0190 | Reverse Bits | 0190-reverse-bits | solution.py | yes | Bit Manipulation | Bit Manipulation | Divide and Conquer | canonical folder |
| 191 | 0191 | Number of 1 Bits | 0191-number-of-1-bits | solution.py | yes | Bit Manipulation | Bit Manipulation | Divide and Conquer | canonical folder |
| 197 | 0197 | Rising Temperature | 0197-rising-temperature | solution.sql | yes | Database | SQL Self Join | - | canonical folder |
| 198 | 0198 | House Robber | 0198-house-robber | solution.py | yes | Array | 1D Dynamic Programming | Dynamic Programming | canonical folder |
| 199 | 0199 | Binary Tree Right Side View | 0199-binary-tree-right-side-view | solution.py | yes | Binary Tree | BFS | DFS | canonical folder |
| 200 | 0200 | Number of Islands | 0200-number-of-islands | solution.py | yes | Array, Matrix | DFS | BFS, Matrix Traversal | canonical folder |
| 201 | 0201 | Bitwise AND of Numbers Range | 0201-bitwise-and-of-numbers-range | solution.py | yes | Bit Manipulation | Bit Manipulation | - | canonical folder |
| 202 | 0202 | Happy Number | 0202-happy-number | solution.py | yes | Hash Table, Math | Fast & Slow Pointers | Hashing, Math, Two Pointers | canonical folder |
| 203 | 0203 | Remove Linked List Elements | 0203-remove-linked-list-elements | solution.py | yes | Linked List | Linked List Traversal | - | canonical folder |
| 205 | 0205 | Isomorphic Strings | 0205-isomorphic-strings | solution.py | yes | Hash Table, String | Hashing | - | canonical folder |
| 206 | 0206 | Reverse Linked List | 0206-reverse-linked-list | solution.py | yes | Linked List | Linked List Reversal | - | canonical folder |
| 207 | 0207 | Course Schedule | 0207-course-schedule | solution.py | yes | Graph | Topological Sort | DFS, BFS, Graph Traversal | canonical folder |
| 208 | 0208 | Implement Trie (Prefix Tree) | 0208-implement-trie-prefix-tree | solution.py | yes | Hash Table, String, Design, Trie | Trie | Hashing, Design | legacy exact duplicate: 208. Implement Trie (Prefix Tree).py |
| 210 | 0210 | Course Schedule II | 0210-course-schedule-ii | solution.py | yes | Graph | Topological Sort | DFS, BFS, Graph Traversal | canonical folder |
| 211 | 0211 | Design Add and Search Words Data Structure | 0211-design-add-and-search-words-data-structure | solution.py | yes | String, Design, Trie | Trie | DFS, Design | canonical folder |
| 215 | 0215 | Kth Largest Element in an Array | 0215-kth-largest-element-in-an-array | solution.py | yes | Array, Heap | Heap / Priority Queue | Divide and Conquer, Sorting, Quickselect | canonical folder |
| 217 | 0217 | Contains Duplicate | 0217-contains-duplicate | solution.py | yes | Array, Hash Table | Hashing | Sorting | canonical folder |
| 219 | 0219 | Contains Duplicate II | 0219-contains-duplicate-ii | solution.py | yes | Array, Hash Table | Sliding Window | Hashing | canonical folder |
| 222 | 0222 | Count Complete Tree Nodes | 0222-count-complete-tree-nodes | solution.py | yes | Bit Manipulation, Binary Tree | Binary Search | Bit Manipulation | legacy exact duplicate: 222. Count Complete Tree Nodes.py |
| 225 | 0225 | Implement Stack using Queues | 0225-implement-stack-using-queues | solution.py | yes | Stack, Design, Queue | Queue | Stack, Design | canonical folder |
| 226 | 0226 | Invert Binary Tree | 0226-invert-binary-tree | solution.py | yes | Binary Tree | Tree Traversal | DFS, BFS | canonical folder |
| 228 | 0228 | Summary Ranges | 0228-summary-ranges | solution.py | yes | Array | Array Scanning | - | canonical folder |
| 230 | 0230 | Kth Smallest Element in a BST | 0230-kth-smallest-element-in-a-bst | solution.py | yes | BST, Binary Tree | Tree Traversal | DFS | canonical folder |
| 231 | 0231 | Power of Two | 0231-power-of-two | solution.py | yes | Math, Bit Manipulation | Bit Manipulation | Math | canonical folder |
| 232 | 0232 | Implement Queue using Stacks | 0232-implement-queue-using-stacks | solution.py | yes | Stack, Design, Queue | Stack | Design, Queue | canonical folder |
| 234 | 0234 | Palindrome Linked List | 0234-palindrome-linked-list | solution.py | yes | Linked List, Stack | Fast & Slow Pointers | Two Pointers, Stack | canonical folder |
| 235 | 0235 | Lowest Common Ancestor of a Binary Search Tree | 0235-lowest-common-ancestor-of-a-binary-search-tree | solution.py | yes | BST, Binary Tree | BST Search | DFS | canonical folder |
| 236 | 0236 | Lowest Common Ancestor of a Binary Tree | 0236-lowest-common-ancestor-of-a-binary-tree | solution.py | yes | Binary Tree | DFS | - | canonical folder |
| 237 | 0237 | Delete Node in a Linked List | 0237-delete-node-in-a-linked-list | solution.py | yes | Linked List | Linked List Traversal | - | canonical folder |
| 238 | 0238 | Product of Array Except Self | 0238-product-of-array-except-self | solution.py | yes | Array | Prefix/Suffix Precomputation | Prefix Sum | canonical folder |
| 242 | 0242 | Valid Anagram | 0242-valid-anagram | solution.py | yes | Hash Table, String | Hashing | Sorting | canonical folder |
| 257 | 0257 | Binary Tree Paths | 0257-binary-tree-paths | solution.py | yes | String, Binary Tree | Backtracking | DFS | canonical folder |
| 258 | 0258 | Add Digits | 0258-add-digits | solution.py | yes | Math | Simulation | Math | canonical folder |
| 268 | 0268 | Missing Number | 0268-missing-number | solution.py | yes | Array, Hash Table, Math, Bit Manipulation | Bit Manipulation | Hashing, Math, Binary Search, Sorting | canonical folder |
| 283 | 0283 | Move Zeroes | 0283-move-zeroes | solution.py | yes | Array | Two Pointers | - | canonical folder |
| 287 | 0287 | Find the Duplicate Number | 0287-find-the-duplicate-number | solution.py | yes | Array, Bit Manipulation | Hashing | Two Pointers, Binary Search, Bit Manipulation | canonical folder |
| 290 | 0290 | Word Pattern | 0290-word-pattern | solution.py | yes | Hash Table, String | Hashing | - | canonical folder |
| 316 | 0316 | Remove Duplicate Letters | 0316-remove-duplicate-letters | solution.py | yes | String, Stack | Monotonic Stack | Stack, Greedy | canonical folder |
| 326 | 0326 | Power of Three | 0326-power-of-three | solution.py | yes | Math | Math | - | canonical folder |
| 328 | 0328 | Odd Even Linked List | 0328-odd-even-linked-list | solution.py | yes | Linked List | Linked List Traversal | - | legacy exact duplicate: 328. Odd Even Linked List.py |
| 334 | 0334 | Increasing Triplet Subsequence | 0334-increasing-triplet-subsequence | solution.py | yes | Array | Greedy | - | canonical folder |
| 338 | 0338 | Counting Bits | 0338-counting-bits | solution.py | yes | Bit Manipulation | Bit Manipulation | Dynamic Programming | canonical folder |
| 342 | 0342 | Power of Four | 0342-power-of-four | solution.py | yes | Math, Bit Manipulation | Bit Manipulation | Math | canonical folder |
| 343 | 0343 | Integer Break | 0343-integer-break | solution.py | yes | Math | Math | Dynamic Programming | canonical folder |
| 344 | 0344 | Reverse String | 0344-reverse-string | solution.py | yes | String | Two Pointers | - | canonical folder |
| 345 | 0345 | Reverse Vowels of a String | 0345-reverse-vowels-of-a-string | solution.py | yes | String | Two Pointers | - | canonical folder |
| 347 | 0347 | Top K Frequent Elements | 0347-top-k-frequent-elements | solution.py | yes | Array, Hash Table, Heap | Heap / Priority Queue | Hashing, Divide and Conquer, Sorting, Counting, Quickselect | canonical folder |
| 349 | 0349 | Intersection of Two Arrays | 0349-intersection-of-two-arrays | solution.py | yes | Array, Hash Table | Hashing | Two Pointers, Binary Search, Sorting | canonical folder |
| 350 | 0350 | Intersection of Two Arrays II | 0350-intersection-of-two-arrays-ii | solution.py | yes | Array, Hash Table | Hashing | Two Pointers, Binary Search, Sorting | canonical folder |
| 374 | 0374 | Guess Number Higher or Lower | 0374-guess-number-higher-or-lower | solution.py | yes | NEEDS_REVIEW | Binary Search | - | canonical folder |
| 382 | 0382 | Linked List Random Node | 0382-linked-list-random-node | solution.py | yes | Linked List, Math | Math | Reservoir Sampling, Randomized | canonical folder |
| 383 | 0383 | Ransom Note | 0383-ransom-note | solution.py | yes | Hash Table, String | Hashing | Counting | canonical folder |
| 387 | 0387 | First Unique Character in a String | 0387-first-unique-character-in-a-string | solution.py | yes | Hash Table, String, Queue | Counting | Hashing, Queue | canonical folder |
| 389 | 0389 | Find the Difference | 0389-find-the-difference | solution.py | yes | Hash Table, String, Bit Manipulation | Bit Manipulation | Hashing, Sorting | canonical folder |
| 392 | 0392 | Is Subsequence | 0392-is-subsequence | solution.py | yes | String | Two Pointers | Dynamic Programming | canonical folder |
| 394 | 0394 | Decode String | 0394-decode-string | solution.py | yes | String, Stack | Stack | - | canonical folder |
| 399 | 0399 | Evaluate Division | 0399-evaluate-division | solution.py | yes | Array, String, Graph | DFS | BFS, Graph Traversal | canonical folder |
| 404 | 0404 | Sum of Left Leaves | 0404-sum-of-left-leaves | solution.py | yes | Binary Tree | DFS | BFS | canonical folder |
| 407 | 0407 | Trapping Rain Water II | 0407-trapping-rain-water-ii | solution.py | yes | Array, Heap, Matrix | BFS | Heap / Priority Queue, Matrix Traversal | canonical folder |
| 412 | 0412 | Fizz Buzz | 0412-fizz-buzz | solution.py | yes | Math, String | Simulation | Math | canonical folder |
| 415 | 0415 | Add Strings | 0415-add-strings | solution.py | yes | Math, String | Simulation | Math | canonical folder |
| 419 | 0419 | Battleships in a Board | 0419-battleships-in-a-board | solution.py | yes | Array, Matrix | Matrix Traversal | DFS | canonical folder |
| 437 | 0437 | Path Sum III | 0437-path-sum-iii | solution.py | yes | Binary Tree | Prefix Sum | DFS | canonical folder |
| 442 | 0442 | Find All Duplicates in an Array | 0442-find-all-duplicates-in-an-array | solution.py | yes | Array, Hash Table | Index Placement | Hashing, Sorting | canonical folder |
| 443 | 0443 | String Compression | 0443-string-compression | solution.py | yes | String | Two Pointers | - | canonical folder |
| 448 | 0448 | Find All Numbers Disappeared in an Array | 0448-find-all-numbers-disappeared-in-an-array | solution.py | yes | Array, Hash Table | Hashing | - | legacy exact duplicate: 448. Find All Numbers Disappeared in an Array.py |
| 450 | 0450 | Delete Node in a BST | 0450-delete-node-in-a-bst | solution.py | yes | BST, Binary Tree | NEEDS_REVIEW | - | canonical folder |
| 455 | 0455 | Assign Cookies | 0455-assign-cookies | solution.py | yes | Array | Two Pointers | Greedy, Sorting | canonical folder |
| 463 | 0463 | Island Perimeter | 0463-island-perimeter | solution.py | yes | Array, Matrix | Matrix Traversal | DFS, BFS | canonical folder |
| 500 | 0500 | Keyboard Row | 0500-keyboard-row | solution.py | yes | Array, Hash Table, String | Hashing | - | canonical folder |
| 501 | 0501 | Find Mode in Binary Search Tree | 0501-find-mode-in-binary-search-tree | solution.py | yes | BST, Binary Tree | DFS | - | canonical folder |
| 506 | 0506 | Relative Ranks | 0506-relative-ranks | solution.py | yes | Array, Heap | Sorting | Heap / Priority Queue | canonical folder |
| 509 | 1013 | Fibonacci Number | 1013-fibonacci-number | solution.py | yes | Math | 1D Dynamic Programming | Math, Dynamic Programming | canonical folder |
| 513 | 0513 | Find Bottom Left Tree Value | 0513-find-bottom-left-tree-value | solution.py | yes | Binary Tree | BFS | DFS | canonical folder |
| 515 | 0515 | Find Largest Value in Each Tree Row | 0515-find-largest-value-in-each-tree-row | solution.py | yes | Binary Tree | BFS | DFS | canonical folder |
| 530 | 0530 | Minimum Absolute Difference in BST | 0530-minimum-absolute-difference-in-bst | solution.py | yes | BST, Binary Tree | BFS | DFS | canonical folder |
| 541 | 0541 | Reverse String II | 0541-reverse-string-ii | solution.py | yes | String | String Scanning | Two Pointers | canonical folder |
| 543 | 0543 | Diameter of Binary Tree | 0543-diameter-of-binary-tree | solution.py | yes | Binary Tree | Tree Postorder / Return Information | DFS | legacy exact duplicate: 543.Diameter of Binary Tree.py |
| 547 | 0547 | Number of Provinces | 0547-number-of-provinces | solution.py | yes | Graph | DFS | BFS, Graph Traversal | canonical folder |
| 557 | 0557 | Reverse Words in a String III | 0557-reverse-words-in-a-string-iii | solution.py | yes | String | String Scanning | Two Pointers | canonical folder |
| 559 | 0774 | Maximum Depth of N-ary Tree | 0774-maximum-depth-of-n-ary-tree | solution.py | yes | Tree | BFS | DFS | canonical folder |
| 563 | 0563 | Binary Tree Tilt | 0563-binary-tree-tilt | solution.py | yes | Binary Tree | Tree Postorder / Return Information | DFS | canonical folder |
| 572 | 0572 | Subtree of Another Tree | 0572-subtree-of-another-tree | solution.py | yes | Binary Tree | DFS | String Matching | canonical folder |
| 584 | 0584 | Find Customer Referee | 0584-find-customer-referee | solution.sql | yes | Database | SQL Filtering | - | canonical folder |
| 589 | 0775 | N-ary Tree Preorder Traversal | 0775-n-ary-tree-preorder-traversal | solution.py | yes | Stack, Tree | Tree Traversal | Stack, DFS | canonical folder |
| 590 | 0776 | N-ary Tree Postorder Traversal | 0776-n-ary-tree-postorder-traversal | solution.py | yes | Stack, Tree | Tree Traversal | Stack, DFS | canonical folder |
| 595 | 0595 | Big Countries | 0595-big-countries | solution.py, solution.sql | yes | Database | SQL Filtering | - | canonical folder |
| 605 | 0605 | Can Place Flowers | 0605-can-place-flowers | solution.py | yes | Array | Greedy | - | legacy exact duplicate: 605.Can Place Flowers.py |
| 606 | 0606 | Construct String from Binary Tree | 0606-construct-string-from-binary-tree | solution.py | yes | String, Binary Tree | DFS | - | canonical folder |
| 617 | 0617 | Merge Two Binary Trees | 0617-merge-two-binary-trees | solution.py | yes | Binary Tree | BFS | DFS | canonical folder |
| 633 | 0633 | Sum of Square Numbers | 0633-sum-of-square-numbers | solution.py | yes | Math | Two Pointers | Math, Binary Search | canonical folder |
| 637 | 0637 | Average of Levels in Binary Tree | 0637-average-of-levels-in-binary-tree | solution.py | yes | Binary Tree | BFS | DFS | canonical folder |
| 643 | 0643 | Maximum Average Subarray I | 0643-maximum-average-subarray-i | solution.py | yes | Array | Sliding Window | - | canonical folder |
| 649 | 0649 | Dota2 Senate | 0649-dota2-senate | solution.py | yes | String, Queue | Queue | Greedy | canonical folder |
| 653 | 0653 | Two Sum IV - Input is a BST | 0653-two-sum-iv---input-is-a-bst | solution.py | yes | Hash Table, BST, Binary Tree | BFS | Hashing, Two Pointers, DFS | canonical folder |
| 658 | 0658 | Find K Closest Elements | 0658-find-k-closest-elements | solution.py | yes | Array, Heap | Binary Search | Two Pointers, Sliding Window, Sorting, Heap / Priority Queue | canonical folder |
| 662 | 0662 | Maximum Width of Binary Tree | 0662-maximum-width-of-binary-tree | solution.py | yes | Binary Tree | BFS | DFS | canonical folder |
| 671 | 0671 | Second Minimum Node In a Binary Tree | 0671-second-minimum-node-in-a-binary-tree | solution.py | yes | Binary Tree | DFS | - | canonical folder |
| 680 | 0680 | Valid Palindrome II | 0680-valid-palindrome-ii | solution.py | yes | String | Greedy | Two Pointers | canonical folder |
| 684 | 0684 | Redundant Connection | 0684-redundant-connection | solution.py | yes | Graph | Union Find | DFS, BFS, Graph Traversal | canonical folder |
| 696 | 0696 | Count Binary Substrings | 0696-count-binary-substrings | solution.py | yes | String | String Scanning | Two Pointers | canonical folder |
| 700 | 0783 | Search in a Binary Search Tree | 0783-search-in-a-binary-search-tree | solution.py | yes | BST, Binary Tree | BST Search | - | canonical folder |
| 704 | 0792 | Binary Search | 0792-binary-search | solution.py | yes | Array | Binary Search | - | canonical folder |
| 709 | 0742 | To Lower Case | 0742-to-lower-case | solution.py | yes | String | String Scanning | - | canonical folder |
| 724 | 0724 | Find Pivot Index | 0724-find-pivot-index | solution.py | yes | Array | Prefix Sum | - | legacy exact duplicate: 724.Find Pivot Index.py |
| 733 | 0733 | Flood Fill | 0733-flood-fill | solution.py | yes | Array, Matrix | DFS | BFS, Matrix Traversal | canonical folder |
| 735 | 0735 | Asteroid Collision | 0735-asteroid-collision | solution.py | yes | Array, Stack | Stack | Simulation | canonical folder |
| 739 | 0739 | Daily Temperatures | 0739-daily-temperatures | solution.py | yes | Array, Stack | Monotonic Stack | Stack | canonical folder |
| 744 | 0745 | Find Smallest Letter Greater Than Target | 0745-find-smallest-letter-greater-than-target | solution.py | yes | Array | Two Pointers | Binary Search | legacy exact duplicate: 744.Find Smallest Letter Greater Than Target.py |
| 746 | 0747 | Min Cost Climbing Stairs | 0747-min-cost-climbing-stairs | solution.py | yes | Array | 1D Dynamic Programming | Dynamic Programming | canonical folder |
| 752 | 0753 | Open the Lock | 0753-open-the-lock | solution.py | yes | Array, Hash Table, String | BFS | Hashing | canonical folder |
| 761 | 0763 | Special Binary String | 0763-special-binary-string | solution.py | yes | String | Sorting | Divide and Conquer | canonical folder |
| 771 | 0782 | Jewels and Stones | 0782-jewels-and-stones | solution.py | yes | Hash Table, String | Hashing | - | canonical folder |
| 783 | 0799 | Minimum Distance Between BST Nodes | 0799-minimum-distance-between-bst-nodes | solution.py | yes | BST, Binary Tree | Tree Traversal | DFS, BFS | canonical folder |
| 802 | 0820 | Find Eventual Safe States | 0820-find-eventual-safe-states | solution.py | yes | Graph | BFS | DFS, Graph Traversal, Topological Sort | canonical folder |
| 804 | 0822 | Unique Morse Code Words | 0822-unique-morse-code-words | solution.py | yes | Array, Hash Table, String | Hashing | - | canonical folder |
| 819 | 0837 | Most Common Word | 0837-most-common-word | solution.py | yes | Array, Hash Table, String | Hashing | Counting | canonical folder |
| 821 | 0841 | Shortest Distance to a Character | 0841-shortest-distance-to-a-character | solution.py | yes | Array, String | Two Pointers | - | canonical folder |
| 824 | 0851 | Goat Latin | 0851-goat-latin | solution.py | yes | String | Simulation | - | canonical folder |
| 832 | 0861 | Flipping an Image | 0861-flipping-an-image | solution.py | yes | Array, Bit Manipulation, Matrix | Two Pointers | Bit Manipulation, Matrix Traversal, Simulation | canonical folder |
| 841 | 0871 | Keys and Rooms | 0871-keys-and-rooms | solution.py | yes | Graph | DFS | BFS, Graph Traversal | canonical folder |
| 853 | 0883 | Car Fleet | 0883-car-fleet | solution.py | yes | Array, Stack | Monotonic Stack | Stack, Sorting | canonical folder |
| 872 | 0904 | Leaf-Similar Trees | 0904-leaf-similar-trees | solution.py | yes | Binary Tree | DFS | - | legacy exact duplicate: 872. Leaf-Similar Trees.py |
| 875 | 0907 | Koko Eating Bananas | 0907-koko-eating-bananas | solution.py | yes | Array | Binary Search | - | canonical folder |
| 876 | 0908 | Middle of the Linked List | 0908-middle-of-the-linked-list | solution.py | yes | Linked List | Fast & Slow Pointers | Two Pointers | canonical folder |
| 880 | 0916 | Decoded String at Index | 0916-decoded-string-at-index | solution.py | yes | String, Stack | Stack | - | canonical folder |
| 881 | 0917 | Boats to Save People | 0917-boats-to-save-people | solution.py | yes | Array | Two Pointers | Greedy, Sorting | canonical folder |
| 897 | 0933 | Increasing Order Search Tree | 0933-increasing-order-search-tree | solution.py | yes | Stack, BST, Binary Tree | Tree Traversal | Stack, DFS | canonical folder |
| 901 | 0937 | Online Stock Span | 0937-online-stock-span | solution.py | yes | Stack, Design | Monotonic Stack | Stack, Design, Data Stream | legacy exact duplicate: 901. Online Stock Span.py |
| 905 | 0941 | Sort Array By Parity | 0941-sort-array-by-parity | solution.py | yes | Array | Two Pointers | Sorting | canonical folder |
| 917 | 0953 | Reverse Only Letters | 0953-reverse-only-letters | solution.py | yes | String | Two Pointers | - | canonical folder |
| 922 | 0958 | Sort Array By Parity II | 0958-sort-array-by-parity-ii | solution.py | yes | Array | Two Pointers | Sorting | canonical folder |
| 923 | 0959 | 3Sum With Multiplicity | 0959-3sum-with-multiplicity | solution.py | yes | Array, Hash Table | Two Pointers | Hashing, Sorting, Counting | canonical folder |
| 933 | 0969 | Number of Recent Calls | 0969-number-of-recent-calls | solution.py | yes | Design, Queue | Queue | Design, Data Stream | canonical folder |
| 938 | 0975 | Range Sum of BST | 0975-range-sum-of-bst | solution.py | yes | BST, Binary Tree | DFS | - | canonical folder |
| 942 | 0979 | DI String Match | 0979-di-string-match | solution.py | yes | Array, String | Two Pointers | Greedy | canonical folder |
| 948 | 0985 | Bag of Tokens | 0985-bag-of-tokens | solution.py | yes | Array | Two Pointers | Greedy, Sorting | canonical folder |
| 956 | 0993 | Tallest Billboard | 0993-tallest-billboard | solution.py | yes | Array | Knapsack / Take-Skip | Dynamic Programming | canonical folder |
| 965 | 1005 | Univalued Binary Tree | 1005-univalued-binary-tree | solution.py | yes | Binary Tree | Tree Traversal | DFS, BFS | canonical folder |
| 969 | 1009 | Pancake Sorting | 1009-pancake-sorting | solution.py | yes | Array | Two Pointers | Greedy, Sorting | canonical folder |
| 977 | 1019 | Squares of a Sorted Array | 1019-squares-of-a-sorted-array | solution.py | yes | Array | Two Pointers | Sorting | legacy alternate approach: 977. Squares of a Sorted Array.py |
| 981 | 1023 | Time Based Key-Value Store | 1023-time-based-key-value-store | solution.py | yes | Hash Table, String, Design | Design | Hashing, Binary Search | canonical folder |
| 993 | 1035 | Cousins in Binary Tree | 1035-cousins-in-binary-tree | solution.py | yes | Binary Tree | BFS | DFS | canonical folder |
| 1004 | 1046 | Max Consecutive Ones III | 1046-max-consecutive-ones-iii | solution.py | yes | Array | Sliding Window | Binary Search, Prefix Sum | legacy exact duplicate: 1004. Max Consecutive Ones III.py |
| 1022 | 1079 | Sum of Root To Leaf Binary Numbers | 1079-sum-of-root-to-leaf-binary-numbers | solution.py | yes | Binary Tree | DFS | - | canonical folder |
| 1025 | 1086 | Divisor Game | 1086-divisor-game | solution.py | yes | Math | 1D Dynamic Programming | Math, Dynamic Programming | canonical folder |
| 1051 | 1137 | Height Checker | 1137-height-checker | solution.py | yes | Array | Sorting | - | canonical folder |
| 1071 | 1146 | Greatest Common Divisor of Strings | 1146-greatest-common-divisor-of-strings | solution.py | yes | Math, String | Math | - | legacy exact duplicate: 1071.Greatest Common Divisor of Strings.py |
| 1081 | 1159 | Smallest Subsequence of Distinct Characters | 1159-smallest-subsequence-of-distinct-characters | solution.py | yes | String, Stack | Monotonic Stack | Stack, Greedy | canonical folder |
| 1089 | 1168 | Duplicate Zeros | 1168-duplicate-zeros | solution.py | yes | Array | Two Pointers | - | canonical folder |
| 1108 | 1205 | Defanging an IP Address | 1205-defanging-an-ip-address | solution.py | yes | String | Simulation | - | canonical folder |
| 1137 | 1236 | N-th Tribonacci Number | 1236-n-th-tribonacci-number | solution.py | yes | Math | 1D Dynamic Programming | Math, Dynamic Programming | canonical folder |
| 1143 | 1250 | Longest Common Subsequence | 1250-longest-common-subsequence | solution.py | yes | String | String Dynamic Programming | Dynamic Programming | canonical folder |
| 1148 | 1258 | Article Views I | 1258-article-views-i | solution.sql | yes | Database | SQL Filtering | - | canonical folder |
| 1161 | 1116 | Maximum Level Sum of a Binary Tree | 1116-maximum-level-sum-of-a-binary-tree | solution.py | yes | Binary Tree | BFS | DFS | legacy exact duplicate: 1161. Maximum Level Sum of a Binary Tree.py |
| 1200 | 1306 | Minimum Absolute Difference | 1306-minimum-absolute-difference | solution.py | yes | Array | Sorting | - | canonical folder |
| 1207 | 1319 | Unique Number of Occurrences | 1319-unique-number-of-occurrences | solution.py | yes | Array, Hash Table | Hashing | - | canonical folder |
| 1267 | 1396 | Count Servers that Communicate | 1396-count-servers-that-communicate | solution.py | yes | Array, Matrix | Counting | DFS, BFS, Matrix Traversal | canonical folder |
| 1268 | 1397 | Search Suggestions System | 1397-search-suggestions-system | solution.py | yes | Array, String, Trie, Heap | Trie | Binary Search, Sorting, Heap / Priority Queue | legacy exact duplicate: 1268 Search Suggestions System.py |
| 1318 | 1441 | Minimum Flips to Make a OR b Equal to c | 1441-minimum-flips-to-make-a-or-b-equal-to-c | solution.py | yes | Bit Manipulation | Bit Manipulation | - | canonical folder |
| 1356 | 1458 | Sort Integers by The Number of 1 Bits | 1458-sort-integers-by-the-number-of-1-bits | solution.py | yes | Array, Bit Manipulation | Bit Manipulation | Sorting, Counting | canonical folder |
| 1372 | 1474 | Longest ZigZag Path in a Binary Tree | 1474-longest-zigzag-path-in-a-binary-tree | solution.py | yes | Binary Tree | Tree Postorder / Return Information | Dynamic Programming, DFS | canonical folder |
| 1379 | 1498 | Find a Corresponding Node of a Binary Tree in a Clone of That Tree | 1498-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree | solution.py | yes | Binary Tree | DFS | BFS | canonical folder |
| 1431 | 1528 | Kids With the Greatest Number of Candies | 1528-kids-with-the-greatest-number-of-candies | solution.py | yes | Array | Array Scanning | - | legacy exact duplicate: 1431.  Kids With the Greatest Number of Candies.py |
| 1448 | 1544 | Count Good Nodes in Binary Tree | 1544-count-good-nodes-in-binary-tree | solution.py | yes | Binary Tree | BFS | DFS | canonical folder |
| 1456 | 1567 | Maximum Number of Vowels in a Substring of Given Length | 1567-maximum-number-of-vowels-in-a-substring-of-given-length | solution.py | yes | String | Sliding Window | - | legacy exact duplicate: 1456. Maximum Number of Vowels in a Subs.py |
| 1462 | 1558 | Course Schedule IV | 1558-course-schedule-iv | solution.py | yes | Graph | DFS | BFS, Graph Traversal, Topological Sort | canonical folder |
| 1466 | 1576 | Reorder Routes to Make All Paths Lead to the City Zero | 1576-reorder-routes-to-make-all-paths-lead-to-the-city-zero | solution.py | yes | Graph | DFS | BFS, Graph Traversal | canonical folder |
| 1493 | 1586 | Longest Subarray of 1's After Deleting One Element | 1586-longest-subarray-of-1s-after-deleting-one-element | solution.py | yes | Array | 1D Dynamic Programming | Dynamic Programming, Sliding Window | canonical folder |
| 1498 | 1621 | Number of Subsequences That Satisfy the Given Sum Condition | 1621-number-of-subsequences-that-satisfy-the-given-sum-condition | solution.py | yes | Array | Two Pointers | Binary Search, Sorting | canonical folder |
| 1535 | 1657 | Find the Winner of an Array Game | 1657-find-the-winner-of-an-array-game | solution.py | yes | Array | Simulation | - | canonical folder |
| 1574 | 1679 | Shortest Subarray to be Removed to Make Array Sorted | 1679-shortest-subarray-to-be-removed-to-make-array-sorted | solution.py | yes | Array, Stack | Two Pointers | Binary Search, Stack, Monotonic Stack | canonical folder |
| 1581 | 1724 | Customer Who Visited but Did Not Make Any Transactions | 1724-customer-who-visited-but-did-not-make-any-transactions | solution.sql | yes | Database | SQL Join | - | canonical folder |
| 1657 | 1777 | Determine if Two Strings Are Close | 1777-determine-if-two-strings-are-close | solution.py | yes | Hash Table, String | Counting | Hashing, Sorting | canonical folder |
| 1662 | 1781 | Check If Two String Arrays are Equivalent | 1781-check-if-two-string-arrays-are-equivalent | solution.py | yes | Array, String | Simulation | - | canonical folder |
| 1678 | 1797 | Goal Parser Interpretation | 1797-goal-parser-interpretation | solution.py | yes | String | Simulation | - | canonical folder |
| 1679 | 1798 | Max Number of K-Sum Pairs | 1798-max-number-of-k-sum-pairs | solution.py | yes | Array, Hash Table | Two Pointers | Hashing, Sorting, Complement Lookup | canonical folder |
| 1683 | 1827 | Invalid Tweets | 1827-invalid-tweets | solution.sql | yes | Database | SQL Filtering | - | canonical folder |
| 1721 | 0528 | Swapping Nodes in a Linked List | 0528-swapping-nodes-in-a-linked-list | solution.py | yes | Linked List | Fast & Slow Pointers | Two Pointers | canonical folder |
| 1732 | 1833 | Find the Highest Altitude | 1833-find-the-highest-altitude | solution.py | yes | Array | Array Scanning | Prefix Sum | canonical folder |
| 1750 | 1850 | Minimum Length of String After Deleting Similar Ends | 1850-minimum-length-of-string-after-deleting-similar-ends | solution.py | yes | String | Two Pointers | - | canonical folder |
| 1757 | 1908 | Recyclable and Low Fat Products | 1908-recyclable-and-low-fat-products | solution.py, solution.sql | yes | Database | SQL Filtering | - | canonical folder |
| 1765 | 1876 | Map of Highest Peak | 1876-map-of-highest-peak | solution.py | yes | Array, Matrix | BFS | Matrix Traversal | canonical folder |
| 1768 | 1894 | Merge Strings Alternately | 1894-merge-strings-alternately | solution.py | yes | String | Two Pointers | - | canonical folder |
| 1813 | 1923 | Sentence Similarity III | 1923-sentence-similarity-iii | solution.py | yes | Array, String | Two Pointers | - | canonical folder |
| 1844 | 1954 | Replace All Digits with Characters | 1954-replace-all-digits-with-characters | solution.py | yes | String | Simulation | - | canonical folder |
| 1848 | 1975 | Minimum Distance to the Target Element | 1975-minimum-distance-to-the-target-element | solution.py | yes | Array | Array Scanning | - | canonical folder |
| 1854 | 1983 | Maximum Population Year | 1983-maximum-population-year | solution.py | yes | Array | Prefix Sum | Counting | canonical folder |
| 1859 | 1970 | Sorting the Sentence | 1970-sorting-the-sentence | solution.py | yes | String | Sorting | - | canonical folder |
| 1877 | 1988 | Minimize Maximum Pair Sum in Array | 1988-minimize-maximum-pair-sum-in-array | solution.py | yes | Array | Two Pointers | Greedy, Sorting | canonical folder |
| 1903 | 2032 | Largest Odd Number in String | 2032-largest-odd-number-in-string | solution.py | yes | Math, String | String Scanning | Math, Greedy | canonical folder |
| 1921 | 2049 | Eliminate Maximum Number of Monsters | 2049-eliminate-maximum-number-of-monsters | solution.py | yes | Array | Greedy | Sorting | canonical folder |
| 1929 | 2058 | Concatenation of Array | 2058-concatenation-of-array | solution.py | yes | Array | Simulation | - | canonical folder |
| 1971 | 2121 | Find if Path Exists in Graph | 2121-find-if-path-exists-in-graph | solution.py | yes | Graph | DFS | BFS, Graph Traversal | canonical folder |
| 1992 | 2103 | Find All Groups of Farmland | 2103-find-all-groups-of-farmland | solution.py | yes | Array, Matrix | DFS | BFS, Matrix Traversal | canonical folder |
| 1993 | 2104 | Operations on Tree | 2104-operations-on-tree | solution.py | yes | Array, Hash Table, Tree, Design | Design | Hashing, DFS, BFS | canonical folder |
| 2000 | 2128 | Reverse Prefix of Word | 2128-reverse-prefix-of-word | solution.py | yes | String, Stack | Stack | Two Pointers | canonical folder |
| 2011 | 2137 | Final Value of Variable After Performing Operations | 2137-final-value-of-variable-after-performing-operations | solution.py | yes | Array, String | Simulation | - | canonical folder |
| 2017 | 2145 | Grid Game | 2145-grid-game | solution.py | yes | Array, Matrix | Grid Dynamic Programming | Matrix Traversal, Prefix Sum | canonical folder |
| 2049 | 2175 | Count Nodes With the Highest Score | 2175-count-nodes-with-the-highest-score | solution.py | yes | Array, Binary Tree | Tree Postorder / Return Information | DFS | canonical folder |
| 2095 | 2216 | Delete the Middle Node of a Linked List | 2216-delete-the-middle-node-of-a-linked-list | solution.py | yes | Linked List | Fast & Slow Pointers | Two Pointers | legacy exact duplicate: 2095. Delete the Middle Node of a Linked.py |
| 2101 | 2206 | Detonate the Maximum Bombs | 2206-detonate-the-maximum-bombs | solution.py | yes | Array, Math, Graph | DFS | Math, BFS, Graph Traversal, Geometry | canonical folder |
| 2127 | 2246 | Maximum Employees to Be Invited to a Meeting | 2246-maximum-employees-to-be-invited-to-a-meeting | solution.py | yes | Array, Graph | Topological Sort | Dynamic Programming, DFS, Graph Traversal | canonical folder |
| 2130 | 2236 | Maximum Twin Sum of a Linked List | 2236-maximum-twin-sum-of-a-linked-list | solution.py | yes | Linked List, Stack | Fast & Slow Pointers | Two Pointers, Stack | canonical folder |
| 2160 | 2264 | Minimum Sum of Four Digit Number After Splitting Digits | 2264-minimum-sum-of-four-digit-number-after-splitting-digits | solution.py | yes | Math | Greedy | Math, Sorting | canonical folder |
| 2164 | 2283 | Sort Even and Odd Indices Independently | 2283-sort-even-and-odd-indices-independently | solution.py | yes | Array | Sorting | - | canonical folder |
| 2215 | 1392 | Find the Difference of Two Arrays | 1392-find-the-difference-of-two-arrays | solution.py | yes | Array, Hash Table | Hashing | - | canonical folder |
| 2235 | 2383 | Add Two Integers | 2383-add-two-integers | solution.py | yes | Math | Math | - | canonical folder |
| 2265 | 2347 | Count Nodes Equal to Average of Subtree | 2347-count-nodes-equal-to-average-of-subtree | solution.py | yes | Binary Tree | Tree Postorder / Return Information | DFS | canonical folder |
| 2285 | 2379 | Maximum Total Importance of Roads | 2379-maximum-total-importance-of-roads | solution.py | yes | Graph, Heap | Greedy | Graph Traversal, Sorting, Heap / Priority Queue | canonical folder |
| 2315 | 2401 | Count Asterisks | 2401-count-asterisks | solution.py | yes | String | String Scanning | - | canonical folder |
| 2331 | 2416 | Evaluate Boolean Binary Tree | 2416-evaluate-boolean-binary-tree | solution.py | yes | Binary Tree | Tree Postorder / Return Information | DFS | canonical folder |
| 2336 | 2413 | Smallest Number in Infinite Set | 2413-smallest-number-in-infinite-set | solution.py | yes | Hash Table, Design, Heap | Heap / Priority Queue | Hashing, Design | canonical folder |
| 2352 | 2428 | Equal Row and Column Pairs | 2428-equal-row-and-column-pairs | solution.py | yes | Array, Hash Table, Matrix | Hashing | Matrix Traversal, Simulation | canonical folder |
| 2390 | 2470 | Removing Stars From a String | 2470-removing-stars-from-a-string | solution.py | yes | String, Stack | Stack | Simulation | canonical folder |
| 2493 | 2583 | Divide Nodes Into the Maximum Number of Groups | 2583-divide-nodes-into-the-maximum-number-of-groups | solution.py | yes | Graph | BFS | DFS, Graph Traversal | canonical folder |
| 2658 | 2764 | Maximum Number of Fish in a Grid | 2764-maximum-number-of-fish-in-a-grid | solution.py | yes | Array, Matrix | DFS | BFS, Matrix Traversal | canonical folder |
| 2661 | 2685 | First Completely Painted Row or Column | 2685-first-completely-painted-row-or-column | solution.py | yes | Array, Hash Table, Matrix | Hashing | Matrix Traversal | canonical folder |
| 2824 | 2917 | Count Pairs Whose Sum is Less than Target | 2917-count-pairs-whose-sum-is-less-than-target | solution.py | yes | Array | Two Pointers | Binary Search, Sorting | canonical folder |
| 2923 | 3188 | Find Champion I | 3188-find-champion-i | solution.py | yes | Array, Matrix | Matrix Traversal | - | canonical folder |
| 2948 | 3219 | Make Lexicographically Smallest Array by Swapping Elements | 3219-make-lexicographically-smallest-array-by-swapping-elements | solution.py | yes | Array | Sorting | - | canonical folder |
| 3151 | 3429 | Special Array I | 3429-special-array-i | solution.py | yes | Array | Array Scanning | - | canonical folder |
| 3330 | 3617 | Find the Original Typed String I | 3617-find-the-original-typed-string-i | solution.py | yes | String | String Scanning | - | canonical folder |
| 3331 | 3576 | Find Subtree Sizes After Changes | 3576-find-subtree-sizes-after-changes | solution.py | yes | Array, Hash Table, String, Tree | Tree Postorder / Return Information | Hashing, DFS | canonical folder |
| 3334 | 3593 | Find the Maximum Factor Score of Array | 3593-find-the-maximum-factor-score-of-array | solution.py | yes | Array, Math | Prefix/Suffix Precomputation | Math | canonical folder |
| 3354 | 3616 | Make Array Elements Equal to Zero | 3616-make-array-elements-equal-to-zero | solution.py | yes | Array | Simulation | Prefix Sum | canonical folder |

## Dashboard-Only Embedded Solved Records

These solved records have accepted code embedded in `dashboard/problems.json` but no physical problem directory. Decide whether to extract them into canonical folders, keep them dashboard-only, or regenerate the dashboard from `REVISION.md`.

| LC | Title | Current location | Topic(s) | Primary pattern | Secondary patterns | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 34 | Find First and Last Position of Element in Sorted Array | dashboard/problems.json (embedded leetcode_solution) | Array | Binary Search | - | dashboard-only; no problem folder |
| 40 | Combination Sum II | dashboard/problems.json (embedded leetcode_solution) | Array | Backtracking | - | dashboard-only; no problem folder |
| 41 | First Missing Positive | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | Index Placement | Hashing | dashboard-only; no problem folder |
| 56 | Merge Intervals | dashboard/problems.json (embedded leetcode_solution) | Array | Intervals | Sorting | dashboard-only; no problem folder |
| 72 | Edit Distance | dashboard/problems.json (embedded leetcode_solution) | String | String Dynamic Programming | Dynamic Programming | dashboard-only; no problem folder |
| 73 | Set Matrix Zeroes | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Matrix | Matrix Traversal | Hashing | dashboard-only; no problem folder |
| 76 | Minimum Window Substring | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Sliding Window | Hashing | dashboard-only; no problem folder |
| 84 | Largest Rectangle in Histogram | dashboard/problems.json (embedded leetcode_solution) | Array, Stack | Monotonic Stack | Stack | dashboard-only; no problem folder |
| 85 | Maximal Rectangle | dashboard/problems.json (embedded leetcode_solution) | Array, Stack, Matrix | Monotonic Stack | Dynamic Programming, Stack, Matrix Traversal | dashboard-only; no problem folder |
| 105 | Construct Binary Tree from Preorder and Inorder Traversal | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Binary Tree | Hashing | Divide and Conquer | dashboard-only; no problem folder |
| 124 | Binary Tree Maximum Path Sum | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | Tree Postorder / Return Information | Dynamic Programming, DFS | dashboard-only; no problem folder |
| 126 | Word Ladder II | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | BFS | Hashing, Backtracking | dashboard-only; no problem folder |
| 127 | Word Ladder | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | BFS | Hashing | dashboard-only; no problem folder |
| 148 | Sort List | dashboard/problems.json (embedded leetcode_solution) | Linked List | Two Pointers | Divide and Conquer, Sorting | dashboard-only; no problem folder |
| 149 | Max Points on a Line | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Math | Hashing | Math, Geometry | dashboard-only; no problem folder |
| 152 | Maximum Product Subarray | dashboard/problems.json (embedded leetcode_solution) | Array | 1D Dynamic Programming | Dynamic Programming | dashboard-only; no problem folder |
| 156 | Binary Tree Upside Down | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | DFS | - | dashboard-only; no problem folder |
| 179 | Largest Number | dashboard/problems.json (embedded leetcode_solution) | Array, String | Sorting | Greedy | dashboard-only; no problem folder |
| 181 | Employees Earning More Than Their Managers | dashboard/problems.json (embedded leetcode_solution) | Database | SQL Join | - | dashboard-only; no problem folder |
| 182 | Duplicate Emails | dashboard/problems.json (embedded leetcode_solution) | Database | SQL Aggregation | - | dashboard-only; no problem folder |
| 183 | Customers Who Never Order | dashboard/problems.json (embedded leetcode_solution) | Database | SQL Join | - | dashboard-only; no problem folder |
| 187 | Repeated DNA Sequences | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String, Bit Manipulation | Sliding Window | Hashing, Bit Manipulation | dashboard-only; no problem folder |
| 196 | Delete Duplicate Emails | dashboard/problems.json (embedded leetcode_solution) | Database | SQL Delete | - | dashboard-only; no problem folder |
| 213 | House Robber II | dashboard/problems.json (embedded leetcode_solution) | Array | 1D Dynamic Programming | Dynamic Programming | dashboard-only; no problem folder |
| 239 | Sliding Window Maximum | dashboard/problems.json (embedded leetcode_solution) | Array, Queue, Heap | Monotonic Queue | Queue, Sliding Window, Heap / Priority Queue | dashboard-only; no problem folder |
| 243 | Shortest Word Distance | dashboard/problems.json (embedded leetcode_solution) | Array, String | Two Pointers | - | dashboard-only; no problem folder |
| 244 | Shortest Word Distance II | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, String, Design | Design | Hashing, Two Pointers | dashboard-only; no problem folder |
| 245 | Shortest Word Distance III | dashboard/problems.json (embedded leetcode_solution) | Array, String | Two Pointers | - | dashboard-only; no problem folder |
| 254 | Factor Combinations | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | Backtracking | - | dashboard-only; no problem folder |
| 255 | Verify Preorder Sequence in Binary Search Tree | dashboard/problems.json (embedded leetcode_solution) | Array, Stack, BST, Binary Tree | Stack | Monotonic Stack | dashboard-only; no problem folder |
| 256 | Paint House | dashboard/problems.json (embedded leetcode_solution) | Array | 1D Dynamic Programming | Dynamic Programming | dashboard-only; no problem folder |
| 261 | Graph Valid Tree | dashboard/problems.json (embedded leetcode_solution) | Graph | Union Find | DFS, BFS, Graph Traversal | dashboard-only; no problem folder |
| 265 | Paint House II | dashboard/problems.json (embedded leetcode_solution) | Array | Dynamic Programming | - | dashboard-only; no problem folder |
| 269 | Alien Dictionary | dashboard/problems.json (embedded leetcode_solution) | Array, String, Graph | Topological Sort | DFS, BFS, Graph Traversal | dashboard-only; no problem folder |
| 270 | Closest Binary Search Tree Value | dashboard/problems.json (embedded leetcode_solution) | BST, Binary Tree | BST Search | Binary Search, DFS | dashboard-only; no problem folder |
| 271 | Encode and Decode Strings | dashboard/problems.json (embedded leetcode_solution) | Array, String, Design | Design | - | dashboard-only; no problem folder |
| 272 | Closest Binary Search Tree Value II | dashboard/problems.json (embedded leetcode_solution) | Stack, BST, Heap, Binary Tree | Tree Traversal | Two Pointers, Stack, DFS, Heap / Priority Queue | dashboard-only; no problem folder |
| 277 | Find the Celebrity | dashboard/problems.json (embedded leetcode_solution) | Graph | Two Pointers | Graph Traversal | dashboard-only; no problem folder |
| 278 | First Bad Version | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | Binary Search | - | dashboard-only; no problem folder |
| 285 | Inorder Successor in BST | dashboard/problems.json (embedded leetcode_solution) | BST, Binary Tree | BST Search | DFS | dashboard-only; no problem folder |
| 286 | Walls and Gates | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | BFS | Matrix Traversal | dashboard-only; no problem folder |
| 295 | Find Median from Data Stream | dashboard/problems.json (embedded leetcode_solution) | Design, Heap | Heap / Priority Queue | Two Pointers, Design, Sorting, Data Stream | dashboard-only; no problem folder |
| 297 | Serialize and Deserialize Binary Tree | dashboard/problems.json (embedded leetcode_solution) | String, Design, Binary Tree | Tree Traversal | DFS, BFS, Design | dashboard-only; no problem folder |
| 314 | Binary Tree Vertical Order Traversal | dashboard/problems.json (embedded leetcode_solution) | Hash Table, Binary Tree | BFS | Hashing, DFS, Sorting | dashboard-only; no problem folder |
| 319 | Bulb Switcher | dashboard/problems.json (embedded leetcode_solution) | Math | Math | - | dashboard-only; no problem folder |
| 322 | Coin Change | dashboard/problems.json (embedded leetcode_solution) | Array | 1D Dynamic Programming | Dynamic Programming, BFS | dashboard-only; no problem folder |
| 323 | Number of Connected Components in an Undirected Graph | dashboard/problems.json (embedded leetcode_solution) | Graph | Union Find | DFS, BFS, Graph Traversal | dashboard-only; no problem folder |
| 329 | Longest Increasing Path in a Matrix | dashboard/problems.json (embedded leetcode_solution) | Array, Graph, Matrix | DFS | Dynamic Programming, BFS, Graph Traversal, Topological Sort, Matrix Traversal | dashboard-only; no problem folder |
| 332 | Reconstruct Itinerary | dashboard/problems.json (embedded leetcode_solution) | Array, String, Graph, Heap | DFS | Graph Traversal, Sorting, Heap / Priority Queue | dashboard-only; no problem folder |
| 333 | Largest BST Subtree | dashboard/problems.json (embedded leetcode_solution) | BST, Binary Tree | Tree Postorder / Return Information | Dynamic Programming, DFS | dashboard-only; no problem folder |
| 339 | Nested List Weight Sum | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | BFS | DFS | dashboard-only; no problem folder |
| 341 | Flatten Nested List Iterator | dashboard/problems.json (embedded leetcode_solution) | Stack, Tree, Design, Queue | DFS | Stack, Design, Queue | dashboard-only; no problem folder |
| 353 | Design Snake Game | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Design, Queue | Design | Hashing, Queue, Simulation | dashboard-only; no problem folder |
| 360 | Sort Transformed Array | dashboard/problems.json (embedded leetcode_solution) | Array, Math | Two Pointers | Math, Sorting | dashboard-only; no problem folder |
| 364 | Nested List Weight Sum II | dashboard/problems.json (embedded leetcode_solution) | Stack | BFS | Stack, DFS | dashboard-only; no problem folder |
| 366 | Find Leaves of Binary Tree | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | Tree Postorder / Return Information | DFS | dashboard-only; no problem folder |
| 367 | Valid Perfect Square | dashboard/problems.json (embedded leetcode_solution) | Math | Binary Search | Math | dashboard-only; no problem folder |
| 373 | Find K Pairs with Smallest Sums | dashboard/problems.json (embedded leetcode_solution) | Array, Heap | Heap / Priority Queue | - | dashboard-only; no problem folder |
| 380 | Insert Delete GetRandom O(1) | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Math, Design | Hashing | Math, Design, Randomized | dashboard-only; no problem folder |
| 384 | Shuffle an Array | dashboard/problems.json (embedded leetcode_solution) | Array, Math, Design | Randomized | Math, Design | dashboard-only; no problem folder |
| 386 | Lexicographical Numbers | dashboard/problems.json (embedded leetcode_solution) | Trie | Trie | DFS | dashboard-only; no problem folder |
| 408 | Valid Word Abbreviation | dashboard/problems.json (embedded leetcode_solution) | String | Two Pointers | - | dashboard-only; no problem folder |
| 417 | Pacific Atlantic Water Flow | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | DFS | BFS, Matrix Traversal | dashboard-only; no problem folder |
| 424 | Longest Repeating Character Replacement | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Sliding Window | Hashing | dashboard-only; no problem folder |
| 426 | Convert Binary Search Tree to Sorted Doubly Linked List | dashboard/problems.json (embedded leetcode_solution) | Linked List, Stack, BST, Binary Tree | Tree Traversal | Stack, DFS | dashboard-only; no problem folder |
| 429 | N-ary Tree Level Order Traversal | dashboard/problems.json (embedded leetcode_solution) | Tree | BFS | - | dashboard-only; no problem folder |
| 432 | All O`one Data Structure | dashboard/problems.json (embedded leetcode_solution) | Hash Table, Linked List, Design | Hashing | Design | dashboard-only; no problem folder |
| 440 | K-th Smallest in Lexicographical Order | dashboard/problems.json (embedded leetcode_solution) | Trie | Trie | - | dashboard-only; no problem folder |
| 441 | Arranging Coins | dashboard/problems.json (embedded leetcode_solution) | Math | Binary Search | Math | dashboard-only; no problem folder |
| 464 | Can I Win | dashboard/problems.json (embedded leetcode_solution) | Math, Bit Manipulation | State Machine DP | Math, Dynamic Programming, Bit Manipulation | dashboard-only; no problem folder |
| 474 | Ones and Zeroes | dashboard/problems.json (embedded leetcode_solution) | Array, String | Dynamic Programming | - | dashboard-only; no problem folder |
| 485 | Max Consecutive Ones | dashboard/problems.json (embedded leetcode_solution) | Array | Array Scanning | - | dashboard-only; no problem folder |
| 489 | Robot Room Cleaner | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | Backtracking | - | dashboard-only; no problem folder |
| 511 | Game Play Analysis I | dashboard/problems.json (embedded leetcode_solution) | Database | SQL Aggregation | - | dashboard-only; no problem folder |
| 512 | Game Play Analysis II | dashboard/problems.json (embedded leetcode_solution) | Database | SQL Join | - | dashboard-only; no problem folder |
| 516 | Longest Palindromic Subsequence | dashboard/problems.json (embedded leetcode_solution) | String | Dynamic Programming | - | dashboard-only; no problem folder |
| 528 | Random Pick with Weight | dashboard/problems.json (embedded leetcode_solution) | Array, Math | Binary Search | Math, Prefix Sum, Randomized | dashboard-only; no problem folder |
| 542 | 01 Matrix | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | BFS | Dynamic Programming, Matrix Traversal | dashboard-only; no problem folder |
| 560 | Subarray Sum Equals K | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | Hashing | Prefix Sum | dashboard-only; no problem folder |
| 567 | Permutation in String | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Sliding Window | Hashing, Two Pointers | dashboard-only; no problem folder |
| 577 | Employee Bonus | dashboard/problems.json (embedded leetcode_solution) | Database | SQL Join | - | dashboard-only; no problem folder |
| 594 | Longest Harmonious Subsequence | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | Sliding Window | Hashing, Sorting, Counting | dashboard-only; no problem folder |
| 611 | Valid Triangle Number | dashboard/problems.json (embedded leetcode_solution) | Array | Binary Search | Two Pointers, Greedy, Sorting | dashboard-only; no problem folder |
| 623 | Add One Row to Tree | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | BFS | DFS | dashboard-only; no problem folder |
| 636 | Exclusive Time of Functions | dashboard/problems.json (embedded leetcode_solution) | Array, Stack | Stack | - | dashboard-only; no problem folder |
| 647 | Palindromic Substrings | dashboard/problems.json (embedded leetcode_solution) | String | Two Pointers | Dynamic Programming | dashboard-only; no problem folder |
| 663 | Equal Tree Partition | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | Tree Postorder / Return Information | DFS | dashboard-only; no problem folder |
| 683 | K Empty Slots | dashboard/problems.json (embedded leetcode_solution) | Array, Queue, Heap | Sliding Window | Queue, Heap / Priority Queue | dashboard-only; no problem folder |
| 687 | Longest Univalue Path | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | DFS | - | dashboard-only; no problem folder |
| 695 | Max Area of Island | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | BFS | DFS, Matrix Traversal | dashboard-only; no problem folder |
| 698 | Partition to K Equal Sum Subsets | dashboard/problems.json (embedded leetcode_solution) | Array, Bit Manipulation | Backtracking | Dynamic Programming, Bit Manipulation | dashboard-only; no problem folder |
| 705 | Design HashSet | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Linked List, Design | Design | Hashing | dashboard-only; no problem folder |
| 706 | Design HashMap | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Linked List, Design | Design | Hashing | dashboard-only; no problem folder |
| 716 | Max Stack | dashboard/problems.json (embedded leetcode_solution) | Linked List, Stack, Design | Stack | Design | dashboard-only; no problem folder |
| 740 | Delete and Earn | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | 1D Dynamic Programming | Hashing, Dynamic Programming | dashboard-only; no problem folder |
| 742 | Closest Leaf in a Binary Tree | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | BFS | DFS | dashboard-only; no problem folder |
| 743 | Network Delay Time | dashboard/problems.json (embedded leetcode_solution) | Graph, Heap | Heap / Priority Queue | DFS, BFS, Graph Traversal | dashboard-only; no problem folder |
| 763 | Partition Labels | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Two Pointers | Hashing, Greedy | dashboard-only; no problem folder |
| 778 | Swim in Rising Water | dashboard/problems.json (embedded leetcode_solution) | Array, Heap, Matrix | Heap / Priority Queue | Binary Search, DFS, BFS, Matrix Traversal | dashboard-only; no problem folder |
| 787 | Cheapest Flights Within K Stops | dashboard/problems.json (embedded leetcode_solution) | Graph, Heap | Shortest Path | Dynamic Programming, DFS, BFS, Graph Traversal, Heap / Priority Queue | dashboard-only; no problem folder |
| 863 | All Nodes Distance K in Binary Tree | dashboard/problems.json (embedded leetcode_solution) | Hash Table, Binary Tree | BFS | Hashing, DFS | dashboard-only; no problem folder |
| 886 | Possible Bipartition | dashboard/problems.json (embedded leetcode_solution) | Graph | BFS | DFS, Graph Traversal | dashboard-only; no problem folder |
| 909 | Snakes and Ladders | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | BFS | Matrix Traversal | dashboard-only; no problem folder |
| 921 | Minimum Add to Make Parentheses Valid | dashboard/problems.json (embedded leetcode_solution) | String, Stack | Stack | Greedy | dashboard-only; no problem folder |
| 925 | Long Pressed Name | dashboard/problems.json (embedded leetcode_solution) | String | Two Pointers | - | dashboard-only; no problem folder |
| 934 | Shortest Bridge | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | BFS | DFS, Matrix Traversal | dashboard-only; no problem folder |
| 941 | Valid Mountain Array | dashboard/problems.json (embedded leetcode_solution) | Array | Array Scanning | - | dashboard-only; no problem folder |
| 973 | K Closest Points to Origin | dashboard/problems.json (embedded leetcode_solution) | Array, Math, Heap | Heap / Priority Queue | Math, Divide and Conquer, Geometry, Sorting, Quickselect | dashboard-only; no problem folder |
| 988 | Smallest String Starting From Leaf | dashboard/problems.json (embedded leetcode_solution) | String, Binary Tree | Backtracking | DFS | dashboard-only; no problem folder |
| 994 | Rotting Oranges | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | BFS | Matrix Traversal | dashboard-only; no problem folder |
| 1026 | Maximum Difference Between Node and Ancestor | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | Tree Postorder / Return Information | DFS | dashboard-only; no problem folder |
| 1041 | Robot Bounded In Circle | dashboard/problems.json (embedded leetcode_solution) | Math, String | Simulation | Math | dashboard-only; no problem folder |
| 1061 | Lexicographically Smallest Equivalent String | dashboard/problems.json (embedded leetcode_solution) | String | Union Find | - | dashboard-only; no problem folder |
| 1064 | Fixed Point | dashboard/problems.json (embedded leetcode_solution) | Array | Binary Search | - | dashboard-only; no problem folder |
| 1117 | Building H2O | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | Concurrency | - | dashboard-only; no problem folder |
| 1197 | Minimum Knight Moves | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | BFS | - | dashboard-only; no problem folder |
| 1220 | Count Vowels Permutation | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | State Machine DP | Dynamic Programming | dashboard-only; no problem folder |
| 1249 | Minimum Remove to Make Valid Parentheses | dashboard/problems.json (embedded leetcode_solution) | String, Stack | Stack | - | dashboard-only; no problem folder |
| 1290 | Convert Binary Number in a Linked List to Integer | dashboard/problems.json (embedded leetcode_solution) | Linked List, Math | Linked List Traversal | Math | dashboard-only; no problem folder |
| 1295 | Find Numbers with Even Number of Digits | dashboard/problems.json (embedded leetcode_solution) | Array, Math | Simulation | Math | dashboard-only; no problem folder |
| 1298 | Maximum Candies You Can Get from Boxes | dashboard/problems.json (embedded leetcode_solution) | Array, Graph | BFS | Graph Traversal | dashboard-only; no problem folder |
| 1299 | Replace Elements with Greatest Element on Right Side | dashboard/problems.json (embedded leetcode_solution) | Array | Prefix/Suffix Precomputation | - | dashboard-only; no problem folder |
| 1302 | Deepest Leaves Sum | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | BFS | DFS | dashboard-only; no problem folder |
| 1325 | Delete Leaves With a Given Value | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | Tree Postorder / Return Information | DFS | dashboard-only; no problem folder |
| 1346 | Check If N and Its Double Exist | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | Hashing | Two Pointers, Binary Search, Sorting | dashboard-only; no problem folder |
| 1353 | Maximum Number of Events That Can Be Attended | dashboard/problems.json (embedded leetcode_solution) | Array, Heap | Greedy | Sorting, Heap / Priority Queue | dashboard-only; no problem folder |
| 1386 | Cinema Seat Allocation | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Bit Manipulation | Hashing | Greedy, Bit Manipulation | dashboard-only; no problem folder |
| 1394 | Find Lucky Integer in an Array | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | Counting | Hashing | dashboard-only; no problem folder |
| 1413 | Minimum Value to Get Positive Step by Step Sum | dashboard/problems.json (embedded leetcode_solution) | Array | Prefix Sum | - | dashboard-only; no problem folder |
| 1432 | Max Difference You Can Get From Changing an Integer | dashboard/problems.json (embedded leetcode_solution) | Math | Greedy | Math | dashboard-only; no problem folder |
| 1480 | Running Sum of 1d Array | dashboard/problems.json (embedded leetcode_solution) | Array | Prefix Sum | - | dashboard-only; no problem folder |
| 1550 | Three Consecutive Odds | dashboard/problems.json (embedded leetcode_solution) | Array | Array Scanning | - | dashboard-only; no problem folder |
| 1554 | Strings Differ by One Character | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Hashing | - | dashboard-only; no problem folder |
| 1584 | Min Cost to Connect All Points | dashboard/problems.json (embedded leetcode_solution) | Array, Graph | Union Find | Graph Traversal | dashboard-only; no problem folder |
| 1644 | Lowest Common Ancestor of a Binary Tree II | dashboard/problems.json (embedded leetcode_solution) | Binary Tree | DFS | - | dashboard-only; no problem folder |
| 1650 | Lowest Common Ancestor of a Binary Tree III | dashboard/problems.json (embedded leetcode_solution) | Hash Table, Binary Tree | Two Pointers | Hashing | dashboard-only; no problem folder |
| 1672 | Richest Customer Wealth | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | Matrix Traversal | - | dashboard-only; no problem folder |
| 1676 | Lowest Common Ancestor of a Binary Tree IV | dashboard/problems.json (embedded leetcode_solution) | Hash Table, Binary Tree | DFS | Hashing | dashboard-only; no problem folder |
| 1695 | Maximum Erasure Value | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | Sliding Window | Hashing | dashboard-only; no problem folder |
| 1751 | Maximum Number of Events That Can Be Attended II | dashboard/problems.json (embedded leetcode_solution) | Array | Binary Search | Dynamic Programming, Sorting | dashboard-only; no problem folder |
| 1752 | Check if Array Is Sorted and Rotated | dashboard/problems.json (embedded leetcode_solution) | Array | Array Scanning | - | dashboard-only; no problem folder |
| 1790 | Check if One String Swap Can Make Strings Equal | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Simulation | Hashing, Counting | dashboard-only; no problem folder |
| 1797 | Design Authentication Manager | dashboard/problems.json (embedded leetcode_solution) | Hash Table, Linked List, Design | Design | Hashing | dashboard-only; no problem folder |
| 1800 | Maximum Ascending Subarray Sum | dashboard/problems.json (embedded leetcode_solution) | Array | Array Scanning | - | dashboard-only; no problem folder |
| 1857 | Largest Color Value in a Directed Graph | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String, Graph | Topological Sort | Hashing, Dynamic Programming, Graph Traversal, Counting | dashboard-only; no problem folder |
| 1865 | Finding Pairs With a Certain Sum | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Design | Hashing | Design | dashboard-only; no problem folder |
| 1900 | The Earliest and Latest Rounds Where Players Compete | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | Dynamic Programming | - | dashboard-only; no problem folder |
| 1905 | Count Sub Islands | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | DFS | BFS, Matrix Traversal | dashboard-only; no problem folder |
| 1926 | Nearest Exit from Entrance in Maze | dashboard/problems.json (embedded leetcode_solution) | Array, Matrix | BFS | Matrix Traversal | dashboard-only; no problem folder |
| 1974 | Minimum Time to Type Word Using Special Typewriter | dashboard/problems.json (embedded leetcode_solution) | String | Simulation | Greedy | dashboard-only; no problem folder |
| 2014 | Longest Subsequence Repeated k Times | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Backtracking | Hashing, Two Pointers, Counting | dashboard-only; no problem folder |
| 2016 | Maximum Difference Between Increasing Elements | dashboard/problems.json (embedded leetcode_solution) | Array | Array Scanning | - | dashboard-only; no problem folder |
| 2040 | Kth Smallest Product of Two Sorted Arrays | dashboard/problems.json (embedded leetcode_solution) | Array | Binary Search | - | dashboard-only; no problem folder |
| 2043 | Simple Bank System | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Design | Design | Hashing, Simulation | dashboard-only; no problem folder |
| 2081 | Sum of k-Mirror Numbers | dashboard/problems.json (embedded leetcode_solution) | Math | Math | - | dashboard-only; no problem folder |
| 2090 | K Radius Subarray Averages | dashboard/problems.json (embedded leetcode_solution) | Array | Prefix Sum | Sliding Window | dashboard-only; no problem folder |
| 2099 | Find Subsequence of Length K With the Largest Sum | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Heap | Heap / Priority Queue | Hashing, Sorting | dashboard-only; no problem folder |
| 2138 | Divide a String Into Groups of Size k | dashboard/problems.json (embedded leetcode_solution) | String | Simulation | - | dashboard-only; no problem folder |
| 2163 | Minimum Difference in Sums After Removal of Elements | dashboard/problems.json (embedded leetcode_solution) | Array, Heap | Heap / Priority Queue | Dynamic Programming | dashboard-only; no problem folder |
| 2200 | Find All K-Distant Indices in an Array | dashboard/problems.json (embedded leetcode_solution) | Array | Two Pointers | - | dashboard-only; no problem folder |
| 2276 | Count Integers in Intervals | dashboard/problems.json (embedded leetcode_solution) | Design | Intervals | Design | dashboard-only; no problem folder |
| 2294 | Partition Array Such That Maximum Difference Is K | dashboard/problems.json (embedded leetcode_solution) | Array | Greedy | Sorting | dashboard-only; no problem folder |
| 2311 | Longest Binary Subsequence Less Than or Equal to K | dashboard/problems.json (embedded leetcode_solution) | String | Greedy | Dynamic Programming | dashboard-only; no problem folder |
| 2359 | Find Closest Node to Given Two Nodes | dashboard/problems.json (embedded leetcode_solution) | Graph | DFS | Graph Traversal | dashboard-only; no problem folder |
| 2402 | Meeting Rooms III | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table, Heap | Heap / Priority Queue | Hashing, Sorting, Simulation | dashboard-only; no problem folder |
| 2410 | Maximum Matching of Players With Trainers | dashboard/problems.json (embedded leetcode_solution) | Array | Greedy | Two Pointers, Sorting | dashboard-only; no problem folder |
| 2434 | Using a Robot to Print the Lexicographically Smallest String | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String, Stack | Stack | Hashing, Greedy | dashboard-only; no problem folder |
| 2560 | House Robber IV | dashboard/problems.json (embedded leetcode_solution) | Array | Binary Search | Dynamic Programming, Greedy | dashboard-only; no problem folder |
| 2566 | Maximum Difference by Remapping a Digit | dashboard/problems.json (embedded leetcode_solution) | Math | Greedy | Math | dashboard-only; no problem folder |
| 2616 | Minimize the Maximum Difference of Pairs | dashboard/problems.json (embedded leetcode_solution) | Array | Binary Search | Dynamic Programming, Greedy, Sorting | dashboard-only; no problem folder |
| 2620 | Counter | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | NEEDS_REVIEW | - | dashboard-only; no problem folder |
| 2654 | Minimum Number of Operations to Make All Array Elements Equal to 1 | dashboard/problems.json (embedded leetcode_solution) | Array, Math | Math | - | dashboard-only; no problem folder |
| 2667 | Create Hello World Function | dashboard/problems.json (embedded leetcode_solution) | NEEDS_REVIEW | NEEDS_REVIEW | - | dashboard-only; no problem folder |
| 2894 | Divisible and Non-divisible Sums Difference | dashboard/problems.json (embedded leetcode_solution) | Math | Math | - | dashboard-only; no problem folder |
| 2900 | Longest Unequal Adjacent Groups Subsequence I | dashboard/problems.json (embedded leetcode_solution) | Array, String | Dynamic Programming | Greedy | dashboard-only; no problem folder |
| 2901 | Longest Unequal Adjacent Groups Subsequence II | dashboard/problems.json (embedded leetcode_solution) | Array, String | Dynamic Programming | - | dashboard-only; no problem folder |
| 2929 | Distribute Candies Among Children II | dashboard/problems.json (embedded leetcode_solution) | Math | Math | - | dashboard-only; no problem folder |
| 2964 | Number of Divisible Triplet Sums | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | Counting | Hashing | dashboard-only; no problem folder |
| 2966 | Divide Array Into Arrays With Max Difference | dashboard/problems.json (embedded leetcode_solution) | Array | Greedy | Sorting | dashboard-only; no problem folder |
| 3019 | Number of Changing Keys | dashboard/problems.json (embedded leetcode_solution) | String | String Scanning | - | dashboard-only; no problem folder |
| 3024 | Type of Triangle | dashboard/problems.json (embedded leetcode_solution) | Array, Math | Simulation | Math, Sorting | dashboard-only; no problem folder |
| 3034 | Number of Subarrays That Match a Pattern I | dashboard/problems.json (embedded leetcode_solution) | Array | Array Scanning | String Matching | dashboard-only; no problem folder |
| 3042 | Count Prefix and Suffix Pairs I | dashboard/problems.json (embedded leetcode_solution) | Array, String, Trie | Trie | String Matching | dashboard-only; no problem folder |
| 3046 | Split the Array | dashboard/problems.json (embedded leetcode_solution) | Array, Hash Table | Hashing | Counting | dashboard-only; no problem folder |
| 3068 | Find the Maximum Sum of Node Values | dashboard/problems.json (embedded leetcode_solution) | Array, Bit Manipulation, Tree | Dynamic Programming | Greedy, Bit Manipulation, Sorting | dashboard-only; no problem folder |
| 3069 | Distribute Elements Into Two Arrays I | dashboard/problems.json (embedded leetcode_solution) | Array | Simulation | - | dashboard-only; no problem folder |
| 3085 | Minimum Deletions to Make String K-Special | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Hashing | Greedy, Sorting, Counting | dashboard-only; no problem folder |
| 3105 | Longest Strictly Increasing or Strictly Decreasing Subarray | dashboard/problems.json (embedded leetcode_solution) | Array | String Scanning | - | dashboard-only; no problem folder |
| 3136 | Valid Word | dashboard/problems.json (embedded leetcode_solution) | String | Simulation | - | dashboard-only; no problem folder |
| 3170 | Lexicographically Minimum String After Removing Stars | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String, Stack, Heap | Heap / Priority Queue | Hashing, Stack, Greedy | dashboard-only; no problem folder |
| 3201 | Find the Maximum Length of Valid Subsequence I | dashboard/problems.json (embedded leetcode_solution) | Array | Dynamic Programming | - | dashboard-only; no problem folder |
| 3202 | Find the Maximum Length of Valid Subsequence II | dashboard/problems.json (embedded leetcode_solution) | Array | Dynamic Programming | - | dashboard-only; no problem folder |
| 3228 | Maximum Number of Operations to Move Ones to the End | dashboard/problems.json (embedded leetcode_solution) | String | Greedy | Counting | dashboard-only; no problem folder |
| 3304 | Find the K-th Character in String Game I | dashboard/problems.json (embedded leetcode_solution) | Math, Bit Manipulation | Bit Manipulation | Math, Simulation | dashboard-only; no problem folder |
| 3307 | Find the K-th Character in String Game II | dashboard/problems.json (embedded leetcode_solution) | Math, Bit Manipulation | Bit Manipulation | Math | dashboard-only; no problem folder |
| 3333 | Find the Original Typed String II | dashboard/problems.json (embedded leetcode_solution) | String | String Dynamic Programming | Dynamic Programming, Prefix Sum | dashboard-only; no problem folder |
| 3355 | Zero Array Transformation I | dashboard/problems.json (embedded leetcode_solution) | Array | Prefix Sum | - | dashboard-only; no problem folder |
| 3362 | Zero Array Transformation III | dashboard/problems.json (embedded leetcode_solution) | Array, Heap | Greedy | Two Pointers, Sorting, Heap / Priority Queue, Prefix Sum | dashboard-only; no problem folder |
| 3372 | Maximize the Number of Target Nodes After Connecting Trees I | dashboard/problems.json (embedded leetcode_solution) | Tree | BFS | DFS | dashboard-only; no problem folder |
| 3403 | Find the Lexicographically Largest String From the Box I | dashboard/problems.json (embedded leetcode_solution) | String | String Scanning | Two Pointers | dashboard-only; no problem folder |
| 3405 | Count the Number of Arrays with K Matching Adjacent Elements | dashboard/problems.json (embedded leetcode_solution) | Math | Math | - | dashboard-only; no problem folder |
| 3423 | Maximum Difference Between Adjacent Elements in a Circular Array | dashboard/problems.json (embedded leetcode_solution) | Array | Array Scanning | - | dashboard-only; no problem folder |
| 3439 | Reschedule Meetings for Maximum Free Time I | dashboard/problems.json (embedded leetcode_solution) | Array | Sliding Window | Greedy | dashboard-only; no problem folder |
| 3440 | Reschedule Meetings for Maximum Free Time II | dashboard/problems.json (embedded leetcode_solution) | Array | Greedy | - | dashboard-only; no problem folder |
| 3442 | Maximum Difference Between Even and Odd Frequency I | dashboard/problems.json (embedded leetcode_solution) | Hash Table, String | Counting | Hashing | dashboard-only; no problem folder |
| 3443 | Maximum Manhattan Distance After K Changes | dashboard/problems.json (embedded leetcode_solution) | Hash Table, Math, String | Hashing | Math, Counting | dashboard-only; no problem folder |
| 3445 | Maximum Difference Between Even and Odd Frequency II | dashboard/problems.json (embedded leetcode_solution) | String | Sliding Window | Prefix Sum | dashboard-only; no problem folder |
| 3453 | Separate Squares I | dashboard/problems.json (embedded leetcode_solution) | Array | Binary Search | - | dashboard-only; no problem folder |
| 3480 | Maximize Subarrays After Removing One Conflicting Pair | dashboard/problems.json (embedded leetcode_solution) | Array | NEEDS_REVIEW | Prefix Sum | dashboard-only; no problem folder |

## Problems Whose Pattern Classification Needs Manual Review

| LC | Title | Location | Reason |
| --- | --- | --- | --- |
| 21 | Merge Two Sorted Lists | 0021-merge-two-sorted-lists | Primary pattern is NEEDS_REVIEW from audit. |
| 24 | Swap Nodes in Pairs | 0024-swap-nodes-in-pairs | Primary pattern is NEEDS_REVIEW from audit. |
| 65 | Valid Number | 0065-valid-number | Primary pattern is NEEDS_REVIEW from audit. |
| 81 | Search in Rotated Sorted Array II | 0081-search-in-rotated-sorted-array-ii | Primary pattern is NEEDS_REVIEW from audit. |
| 450 | Delete Node in a BST | 0450-delete-node-in-a-bst | Primary pattern is NEEDS_REVIEW from audit. |
| 2620 | Counter | dashboard/problems.json (embedded leetcode_solution) | Primary pattern is NEEDS_REVIEW from audit. |
| 2667 | Create Hello World Function | dashboard/problems.json (embedded leetcode_solution) | Primary pattern is NEEDS_REVIEW from audit. |
| 3480 | Maximize Subarrays After Removing One Conflicting Pair | dashboard/problems.json (embedded leetcode_solution) | Primary pattern is NEEDS_REVIEW from audit. |

Additional code-level review is recommended for accepted solutions with debug prints or non-textbook shortcuts even if their pattern is classified.

## Problems Whose Actual LeetCode ID Needs Verification

No physical synced directory lacked an actual LC frontend ID after slug-based matching against local API-enriched dashboard metadata.

Still verify IDs before writing permanent metadata because this audit did not run a fresh LeetCode API fetch. Two folder slugs required hyphen-normalized matching:

| LC | Sync ID | Title | Location |
| --- | --- | --- | --- |
| 167 | 0167 | Two Sum II - Input Array Is Sorted | 0167-two-sum-ii---input-array-is-sorted |
| 653 | 0653 | Two Sum IV - Input is a BST | 0653-two-sum-iv---input-is-a-bst |

## Sync ID Mismatch Examples

125 physical folders have a sync/internal directory ID that differs from the actual frontend LC ID. Representative examples:

- `1013-fibonacci-number`: sync/internal `1013`, actual LC `509` - Fibonacci Number.
- `0774-maximum-depth-of-n-ary-tree`: sync/internal `0774`, actual LC `559` - Maximum Depth of N-ary Tree.
- `0775-n-ary-tree-preorder-traversal`: sync/internal `0775`, actual LC `589` - N-ary Tree Preorder Traversal.
- `0776-n-ary-tree-postorder-traversal`: sync/internal `0776`, actual LC `590` - N-ary Tree Postorder Traversal.
- `0783-search-in-a-binary-search-tree`: sync/internal `0783`, actual LC `700` - Search in a Binary Search Tree.
- `0792-binary-search`: sync/internal `0792`, actual LC `704` - Binary Search.
- `0742-to-lower-case`: sync/internal `0742`, actual LC `709` - To Lower Case.
- `0745-find-smallest-letter-greater-than-target`: sync/internal `0745`, actual LC `744` - Find Smallest Letter Greater Than Target.
- `0747-min-cost-climbing-stairs`: sync/internal `0747`, actual LC `746` - Min Cost Climbing Stairs.
- `0753-open-the-lock`: sync/internal `0753`, actual LC `752` - Open the Lock.
- `0763-special-binary-string`: sync/internal `0763`, actual LC `761` - Special Binary String.
- `0782-jewels-and-stones`: sync/internal `0782`, actual LC `771` - Jewels and Stones.
- `0799-minimum-distance-between-bst-nodes`: sync/internal `0799`, actual LC `783` - Minimum Distance Between BST Nodes.
- `0820-find-eventual-safe-states`: sync/internal `0820`, actual LC `802` - Find Eventual Safe States.
- `0822-unique-morse-code-words`: sync/internal `0822`, actual LC `804` - Unique Morse Code Words.
- `0837-most-common-word`: sync/internal `0837`, actual LC `819` - Most Common Word.
- `0841-shortest-distance-to-a-character`: sync/internal `0841`, actual LC `821` - Shortest Distance to a Character.
- `0851-goat-latin`: sync/internal `0851`, actual LC `824` - Goat Latin.
- `0861-flipping-an-image`: sync/internal `0861`, actual LC `832` - Flipping an Image.
- `0871-keys-and-rooms`: sync/internal `0871`, actual LC `841` - Keys and Rooms.
- `0883-car-fleet`: sync/internal `0883`, actual LC `853` - Car Fleet.
- `0904-leaf-similar-trees`: sync/internal `0904`, actual LC `872` - Leaf-Similar Trees.
- `0907-koko-eating-bananas`: sync/internal `0907`, actual LC `875` - Koko Eating Bananas.
- `0908-middle-of-the-linked-list`: sync/internal `0908`, actual LC `876` - Middle of the Linked List.
- `0916-decoded-string-at-index`: sync/internal `0916`, actual LC `880` - Decoded String at Index.

## Orphan, Junk, Suspicious, or Manual-Review Content

- `000/00000/aaaaa.md`: useful pattern notes in a placeholder-like directory; move content into `revision/patterns/README.md` or archive later.
- `dashboard/__pycache__/fetch_leetcode.cpython-313.pyc`: generated bytecode is tracked; archive/remove from version control later.
- `dashboard/.env`: ignored local secret file exists; keep untracked and do not read into reports.
- `dashboard/problems.json`: valuable but generated/stale; 543 API-enriched solved records with code plus 109 stale no-slug records.
- `dashboard/generate_data.py`: unsafe for migration because it derives problem number from the first four folder digits.
- `dashboard/fetch_leetcode.py`: useful for metadata enrichment, but folder sync helpers also look up existing folders by numeric prefix.
- `dashboard/_test_auth.py`: local API test utility reads `.env` and contains a fixed submission ID.
- `0595-big-countries/` and `1908-recyclable-and-low-fat-products/`: each has both pandas `solution.py` and SQL `solution.sql`; choose a language policy later.
- Accepted solution files with active `print` statements:
  - `0100-same-tree/solution.py:13` - `print(p,q)`
  - `0128-longest-consecutive-sequence/solution.py:12` - `print (m)`
  - `0225-implement-stack-using-queues/solution.py:11` - `print(self.q[len(self.q)-1])`
  - `0649-dota2-senate/solution.py:12` - `print (r,d)`
  - `0739-daily-temperatures/solution.py:18` - `print(i,previous_i)`
  - `128. Longest Consecutive Sequence.py:28` - `print (m)`
  - `dashboard/_test_auth.py:13` - `print(f"Cookie length: {len(session)}")`
  - `dashboard/_test_auth.py:50` - `print("SUCCESS:", json.dumps(data, indent=2)[:1000])`
  - `dashboard/_test_auth.py:52` - `print(f"Error: {e}")`
  - `dashboard/_test_auth.py:55` - `print(f"Response body: {body}")`
  - `dashboard/fetch_leetcode.py:75` - `print("ERROR: No LEETCODE_SESSION cookie provided.")`
  - `dashboard/fetch_leetcode.py:76` - `print()`
  - `dashboard/fetch_leetcode.py:77` - `print("How to get your session cookie:")`
  - `dashboard/fetch_leetcode.py:78` - `print("  1. Log into https://leetcode.com in your browser")`
  - `dashboard/fetch_leetcode.py:79` - `print("  2. Open DevTools (F12) -> Application -> Cookies -> leetcode.com")`
  - `dashboard/fetch_leetcode.py:80` - `print("  3. Copy the value of 'LEETCODE_SESSION'")`
  - `dashboard/fetch_leetcode.py:81` - `print()`
  - `dashboard/fetch_leetcode.py:82` - `print("Then either:")`
  - `dashboard/fetch_leetcode.py:83` - `print('  set LEETCODE_SESSION=<value>')`
  - `dashboard/fetch_leetcode.py:84` - `print("  python dashboard/fetch_leetcode.py")`
  - `dashboard/fetch_leetcode.py:85` - `print()`
  - `dashboard/fetch_leetcode.py:86` - `print("Or:")`
  - `dashboard/fetch_leetcode.py:87` - `print("  python dashboard/fetch_leetcode.py --session <value>")`
  - `dashboard/fetch_leetcode.py:88` - `print()`
  - `dashboard/fetch_leetcode.py:89` - `print("Or create dashboard/.env with:")`
  - `dashboard/fetch_leetcode.py:90` - `print("  LEETCODE_SESSION=<value>")`
  - `dashboard/fetch_leetcode.py:116` - `print(f"  GraphQL errors: {data['errors']}")`
  - `dashboard/fetch_leetcode.py:121` - `print(f"  AUTH ERROR ({e.code}): Session cookie may be expired. Refresh it.")`
  - `dashboard/fetch_leetcode.py:123` - `print(f"  HTTP Error {e.code}: {e.reason}")`
  - `dashboard/fetch_leetcode.py:126` - `print(f"  Network error: {e.reason}")`
  - `dashboard/fetch_leetcode.py:231` - `print("Fetching all solved problems from LeetCode...")`
  - `dashboard/fetch_leetcode.py:242` - `print("  Failed to fetch problem list. Check your session cookie.")`
  - `dashboard/fetch_leetcode.py:255` - `print(f"  Page {skip // limit}: {len(solved_page)} solved out of {len(questions)`
  - `dashboard/fetch_leetcode.py:263` - `print(f"  Total solved problems fetched: {len(all_questions)}")`
  - `dashboard/fetch_leetcode.py:441` - `print(f"\n  Updated {updated_count} existing problems with LeetCode data")`
  - `dashboard/fetch_leetcode.py:442` - `print(f"  Added {new_count} new problems from LeetCode")`
  - `dashboard/fetch_leetcode.py:463` - `print(f"\nFetching accepted solutions for {len(to_fetch)} problems...")`
  - `dashboard/fetch_leetcode.py:464` - `print("  (This takes ~3 sec per problem due to rate limiting)")`
  - `dashboard/fetch_leetcode.py:465` - `print(f"  Estimated time: ~{len(to_fetch) * 3 // 60} min {len(to_fetch) * 3 % 60`
  - `dashboard/fetch_leetcode.py:466` - `print()`
  - `dashboard/fetch_leetcode.py:470` - `print(f"  [{i+1}/{len(to_fetch)}] Fetching solution for #{num} {p['name']}...", `
  - `dashboard/fetch_leetcode.py:479` - `print(f"OK ({sub['language']}, {sub['runtime']})")`
  - `dashboard/fetch_leetcode.py:481` - `print("No submission found")`
  - `dashboard/fetch_leetcode.py:485` - `print(f"\n  Fetched {solution_count} solutions")`
  - `dashboard/fetch_leetcode.py:492` - `print(f"\nWritten {len(merged)} problems to {PROBLEMS_JSON}")`
  - `dashboard/fetch_leetcode.py:542` - `print("No problems.json found. Run the fetcher first.")`
  - `dashboard/fetch_leetcode.py:557` - `print(f"\nSyncing folders for {len(problems_with_code)} problems with solution c`
  - `dashboard/fetch_leetcode.py:558` - `print(f"  Existing folders found: {len(existing_folders)}")`
  - `dashboard/fetch_leetcode.py:585` - `print(f"  + Added solution to existing {existing_path.name}/")`
  - `dashboard/fetch_leetcode.py:627` - `print(f"  + Created {folder_name}/ ({lang})")`
  - `dashboard/fetch_leetcode.py:633` - `print(f"\nFolder sync complete:")`
  - `dashboard/fetch_leetcode.py:634` - `print(f"  Created: {created} new folders")`
  - `dashboard/fetch_leetcode.py:635` - `print(f"  Updated: {updated} existing folders (added solution)")`
  - `dashboard/fetch_leetcode.py:636` - `print(f"  Skipped: {skipped} (already complete or no code)")`
  - `dashboard/fetch_leetcode.py:638` - `print(f"  Descriptions fetched: {desc_fetched}")`
  - `dashboard/fetch_leetcode.py:662` - `print("Syncing folders from existing problems.json (no LeetCode fetch)...")`
  - `dashboard/fetch_leetcode.py:664` - `print("\nDone!")`
  - `dashboard/fetch_leetcode.py:668` - `print("Testing LeetCode session...")`
  - `dashboard/fetch_leetcode.py:671` - `print("\nFailed to authenticate. Please check your LEETCODE_SESSION cookie.")`
  - `dashboard/fetch_leetcode.py:675` - `print(f"  Authenticated! Connection successful (got {len(questions)} test record`
  - `dashboard/fetch_leetcode.py:680` - `print("No solved problems found. Exiting.")`
  - `dashboard/fetch_leetcode.py:696` - `print("\nDone! Refresh your dashboard to see the updated data.")`
  - `dashboard/fetch_leetcode.py:698` - `print("Tip: Run without --no-solutions to also fetch your accepted code.")`
  - `dashboard/fetch_leetcode.py:700` - `print("Tip: Run with --sync-folders to create solution folders in your repo.")`
  - `dashboard/generate_data.py:282` - `print("Scanning solution folders...")`
  - `dashboard/generate_data.py:284` - `print(f"  Found {len(folder_problems)} problems in folders")`
  - `dashboard/generate_data.py:286` - `print("Scanning loose .py files...")`
  - `dashboard/generate_data.py:288` - `print(f"  Found {len(loose_problems)} problems in loose files")`
  - `dashboard/generate_data.py:292` - `print(f"  Total unique problems: {len(all_problems)}")`
  - `dashboard/generate_data.py:294` - `print("Merging with existing data...")`
  - `dashboard/generate_data.py:301` - `print(f"Written {len(merged)} problems to {PROBLEMS_JSON}")`
  - `dashboard/generate_data.py:309` - `print("\nSummary:")`
  - `dashboard/generate_data.py:311` - `print(f"  {d}: {count}")`
  - `dashboard/generate_data.py:312` - `print(f"  Total: {len(merged)}")`
- Root `leetcode.md` has a legacy link list and trailing empty links; replace with generated trackers.
- Root `roadmap.md` is generic and has mojibake/encoding artifacts; archive or condense into `revision/README.md`.
- Root `README.md` is useful as a project front door/resource list, but stale as a problem index.

## Legacy Docs Review

- `README.md`: useful overview/resources; eventually rewrite around the revision workflow and link to `revision/tracker.md`.
- `leetcode.md`: stale manual index of 26 legacy files with empty links; archive after generated tracker exists.
- `roadmap.md`: useful general roadmap but not repo-specific; archive or fold useful pieces into the revision homepage.

## Automation Plan

Do not implement yet. Future `scripts/build_revision_indexes.py` should:

- Scan canonical directories by slug, not numeric prefix.
- Read YAML frontmatter from each `REVISION.md`.
- Generate `revision/tracker.md`, `revision/topics/*.md`, and `revision/patterns/*.md`.
- Detect folders missing `REVISION.md` and list them in `revision/unclassified.md`.
- Detect dashboard-only solved records and report extraction/archive status.
- Validate relative links and frontmatter consistency.
- Fail loudly if two physical folders normalize to the same slug.

`scripts/validate_revision_metadata.py` should separately check schema, duplicate slugs, confidence values, invalid patterns/topics, and broken links.

## Exact Migration Plan

1. Freeze current state with this audit report and review the dashboard-only solved records decision.
2. Create a checked-in slug-to-frontend-ID metadata source from `dashboard/problems.json` or a fresh LeetCode API export. Do not key by folder prefix.
3. Add `revision/` skeleton pages and scripts without moving problem folders.
4. Generate draft `REVISION.md` files with `confidence: yellow` and conservative metadata; commit only after reviewing diffs.
5. Move category C legacy files into canonical `alternatives/` folders and note them in `REVISION.md`.
6. For category A/B legacy files, copy useful comments into `REVISION.md`, then archive root files after validation.
7. Decide whether the 209 dashboard-only accepted solutions should be extracted into canonical folders or archived as dashboard cache.
8. Update or replace `leetcode.md` and `roadmap.md` with generated navigation/tracker pages.
9. Add validators and CI; leave `.github/workflows/sync_leetcode.yml` unchanged until custom metadata survives a sync run.
10. Regenerate `dashboard/problems.json` from revision metadata or retire the dashboard data path.

## Files That Would Be Moved

- `75. Sort Colors.py` -> `0075-sort-colors/alternatives/counting-passes.py`.
- `81. Search in Rotated Sorted Array II.py` -> `0081-search-in-rotated-sorted-array-ii/alternatives/duplicate-aware-binary-search.py`.
- `977. Squares of a Sorted Array.py` -> `1019-squares-of-a-sorted-array/alternatives/split-negative-merge.py`.
- Potentially `16. 3Sum Closest.py` -> archive or `alternatives/sorted-two-pointers-legacy.py` if comments are worth preserving.
- Potentially `000/00000/aaaaa.md` -> `revision/patterns/README.md` or `archive/notes/patterns.md`.

## Files That Would Be Created

- `revision/README.md`
- `revision/tracker.md`
- `revision/unclassified.md`
- `revision/patterns/README.md`
- `revision/patterns/*.md`
- `revision/topics/*.md`
- `revision/queues/weak-problems.md`
- `revision/queues/must-redo.md`
- `scripts/build_revision_indexes.py`
- `scripts/validate_revision_metadata.py`
- `<each canonical problem folder>/REVISION.md`
- `<canonical folders with real alternate approaches>/alternatives/*.py`

## Files That Would Eventually Be Archived

- `1004. Max Consecutive Ones III.py`
- `1071.Greatest Common Divisor of Strings.py`
- `111. Minimum Depth of Binary Tree.py`
- `1161. Maximum Level Sum of a Binary Tree.py`
- `1268 Search Suggestions System.py`
- `128. Longest Consecutive Sequence.py`
- `1431.  Kids With the Greatest Number of Candies.py`
- `1456. Maximum Number of Vowels in a Subs.py`
- `16. 3Sum Closest.py`
- `208. Implement Trie (Prefix Tree).py`
- `2095. Delete the Middle Node of a Linked.py`
- `222. Count Complete Tree Nodes.py`
- `328. Odd Even Linked List.py`
- `33. Search in Rotated Sorted Array.py`
- `35. Search Insert Position.py`
- `448. Find All Numbers Disappeared in an Array.py`
- `543.Diameter of Binary Tree.py`
- `605.Can Place Flowers.py`
- `724.Find Pivot Index.py`
- `83. Remove Duplicates from Sorted List.py`
- `872. Leaf-Similar Trees.py`
- `901. Online Stock Span.py`
- `leetcode.md` after `revision/tracker.md` replaces it.
- `roadmap.md` after useful links are merged into `revision/README.md`.
- `000/00000/aaaaa.md` after useful pattern notes are moved.
- `dashboard/__pycache__/fetch_leetcode.cpython-313.pyc`.
- The 109 no-slug stale records inside `dashboard/problems.json` after archiving/regenerating old dashboard JSON.

## Files That Should NOT Be Touched

- `.github/workflows/sync_leetcode.yml` during initial metadata migration
- All existing `<problem-folder>/README.md` files except by the sync tool
- All existing `<problem-folder>/solution.*` files except by the sync tool or explicit solution work
- `dashboard/.env`
- `LICENSE`
- `.git/ internals`

## Architecture Risks

- The biggest risk is using folder numeric prefixes as frontend LC IDs; 125 mismatches were observed.
- `dashboard/problems.json` mixes actual API records with stale folder-derived rows, so naive reuse will duplicate or mislabel problems.
- Future sync runs can add new root folders; the indexer must mark them unclassified instead of assuming a fixed set.
- Generated `README.md` and `solution.*` may be overwritten; custom notes should live in `REVISION.md` and generated `revision/` pages.
- Pattern classification should follow the saved solution approach, not only LeetCode tags.
- SQL, pandas database solutions, beginner JavaScript-style problems, and concurrency problems need taxonomy buckets outside pure DSA.
- The dashboard should become a consumer of revision metadata, not a competing source of truth.
- Category C legacy files are valuable alternate approaches; deleting them would reduce revision value.

## Final Notes

- This audit intentionally did not implement scripts or revision folders.
- This audit intentionally did not commit or push.
- Before migration, decide whether scope is 334 physical folders only or all 543 solved records with code including dashboard-only entries.
