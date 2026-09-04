---
leetcode_id: 189
sync_id: "0189"
title: "Rotate Array"
slug: "rotate-array"
difficulty: "Medium"
topics: ["Array", "Math"]
current_approach: "Array Slicing and Concatenation"
target_pattern: "Two Pointers"
pattern_variant: "Two Pointers"
secondary_patterns: ["Math"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 189. Rotate Array

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Two Pointers** variant.

## Current Approach

The saved solution uses **Array Slicing and Concatenation**.

## Interview Approach

Use **Two Pointers** with **Two Pointers**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(n)
Space: O(n)

### Target Interview Approach

Time: O(n)
Space: O(1)

## Common Mistake

Do not move both pointers until the invariant justifies it.

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Two Pointers.

## Redo Test

Can I derive the target interview approach without looking at code?
