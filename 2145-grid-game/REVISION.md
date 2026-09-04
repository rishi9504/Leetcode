---
leetcode_id: 2017
sync_id: "2145"
title: "Grid Game"
slug: "grid-game"
difficulty: "Medium"
topics: ["Array", "Matrix"]
current_approach: "Grid Dynamic Programming"
target_pattern: "Dynamic Programming"
pattern_variant: "Grid Dynamic Programming"
secondary_patterns: ["Matrix Traversal", "Prefix Sum"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 2017. Grid Game

## Recognition

Overlapping subproblems with a small state and reusable transitions suggest DP. This problem uses the **Grid Dynamic Programming** variant.

## Current Approach

The saved solution uses **Grid Dynamic Programming**.

## Interview Approach

Use **Dynamic Programming** with **Grid Dynamic Programming**. The saved implementation already demonstrates this approach.

## Core Mental Model

Define the state, base case, and transition before choosing memoization or tabulation.

## Complexity

### Current Solution

Time: O(mn)
Space: O(mn)

## Common Mistake

Check iteration order so every dependency is already available.

## What I Should Remember

- Recognition: Overlapping subproblems with a small state and reusable transitions suggest DP.
- Target: Dynamic Programming - Grid Dynamic Programming.

## Redo Test

Can I derive the target interview approach without looking at code?
