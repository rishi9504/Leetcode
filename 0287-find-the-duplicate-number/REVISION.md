---
leetcode_id: 287
sync_id: "0287"
title: "Find the Duplicate Number"
slug: "find-the-duplicate-number"
difficulty: "Medium"
topics: ["Array", "Bit Manipulation"]
current_approach: "Hash Set Duplicate Detection"
target_pattern: "Two Pointers"
pattern_variant: "Floyd Cycle Detection"
secondary_patterns: ["Binary Search", "Bit Manipulation"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 287. Find the Duplicate Number

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Floyd Cycle Detection** variant.

## Current Approach

The saved solution uses **Hash Set Duplicate Detection**.

## Interview Approach

Use **Two Pointers** with **Floyd Cycle Detection**. The saved implementation is valid, but it gives up an expected time or space improvement.

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
- Target: Two Pointers - Floyd Cycle Detection.

## Redo Test

Can I derive the target interview approach without looking at code?
