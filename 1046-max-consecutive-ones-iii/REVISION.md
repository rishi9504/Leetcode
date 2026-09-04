---
leetcode_id: 1004
sync_id: "1046"
title: "Max Consecutive Ones III"
slug: "max-consecutive-ones-iii"
difficulty: "Medium"
topics: ["Array"]
current_approach: "At Most k Zeros"
target_pattern: "Sliding Window"
pattern_variant: "At Most k Zeros"
secondary_patterns: ["Binary Search", "Prefix Sum"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1004. Max Consecutive Ones III

## Recognition

A contiguous range with a condition that can be updated incrementally suggests a window. This problem uses the **At Most k Zeros** variant.

## Current Approach

The saved solution uses **At Most k Zeros**.

Treat each zero as one unit of budget and advance the left edge only when that budget is exceeded.

## Interview Approach

Use **Sliding Window** with **At Most k Zeros**. The saved implementation already demonstrates this approach.

## Core Mental Model

Expand to gain candidates; shrink only enough to restore the window invariant.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Keep counts synchronized when either boundary moves.

## What I Should Remember

- Recognition: A contiguous range with a condition that can be updated incrementally suggests a window.
- Target: Sliding Window - At Most k Zeros.

## Redo Test

Can I derive the target interview approach without looking at code?
