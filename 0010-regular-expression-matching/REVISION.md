---
leetcode_id: 10
sync_id: "0010"
title: "Regular Expression Matching"
slug: "regular-expression-matching"
difficulty: "Hard"
topics: ["String"]
current_approach: "Two-Dimensional String Dynamic Programming"
target_pattern: "Dynamic Programming"
pattern_variant: "String Dynamic Programming"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 10. Regular Expression Matching

## Recognition

Overlapping subproblems with a small state and reusable transitions suggest DP. This problem uses the **String Dynamic Programming** variant.

## Current Approach

The saved solution uses **Two-Dimensional String Dynamic Programming**.

## Interview Approach

Use **Dynamic Programming** with **String Dynamic Programming**. The saved implementation already demonstrates this approach.

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
- Target: Dynamic Programming - String Dynamic Programming.

## Redo Test

Can I derive the target interview approach without looking at code?
