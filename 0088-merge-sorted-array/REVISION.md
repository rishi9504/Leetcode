---
leetcode_id: 88
sync_id: "0088"
title: "Merge Sorted Array"
slug: "merge-sorted-array"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Copy the Second Array, Then Sort Everything"
target_pattern: "Two Pointers"
pattern_variant: "Two Pointers"
secondary_patterns: ["Sorting"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 88. Merge Sorted Array

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Two Pointers** variant.

## Current Approach

The saved solution uses **Copy the Second Array, Then Sort Everything**.

## Interview Approach

Use **Two Pointers** with **Two Pointers**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O((m+n) log(m+n))
Space: O(1) to O(m+n), implementation-dependent

### Target Interview Approach

Time: O(m+n)
Space: O(1)

## Common Mistake

Do not move both pointers until the invariant justifies it.

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Two Pointers.

## Redo Test

Can I derive the target interview approach without looking at code?
