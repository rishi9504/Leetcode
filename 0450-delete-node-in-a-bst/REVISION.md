---
leetcode_id: 450
sync_id: "0450"
title: "Delete Node in a BST"
slug: "delete-node-in-a-bst"
difficulty: "Medium"
topics: ["BST", "Binary Tree"]
current_approach: "Recursive BST Deletion with Inorder Successor"
target_pattern: "BST"
pattern_variant: "Recursive BST Deletion with Inorder Successor"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 450. Delete Node in a BST

## Recognition

Ordered left/right subtrees allow pruning or sorted inorder traversal. This problem uses the **Recursive BST Deletion with Inorder Successor** variant.

## Current Approach

The saved solution uses **Recursive BST Deletion with Inorder Successor**.

## Interview Approach

Use **BST** with **Recursive BST Deletion with Inorder Successor**. The saved implementation already demonstrates this approach.

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
- Target: BST - Recursive BST Deletion with Inorder Successor.

## Redo Test

Can I derive the target interview approach without looking at code?
