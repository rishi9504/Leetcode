---
leetcode_id: 234
sync_id: "0234"
title: "Palindrome Linked List"
slug: "palindrome-linked-list"
difficulty: "Easy"
topics: ["Linked List", "Stack"]
current_approach: "Middle Split, Reverse Second Half, and Compare"
target_pattern: "Linked List Techniques"
pattern_variant: "Reverse the Second Half"
secondary_patterns: ["Two Pointers", "Stack"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 234. Palindrome Linked List

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Reverse the Second Half** variant.

## Current Approach

The saved solution uses **Middle Split, Reverse Second Half, and Compare**.

## Interview Approach

Use **Linked List Techniques** with **Reverse the Second Half**. The saved implementation already demonstrates this approach.

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
- Target: Linked List Techniques - Reverse the Second Half.

## Redo Test

Can I derive the target interview approach without looking at code?
