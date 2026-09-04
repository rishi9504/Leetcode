---
leetcode_id: 956
sync_id: "0993"
title: "Tallest Billboard"
slug: "tallest-billboard"
difficulty: "Hard"
topics: ["Array"]
current_approach: "Difference-State Take/Skip Dynamic Programming"
target_pattern: "Dynamic Programming"
pattern_variant: "Knapsack / Take-Skip"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 956. Tallest Billboard

## Recognition

Overlapping subproblems with a small state and reusable transitions suggest DP. This problem uses the **Knapsack / Take-Skip** variant.

## Current Approach

The saved solution uses **Difference-State Take/Skip Dynamic Programming**.

## Interview Approach

Use **Dynamic Programming** with **Knapsack / Take-Skip**. The saved implementation already demonstrates this approach.

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
- Target: Dynamic Programming - Knapsack / Take-Skip.

## Redo Test

Can I derive the target interview approach without looking at code?
