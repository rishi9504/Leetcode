---
leetcode_id: 350
sync_id: "0350"
title: "Intersection of Two Arrays II"
slug: "intersection-of-two-arrays-ii"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
current_approach: "Sort and Two Pointers with an Active Delay"
target_pattern: "Two Pointers"
pattern_variant: "Sort and Merge"
secondary_patterns: ["Binary Search", "Sorting"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 350. Intersection of Two Arrays II

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Sort and Merge** variant.

## Current Approach

The saved solution uses **Sort and Two Pointers with an Active Delay**.

## Interview Approach

Re-derive **Two Pointers** with **Sort and Merge** and test it carefully. The merge logic is appropriate, but an active `time.sleep(0.1)` artificially delays every call.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(n log n + m log m), plus an artificial delay
Space: O(1) excluding output

### Target Interview Approach

Time: O(n + m)
Space: O(min(n, m))

## Common Mistake

Do not move both pointers until the invariant justifies it.

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Sort and Merge.

## Redo Test

Can I derive the target interview approach without looking at code?
