---
leetcode_id: 19
sync_id: "0019"
title: "Remove Nth Node From End of List"
slug: "remove-nth-node-from-end-of-list"
difficulty: "Medium"
topics: ["Linked List"]
current_approach: "Length Count Followed by a Second Traversal"
target_pattern: "Linked List Techniques"
pattern_variant: "Fast and Slow Pointer Gap"
secondary_patterns: ["Two Pointers"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 19. Remove Nth Node From End of List

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Fast and Slow Pointer Gap** variant.

## Current Approach

The saved solution uses **Length Count Followed by a Second Traversal**.

## Interview Approach

Use **Linked List Techniques** with **Fast and Slow Pointer Gap**. The saved implementation is valid, but it gives up an expected time or space improvement.

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
- Target: Linked List Techniques - Fast and Slow Pointer Gap.

## Redo Test

Can I derive the target interview approach without looking at code?
