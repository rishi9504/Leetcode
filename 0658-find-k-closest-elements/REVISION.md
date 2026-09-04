---
leetcode_id: 658
sync_id: "0658"
title: "Find K Closest Elements"
slug: "find-k-closest-elements"
difficulty: "Medium"
topics: ["Array", "Heap"]
current_approach: "Shrink Opposing Ends Until k Elements Remain"
target_pattern: "Binary Search"
pattern_variant: "Binary Search for Window Start"
secondary_patterns: ["Two Pointers", "Sliding Window", "Sorting", "Heap / Priority Queue"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 658. Find K Closest Elements

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Binary Search for Window Start** variant.

## Current Approach

The saved solution uses **Shrink Opposing Ends Until k Elements Remain**.

## Interview Approach

Use **Binary Search** with **Binary Search for Window Start**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(n-k)
Space: O(1) auxiliary

### Target Interview Approach

Time: O(log(n-k) + k)
Space: O(k) output

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Binary Search for Window Start.

## Redo Test

Can I derive the target interview approach without looking at code?
