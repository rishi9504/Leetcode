---
leetcode_id: 617
sync_id: "0617"
title: "Merge Two Binary Trees"
slug: "merge-two-binary-trees"
difficulty: "Easy"
topics: ["Binary Tree"]
current_approach: "Recursive Pairwise Merge"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Recursive Pairwise Merge"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 617. Merge Two Binary Trees

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Recursive Pairwise Merge** variant.

## Current Approach

The saved solution uses **Recursive Pairwise Merge**.

## Interview Approach

Use **Tree DFS / Recursion** with **Recursive Pairwise Merge**. The saved implementation already demonstrates this approach.

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
- Target: Tree DFS / Recursion - Recursive Pairwise Merge.

## Redo Test

Can I derive the target interview approach without looking at code?
