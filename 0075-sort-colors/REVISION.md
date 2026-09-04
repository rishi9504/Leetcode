---
leetcode_id: 75
sync_id: "0075"
title: "Sort Colors"
slug: "sort-colors"
difficulty: "Medium"
topics: ["Array"]
current_approach: "Dutch National Flag Three-Way Partition"
target_pattern: "Two Pointers"
pattern_variant: "Partitioning / Dutch National Flag"
secondary_patterns: ["Sorting"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 75. Sort Colors

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Partitioning / Dutch National Flag** variant.

## Current Approach

The saved solution uses **Dutch National Flag Three-Way Partition**.

## Interview Approach

Use **Two Pointers** with **Partitioning / Dutch National Flag**. The saved implementation already demonstrates this approach.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Do not move both pointers until the invariant justifies it.

## Alternative Approaches

- [Counting passes](alternatives/counting-passes.py)

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Partitioning / Dutch National Flag.

## Redo Test

Can I derive the target interview approach without looking at code?
