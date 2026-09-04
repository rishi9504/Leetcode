---
leetcode_id: 643
sync_id: "0643"
title: "Maximum Average Subarray I"
slug: "maximum-average-subarray-i"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Sliding Window"
target_pattern: "Sliding Window"
pattern_variant: "Sliding Window"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 643. Maximum Average Subarray I

## Recognition

A contiguous range with a condition that can be updated incrementally suggests a window. This problem uses the **Sliding Window** variant.

## Current Approach

The saved solution uses **Sliding Window**.

## Interview Approach

Use **Sliding Window** with **Sliding Window**. The saved implementation already demonstrates this approach.

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
- Target: Sliding Window - Sliding Window.

## Redo Test

Can I derive the target interview approach without looking at code?
