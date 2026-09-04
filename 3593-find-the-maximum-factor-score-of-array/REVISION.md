---
leetcode_id: 3334
sync_id: "3593"
title: "Find the Maximum Factor Score of Array"
slug: "find-the-maximum-factor-score-of-array"
difficulty: "Medium"
topics: ["Array", "Math"]
current_approach: "Prefix/Suffix GCD with Recomputed LCM per Removal"
target_pattern: "Prefix Sum / Prefix-Suffix"
pattern_variant: "Prefix/Suffix GCD and LCM"
secondary_patterns: ["Math"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 3334. Find the Maximum Factor Score of Array

## Recognition

Repeated range totals or information from both sides suggests precomputed aggregates. This problem uses the **Prefix/Suffix GCD and LCM** variant.

## Current Approach

The saved solution uses **Prefix/Suffix GCD with Recomputed LCM per Removal**.

## Interview Approach

Use **Prefix Sum / Prefix-Suffix** with **Prefix/Suffix GCD and LCM**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Carry left-side state forward and combine it with right-side state at each position.

## Complexity

### Current Solution

Time: O(n^2 log V)
Space: O(n)

### Target Interview Approach

Time: O(n log V)
Space: O(n)

## Common Mistake

Be precise about whether the current element is included in each aggregate.

## What I Should Remember

- Recognition: Repeated range totals or information from both sides suggests precomputed aggregates.
- Target: Prefix Sum / Prefix-Suffix - Prefix/Suffix GCD and LCM.

## Redo Test

Can I derive the target interview approach without looking at code?
