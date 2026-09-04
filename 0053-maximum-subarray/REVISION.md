---
leetcode_id: 53
sync_id: "0053"
title: "Maximum Subarray"
slug: "maximum-subarray"
difficulty: "Medium"
topics: ["Array"]
current_approach: "1D Dynamic Programming"
target_pattern: "Dynamic Programming"
pattern_variant: "1D Dynamic Programming"
secondary_patterns: ["Divide and Conquer"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 53. Maximum Subarray

## Recognition

Overlapping subproblems with a small state and reusable transitions suggest DP. This problem uses the **1D Dynamic Programming** variant.

## Current Approach

The saved solution uses **1D Dynamic Programming**.

## Interview Approach

Use **Dynamic Programming** with **1D Dynamic Programming**. The saved implementation already demonstrates this approach.

## Core Mental Model

Define the state, base case, and transition before choosing memoization or tabulation.

## Complexity

### Current Solution

Time: O(n) to O(n^2), according to the transition
Space: O(n) state

## Common Mistake

Check iteration order so every dependency is already available.

## What I Should Remember

- Recognition: Overlapping subproblems with a small state and reusable transitions suggest DP.
- Target: Dynamic Programming - 1D Dynamic Programming.

## Redo Test

Can I derive the target interview approach without looking at code?
