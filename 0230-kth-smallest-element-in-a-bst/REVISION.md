---
leetcode_id: 230
sync_id: "0230"
title: "Kth Smallest Element in a BST"
slug: "kth-smallest-element-in-a-bst"
difficulty: "Medium"
topics: ["BST", "Binary Tree"]
current_approach: "Full Reverse-Inorder List Materialization"
target_pattern: "BST"
pattern_variant: "Early-Stopping Inorder Traversal"
secondary_patterns: ["DFS"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 230. Kth Smallest Element in a BST

## Recognition

Ordered left/right subtrees allow pruning or sorted inorder traversal. This problem uses the **Early-Stopping Inorder Traversal** variant.

## Current Approach

The saved solution uses **Full Reverse-Inorder List Materialization**.

## Interview Approach

Use **BST** with **Early-Stopping Inorder Traversal**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Use BST ordering to avoid searching branches that cannot contain the answer.

## Complexity

### Current Solution

Time: O(n)
Space: O(h) recursion or O(w) queue/storage

### Target Interview Approach

Time: O(h), or O(n) when traversal is required
Space: O(h)

## Common Mistake

Carry strict bounds when duplicates are not allowed.

## What I Should Remember

- Recognition: Ordered left/right subtrees allow pruning or sorted inorder traversal.
- Target: BST - Early-Stopping Inorder Traversal.

## Redo Test

Can I derive the target interview approach without looking at code?
