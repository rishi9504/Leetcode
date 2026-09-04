---
leetcode_id: 2095
sync_id: "2216"
title: "Delete the Middle Node of a Linked List"
slug: "delete-the-middle-node-of-a-linked-list"
difficulty: "Medium"
topics: ["Linked List"]
current_approach: "Fast and Slow Pointers"
target_pattern: "Linked List Techniques"
pattern_variant: "Fast and Slow Pointers with Predecessor"
secondary_patterns: ["Two Pointers"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 2095. Delete the Middle Node of a Linked List

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Fast and Slow Pointers with Predecessor** variant.

## Current Approach

The saved solution uses **Fast and Slow Pointers**.

When the fast pointer reaches the end, keep the slow pointer positioned at the predecessor of the middle node.

## Interview Approach

Use **Linked List Techniques** with **Fast and Slow Pointers with Predecessor**. The saved implementation already demonstrates this approach.

## Core Mental Model

Name the predecessor/current/successor roles and change links in a lossless order.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

A dummy node often removes special handling at the head.

## What I Should Remember

- Recognition: Pointer rewiring, relative positions, or cycle structure is the main signal.
- Target: Linked List Techniques - Fast and Slow Pointers with Predecessor.

## Redo Test

Can I derive the target interview approach without looking at code?
