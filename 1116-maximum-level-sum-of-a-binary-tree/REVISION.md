---
leetcode_id: 1161
sync_id: "1116"
title: "Maximum Level Sum of a Binary Tree"
slug: "maximum-level-sum-of-a-binary-tree"
difficulty: "Medium"
topics: ["Binary Tree"]
current_approach: "DFS Aggregation by Depth"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Depth-Indexed Aggregation"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1161. Maximum Level Sum of a Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Depth-Indexed Aggregation** variant.

## Current Approach

The saved solution uses **DFS Aggregation by Depth**.

Accumulate values by depth, then choose the earliest depth with the maximum total.

## Interview Approach

Use **Tree DFS / Recursion** with **Depth-Indexed Aggregation**. The saved implementation already demonstrates this approach.

## Core Mental Model

Define exactly what the recursive call returns before combining child results.

## Complexity

### Current Solution

Time: O(n)
Space: O(h) recursion or O(w) queue/storage

## Common Mistake

Separate leaf/base cases from the combine step.

## What I Should Remember

- Recognition: Subtree answers combine naturally at a node, or a root-to-leaf state must be carried.
- Target: Tree DFS / Recursion - Depth-Indexed Aggregation.

## Redo Test

Can I derive the target interview approach without looking at code?
