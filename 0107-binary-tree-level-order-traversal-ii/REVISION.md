---
leetcode_id: 107
sync_id: "0107"
title: "Binary Tree Level Order Traversal II"
slug: "binary-tree-level-order-traversal-ii"
difficulty: "Medium"
topics: ["Binary Tree"]
current_approach: "BFS"
target_pattern: "Tree BFS"
pattern_variant: "BFS"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 107. Binary Tree Level Order Traversal II

## Recognition

Level order, minimum depth, or per-level aggregation suggests breadth-first traversal. This problem uses the **BFS** variant.

## Current Approach

The saved solution uses **BFS**.

## Interview Approach

Use **Tree BFS** with **BFS**. The saved implementation already demonstrates this approach.

## Core Mental Model

Process one queue layer at a time; the queue contains the next frontier.

## Complexity

### Current Solution

Time: O(n)
Space: O(h) recursion or O(w) queue/storage

## Common Mistake

Snapshot the level size before adding children.

## What I Should Remember

- Recognition: Level order, minimum depth, or per-level aggregation suggests breadth-first traversal.
- Target: Tree BFS - BFS.

## Redo Test

Can I derive the target interview approach without looking at code?
