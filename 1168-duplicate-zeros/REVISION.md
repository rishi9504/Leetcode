---
leetcode_id: 1089
sync_id: "1168"
title: "Duplicate Zeros"
slug: "duplicate-zeros"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Repeated List Insert and Pop"
target_pattern: "Two Pointers"
pattern_variant: "Two Pointers"
secondary_patterns: []
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 1089. Duplicate Zeros

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Two Pointers** variant.

## Current Approach

The saved solution uses **Repeated List Insert and Pop**.

## Interview Approach

Use **Two Pointers** with **Two Pointers**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(n^2) worst case
Space: O(1)

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
