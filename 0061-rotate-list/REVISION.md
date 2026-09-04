---
leetcode_id: 61
sync_id: "0061"
title: "Rotate List"
slug: "rotate-list"
difficulty: "Medium"
topics: ["Linked List"]
current_approach: "Fast and Slow Pointers"
target_pattern: "Linked List Techniques"
pattern_variant: "Fast & Slow Pointers"
secondary_patterns: ["Two Pointers"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 61. Rotate List

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Fast & Slow Pointers** variant.

## Current Approach

The saved solution uses **Fast and Slow Pointers**.

## Interview Approach

Use **Linked List Techniques** with **Fast & Slow Pointers**. The saved implementation already demonstrates this approach.

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
- Target: Linked List Techniques - Fast & Slow Pointers.

## Redo Test

Can I derive the target interview approach without looking at code?
