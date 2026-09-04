---
leetcode_id: 328
sync_id: "0328"
title: "Odd Even Linked List"
slug: "odd-even-linked-list"
difficulty: "Medium"
topics: ["Linked List"]
current_approach: "Odd/Even Position Chains"
target_pattern: "Linked List Techniques"
pattern_variant: "Odd/Even Position Chains"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 328. Odd Even Linked List

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Odd/Even Position Chains** variant.

## Current Approach

The saved solution uses **Odd/Even Position Chains**.

Maintain separate odd-position and even-position chains, then reconnect the odd tail to the saved even head.

## Interview Approach

Use **Linked List Techniques** with **Odd/Even Position Chains**. The saved implementation already demonstrates this approach.

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
- Target: Linked List Techniques - Odd/Even Position Chains.

## Redo Test

Can I derive the target interview approach without looking at code?
