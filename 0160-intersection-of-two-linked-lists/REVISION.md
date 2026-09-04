---
leetcode_id: 160
sync_id: "0160"
title: "Intersection of Two Linked Lists"
slug: "intersection-of-two-linked-lists"
difficulty: "Easy"
topics: ["Hash Table", "Linked List"]
current_approach: "Two Pointers"
target_pattern: "Two Pointers"
pattern_variant: "Two Pointers"
secondary_patterns: ["Hashing"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 160. Intersection of Two Linked Lists

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Two Pointers** variant.

## Current Approach

The saved solution uses **Two Pointers**.

## Interview Approach

Use **Two Pointers** with **Two Pointers**. The saved implementation already demonstrates this approach.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Do not move both pointers until the invariant justifies it.

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Two Pointers.

## Redo Test

Can I derive the target interview approach without looking at code?
