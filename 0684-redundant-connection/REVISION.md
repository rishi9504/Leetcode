---
leetcode_id: 684
sync_id: "0684"
title: "Redundant Connection"
slug: "redundant-connection"
difficulty: "Medium"
topics: ["Graph"]
current_approach: "Incremental DFS Cycle Detection"
target_pattern: "Union Find"
pattern_variant: "Disjoint-Set Cycle Detection"
secondary_patterns: ["DFS", "BFS", "Graph Traversal"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 684. Redundant Connection

## Recognition

Repeated connectivity checks while edges are added suggest disjoint sets. This problem uses the **Disjoint-Set Cycle Detection** variant.

## Current Approach

The saved solution uses **Incremental DFS Cycle Detection**.

## Interview Approach

Use **Union Find** with **Disjoint-Set Cycle Detection**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Represent each component by a root and merge roots with compression and rank/size.

## Complexity

### Current Solution

Time: O(n^2) worst case
Space: O(n)

### Target Interview Approach

Time: O(n alpha(n))
Space: O(n)

## Common Mistake

Compare roots, not immediate parents.

## What I Should Remember

- Recognition: Repeated connectivity checks while edges are added suggest disjoint sets.
- Target: Union Find - Disjoint-Set Cycle Detection.

## Redo Test

Can I derive the target interview approach without looking at code?
