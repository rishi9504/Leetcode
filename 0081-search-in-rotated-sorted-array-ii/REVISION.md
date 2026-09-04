---
leetcode_id: 81
sync_id: "0081"
title: "Search in Rotated Sorted Array II"
slug: "search-in-rotated-sorted-array-ii"
difficulty: "Medium"
topics: ["Array"]
current_approach: "Python Linear Membership Test"
target_pattern: "Binary Search"
pattern_variant: "Duplicate-Aware Rotated Search"
secondary_patterns: []
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 81. Search in Rotated Sorted Array II

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Duplicate-Aware Rotated Search** variant.

## Current Approach

The saved solution uses **Python Linear Membership Test**.

## Interview Approach

Implement **Binary Search** with **Duplicate-Aware Rotated Search** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(n)
Space: O(1)

### Target Interview Approach

Time: O(log n) average, O(n) worst case with duplicates
Space: O(1)

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## Alternative Approaches

- [Duplicate-aware binary search](alternatives/duplicate-aware-binary-search.py)

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Duplicate-Aware Rotated Search.

## Redo Test

Can I derive the target interview approach without looking at code?
