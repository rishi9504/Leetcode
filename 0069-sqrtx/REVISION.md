---
leetcode_id: 69
sync_id: "0069"
title: "Sqrt(x)"
slug: "sqrtx"
difficulty: "Easy"
topics: ["Math"]
current_approach: "Linear Trial of Consecutive Integers"
target_pattern: "Binary Search"
pattern_variant: "Binary Search"
secondary_patterns: ["Math"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 69. Sqrt(x)

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Binary Search** variant.

## Current Approach

The saved solution uses **Linear Trial of Consecutive Integers**.

## Interview Approach

Use **Binary Search** with **Binary Search**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(x)
Space: O(1)

### Target Interview Approach

Time: O(log x)
Space: O(1)

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Binary Search.

## Redo Test

Can I derive the target interview approach without looking at code?
