---
leetcode_id: 530
sync_id: "0530"
title: "Minimum Absolute Difference in BST"
slug: "minimum-absolute-difference-in-bst"
difficulty: "Easy"
topics: ["BST", "Binary Tree"]
current_approach: "Inorder Previous Value"
target_pattern: "BST"
pattern_variant: "Inorder Previous Value"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 530. Minimum Absolute Difference in BST

## Recognition

Ordered left/right subtrees allow pruning or sorted inorder traversal. This problem uses the **Inorder Previous Value** variant.

## Current Approach

The saved solution uses **Inorder Previous Value**.

## Interview Approach

Use **BST** with **Inorder Previous Value**. The saved implementation already demonstrates this approach.

## Core Mental Model

Use BST ordering to avoid searching branches that cannot contain the answer.

## Complexity

### Current Solution

Time: O(n)
Space: O(h) recursion or O(w) queue/storage

## Common Mistake

Carry strict bounds when duplicates are not allowed.

## What I Should Remember

- Recognition: Ordered left/right subtrees allow pruning or sorted inorder traversal.
- Target: BST - Inorder Previous Value.

## Redo Test

Can I derive the target interview approach without looking at code?
