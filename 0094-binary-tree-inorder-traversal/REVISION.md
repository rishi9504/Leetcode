---
leetcode_id: 94
sync_id: "0094"
title: "Binary Tree Inorder Traversal"
slug: "binary-tree-inorder-traversal"
difficulty: "Easy"
topics: ["Stack", "Binary Tree"]
current_approach: "Tree Traversal"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Tree Traversal"
secondary_patterns: ["Stack", "DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 94. Binary Tree Inorder Traversal

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Tree Traversal** variant.

## Current Approach

The saved solution uses **Tree Traversal**.

## Interview Approach

Use **Tree DFS / Recursion** with **Tree Traversal**. The saved implementation already demonstrates this approach.

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
- Target: Tree DFS / Recursion - Tree Traversal.

## Redo Test

Can I derive the target interview approach without looking at code?
