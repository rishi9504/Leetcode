---
leetcode_id: 74
sync_id: "0074"
title: "Search a 2D Matrix"
slug: "search-a-2d-matrix"
difficulty: "Medium"
topics: ["Array", "Matrix"]
current_approach: "Flatten the Matrix, Then Binary Search"
target_pattern: "Binary Search"
pattern_variant: "Binary Search"
secondary_patterns: ["Matrix Traversal"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 74. Search a 2D Matrix

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Binary Search** variant.

## Current Approach

The saved solution uses **Flatten the Matrix, Then Binary Search**.

## Interview Approach

Use **Binary Search** with **Binary Search**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(mn)
Space: O(mn)

### Target Interview Approach

Time: O(log(mn))
Space: O(1)

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Binary Search.

## Redo Test

Can I derive the target interview approach without looking at code?
