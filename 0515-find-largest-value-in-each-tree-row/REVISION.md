---
leetcode_id: 515
sync_id: "0515"
title: "Find Largest Value in Each Tree Row"
slug: "find-largest-value-in-each-tree-row"
difficulty: "Medium"
topics: ["Binary Tree"]
current_approach: "List-Based BFS with pop(0)"
target_pattern: "Tree BFS"
pattern_variant: "BFS"
secondary_patterns: ["DFS"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 515. Find Largest Value in Each Tree Row

## Recognition

Level order, minimum depth, or per-level aggregation suggests breadth-first traversal. This problem uses the **BFS** variant.

## Current Approach

The saved solution uses **List-Based BFS with pop(0)**.

## Interview Approach

Use **Tree BFS** with **BFS**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Process one queue layer at a time; the queue contains the next frontier.

## Complexity

### Current Solution

Time: O(n^2) worst case with pop(0)
Space: O(w)

### Target Interview Approach

Time: O(n)
Space: O(w)

## Common Mistake

Snapshot the level size before adding children.

## What I Should Remember

- Recognition: Level order, minimum depth, or per-level aggregation suggests breadth-first traversal.
- Target: Tree BFS - BFS.

## Redo Test

Can I derive the target interview approach without looking at code?
