---
leetcode_id: 4
sync_id: "0004"
title: "Median of Two Sorted Arrays"
slug: "median-of-two-sorted-arrays"
difficulty: "Hard"
topics: ["Array"]
current_approach: "Partition Binary Search with Reversed Boundary Variables"
target_pattern: "Binary Search"
pattern_variant: "Partition on the Smaller Array"
secondary_patterns: ["Divide and Conquer"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 4. Median of Two Sorted Arrays

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Partition on the Smaller Array** variant.

## Current Approach

The saved solution uses **Partition Binary Search with Reversed Boundary Variables**.

## Interview Approach

Re-derive **Binary Search** with **Partition on the Smaller Array** and test it carefully. The saved code assigns left/right partition boundaries in reverse; common inputs such as `[1,2]` and `[3,4]` return the wrong result.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(log(min(m, n)))
Space: O(log(min(m, n))) recursion stack in the swap case

### Target Interview Approach

Time: O(log(min(m, n)))
Space: O(1)

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Partition on the Smaller Array.

## Redo Test

Can I derive the target interview approach without looking at code?
