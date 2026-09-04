---
leetcode_id: 98
sync_id: "0098"
title: "Validate Binary Search Tree"
slug: "validate-binary-search-tree"
difficulty: "Medium"
topics: ["BST", "Binary Tree"]
current_approach: "BST Search"
target_pattern: "BST"
pattern_variant: "BST Search"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 98. Validate Binary Search Tree

## Recognition

Ordered left/right subtrees allow pruning or sorted inorder traversal. This problem uses the **BST Search** variant.

## Current Approach

The saved solution uses **BST Search**.

## Interview Approach

Use **BST** with **BST Search**. The saved implementation already demonstrates this approach.

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
- Target: BST - BST Search.

## Redo Test

Can I derive the target interview approach without looking at code?
