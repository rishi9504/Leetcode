---
leetcode_id: 26
sync_id: "0026"
title: "Remove Duplicates from Sorted Array"
slug: "remove-duplicates-from-sorted-array"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Set Conversion Followed by Sorting"
target_pattern: "Two Pointers"
pattern_variant: "Write Pointer"
secondary_patterns: []
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 26. Remove Duplicates from Sorted Array

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Write Pointer** variant.

## Current Approach

The saved solution uses **Set Conversion Followed by Sorting**.

## Interview Approach

Implement **Two Pointers** with **Write Pointer** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(n log n)
Space: O(n)

### Target Interview Approach

Time: O(n)
Space: O(1)

## Common Mistake

Do not move both pointers until the invariant justifies it.

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Write Pointer.

## Redo Test

Can I derive the target interview approach without looking at code?
