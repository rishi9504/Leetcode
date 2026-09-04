---
leetcode_id: 16
sync_id: "0016"
title: "3Sum Closest"
slug: "3sum-closest"
difficulty: "Medium"
topics: ["Array"]
current_approach: "Sorted Outer Loop with Opposing Pointers"
target_pattern: "Two Pointers"
pattern_variant: "Sorted Outer Loop with Opposing Pointers"
secondary_patterns: ["Sorting"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 16. 3Sum Closest

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Sorted Outer Loop with Opposing Pointers** variant.

## Current Approach

The saved solution uses **Sorted Outer Loop with Opposing Pointers**.

Sort first; for each fixed value, move the two inner pointers according to whether the sum is below or above the target.

## Interview Approach

Use **Two Pointers** with **Sorted Outer Loop with Opposing Pointers**. The saved implementation already demonstrates this approach.

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
- Target: Two Pointers - Sorted Outer Loop with Opposing Pointers.

## Redo Test

Can I derive the target interview approach without looking at code?
