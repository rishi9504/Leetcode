---
leetcode_id: 118
sync_id: "0118"
title: "Pascal's Triangle"
slug: "pascals-triangle"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Hardcoded Rows Through the Constraint Limit"
target_pattern: "Dynamic Programming"
pattern_variant: "Build Each Row from the Previous Row"
secondary_patterns: []
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 118. Pascal's Triangle

## Recognition

Overlapping subproblems with a small state and reusable transitions suggest DP. This problem uses the **Build Each Row from the Previous Row** variant.

## Current Approach

The saved solution uses **Hardcoded Rows Through the Constraint Limit**.

## Interview Approach

Implement **Dynamic Programming** with **Build Each Row from the Previous Row** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Define the state, base case, and transition before choosing memoization or tabulation.

## Complexity

### Current Solution

Time: O(r^2) to materialize the sliced literal
Space: O(r^2) output

### Target Interview Approach

Time: O(r^2)
Space: O(r^2) output

## Common Mistake

Check iteration order so every dependency is already available.

## What I Should Remember

- Recognition: Overlapping subproblems with a small state and reusable transitions suggest DP.
- Target: Dynamic Programming - Build Each Row from the Previous Row.

## Redo Test

Can I derive the target interview approach without looking at code?
