---
leetcode_id: 21
sync_id: "0021"
title: "Merge Two Sorted Lists"
slug: "merge-two-sorted-lists"
difficulty: "Easy"
topics: ["Linked List"]
current_approach: "Dummy-Head Sorted Merge"
target_pattern: "Linked List Techniques"
pattern_variant: "Dummy-Head Sorted Merge"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 21. Merge Two Sorted Lists

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Dummy-Head Sorted Merge** variant.

## Current Approach

The saved solution uses **Dummy-Head Sorted Merge**.

## Interview Approach

Use **Linked List Techniques** with **Dummy-Head Sorted Merge**. The saved implementation already demonstrates this approach.

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
- Target: Linked List Techniques - Dummy-Head Sorted Merge.

## Redo Test

Can I derive the target interview approach without looking at code?
