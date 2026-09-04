---
leetcode_id: 1721
sync_id: "0528"
title: "Swapping Nodes in a Linked List"
slug: "swapping-nodes-in-a-linked-list"
difficulty: "Medium"
topics: ["Linked List"]
current_approach: "Length Count Followed by a Second Traversal"
target_pattern: "Linked List Techniques"
pattern_variant: "Fast & Slow Pointers"
secondary_patterns: ["Two Pointers"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 1721. Swapping Nodes in a Linked List

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Fast & Slow Pointers** variant.

## Current Approach

The saved solution uses **Length Count Followed by a Second Traversal**.

## Interview Approach

Use **Linked List Techniques** with **Fast & Slow Pointers**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Name the predecessor/current/successor roles and change links in a lossless order.

## Complexity

### Current Solution

Time: O(n) in two passes
Space: O(1)

### Target Interview Approach

Time: O(n) in one pass
Space: O(1)

## Common Mistake

A dummy node often removes special handling at the head.

## What I Should Remember

- Recognition: Pointer rewiring, relative positions, or cycle structure is the main signal.
- Target: Linked List Techniques - Fast & Slow Pointers.

## Redo Test

Can I derive the target interview approach without looking at code?
