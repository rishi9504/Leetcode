---
leetcode_id: 1372
sync_id: "1474"
title: "Longest ZigZag Path in a Binary Tree"
slug: "longest-zigzag-path-in-a-binary-tree"
difficulty: "Medium"
topics: ["Binary Tree"]
current_approach: "Postorder DFS Returning Subtree Information"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Tree Postorder / Return Information"
secondary_patterns: ["Dynamic Programming", "DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1372. Longest ZigZag Path in a Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Tree Postorder / Return Information** variant.

## Current Approach

The saved solution uses **Postorder DFS Returning Subtree Information**.

## Interview Approach

Use **Tree DFS / Recursion** with **Tree Postorder / Return Information**. The saved implementation already demonstrates this approach.

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
- Target: Tree DFS / Recursion - Tree Postorder / Return Information.

## Redo Test

Can I derive the target interview approach without looking at code?
