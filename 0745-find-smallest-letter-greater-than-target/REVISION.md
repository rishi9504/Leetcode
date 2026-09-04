---
leetcode_id: 744
sync_id: "0745"
title: "Find Smallest Letter Greater Than Target"
slug: "find-smallest-letter-greater-than-target"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Linear Scan with Wraparound"
target_pattern: "Binary Search"
pattern_variant: "Upper Bound with Wraparound"
secondary_patterns: []
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 744. Find Smallest Letter Greater Than Target

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Upper Bound with Wraparound** variant.

## Current Approach

The saved solution uses **Linear Scan with Wraparound**.

The target upper bound finds the first strictly greater letter and wraps to index zero when none exists.

## Interview Approach

Use **Binary Search** with **Upper Bound with Wraparound**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(n)
Space: O(1)

### Target Interview Approach

Time: O(log n)
Space: O(1)

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Upper Bound with Wraparound.

## Redo Test

Can I derive the target interview approach without looking at code?
