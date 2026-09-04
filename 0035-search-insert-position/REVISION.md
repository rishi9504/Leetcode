---
leetcode_id: 35
sync_id: "0035"
title: "Search Insert Position"
slug: "search-insert-position"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Lower Bound"
target_pattern: "Binary Search"
pattern_variant: "Lower Bound"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 35. Search Insert Position

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Lower Bound** variant.

## Current Approach

The saved solution uses **Lower Bound**.

The final left boundary is the first valid insertion position even when the target is absent.

## Interview Approach

Use **Binary Search** with **Lower Bound**. The saved implementation already demonstrates this approach.

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
- Target: Binary Search - Lower Bound.

## Redo Test

Can I derive the target interview approach without looking at code?
