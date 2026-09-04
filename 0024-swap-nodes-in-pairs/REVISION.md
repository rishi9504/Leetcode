---
leetcode_id: 24
sync_id: "0024"
title: "Swap Nodes in Pairs"
slug: "swap-nodes-in-pairs"
difficulty: "Medium"
topics: ["Linked List"]
current_approach: "Recursive Pair Reversal"
target_pattern: "Linked List Techniques"
pattern_variant: "Recursive Pair Reversal"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 24. Swap Nodes in Pairs

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Recursive Pair Reversal** variant.

## Current Approach

The saved solution uses **Recursive Pair Reversal**.

## Interview Approach

Use **Linked List Techniques** with **Recursive Pair Reversal**. The saved implementation already demonstrates this approach.

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
- Target: Linked List Techniques - Recursive Pair Reversal.

## Redo Test

Can I derive the target interview approach without looking at code?
