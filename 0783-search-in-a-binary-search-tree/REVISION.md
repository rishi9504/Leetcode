---
leetcode_id: 700
sync_id: "0783"
title: "Search in a Binary Search Tree"
slug: "search-in-a-binary-search-tree"
difficulty: "Easy"
topics: ["BST", "Binary Tree"]
current_approach: "BST Search"
target_pattern: "BST"
pattern_variant: "BST Search"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 700. Search in a Binary Search Tree

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
