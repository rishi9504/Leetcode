---
leetcode_id: 83
sync_id: "0083"
title: "Remove Duplicates from Sorted List"
slug: "remove-duplicates-from-sorted-list"
difficulty: "Easy"
topics: ["Linked List"]
current_approach: "Single-Pass Link Skipping"
target_pattern: "Linked List Techniques"
pattern_variant: "Single-Pass Link Skipping"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 83. Remove Duplicates from Sorted List

## Recognition

Pointer rewiring, relative positions, or cycle structure is the main signal. This problem uses the **Single-Pass Link Skipping** variant.

## Current Approach

The saved solution uses **Single-Pass Link Skipping**.

Sorted duplicates are adjacent, so bypass equal successors without advancing the current node.

## Interview Approach

Use **Linked List Techniques** with **Single-Pass Link Skipping**. The saved implementation already demonstrates this approach.

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
- Target: Linked List Techniques - Single-Pass Link Skipping.

## Redo Test

Can I derive the target interview approach without looking at code?
