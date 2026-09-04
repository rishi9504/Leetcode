---
leetcode_id: 1493
sync_id: "1586"
title: "Longest Subarray of 1's After Deleting One Element"
slug: "longest-subarray-of-1s-after-deleting-one-element"
difficulty: "Medium"
topics: ["Array"]
current_approach: "At Most One Zero"
target_pattern: "Sliding Window"
pattern_variant: "At Most One Zero"
secondary_patterns: ["Dynamic Programming"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1493. Longest Subarray of 1's After Deleting One Element

## Recognition

A contiguous range with a condition that can be updated incrementally suggests a window. This problem uses the **At Most One Zero** variant.

## Current Approach

The saved solution uses **At Most One Zero**.

## Interview Approach

Use **Sliding Window** with **At Most One Zero**. The saved implementation already demonstrates this approach.

## Core Mental Model

Expand to gain candidates; shrink only enough to restore the window invariant.

## Complexity

### Current Solution

Time: O(n)
Space: O(n) or O(1) with rolling state

## Common Mistake

Keep counts synchronized when either boundary moves.

## What I Should Remember

- Recognition: A contiguous range with a condition that can be updated incrementally suggests a window.
- Target: Sliding Window - At Most One Zero.

## Redo Test

Can I derive the target interview approach without looking at code?
