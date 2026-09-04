---
leetcode_id: 33
sync_id: "0033"
title: "Search in Rotated Sorted Array"
slug: "search-in-rotated-sorted-array"
difficulty: "Medium"
topics: ["Array"]
current_approach: "Identify the Sorted Half"
target_pattern: "Binary Search"
pattern_variant: "Identify the Sorted Half"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 33. Search in Rotated Sorted Array

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Identify the Sorted Half** variant.

## Current Approach

The saved solution uses **Identify the Sorted Half**.

At every step one half is sorted; test whether the target lies inside that half before discarding the other.

## Interview Approach

Use **Binary Search** with **Identify the Sorted Half**. The saved implementation already demonstrates this approach.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(log n), or O(log range) plus feasibility work
Space: O(1) auxiliary

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Identify the Sorted Half.

## Redo Test

Can I derive the target interview approach without looking at code?
