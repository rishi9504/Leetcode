---
leetcode_id: 42
sync_id: "0042"
title: "Trapping Rain Water"
slug: "trapping-rain-water"
difficulty: "Hard"
topics: ["Array", "Stack"]
current_approach: "Prefix and Suffix Precomputation"
target_pattern: "Prefix Sum / Prefix-Suffix"
pattern_variant: "Prefix/Suffix Precomputation"
secondary_patterns: ["Two Pointers", "Dynamic Programming", "Stack", "Monotonic Stack"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 42. Trapping Rain Water

## Recognition

Repeated range totals or information from both sides suggests precomputed aggregates. This problem uses the **Prefix/Suffix Precomputation** variant.

## Current Approach

The saved solution uses **Prefix and Suffix Precomputation**.

## Interview Approach

Use **Prefix Sum / Prefix-Suffix** with **Prefix/Suffix Precomputation**. The saved implementation already demonstrates this approach.

## Core Mental Model

Carry left-side state forward and combine it with right-side state at each position.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Be precise about whether the current element is included in each aggregate.

## What I Should Remember

- Recognition: Repeated range totals or information from both sides suggests precomputed aggregates.
- Target: Prefix Sum / Prefix-Suffix - Prefix/Suffix Precomputation.

## Redo Test

Can I derive the target interview approach without looking at code?
