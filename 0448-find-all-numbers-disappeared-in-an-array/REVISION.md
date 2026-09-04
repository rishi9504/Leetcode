---
leetcode_id: 448
sync_id: "0448"
title: "Find All Numbers Disappeared in an Array"
slug: "find-all-numbers-disappeared-in-an-array"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
current_approach: "Built-in Set Difference"
target_pattern: "Other"
pattern_variant: "In-Place Index Marking"
secondary_patterns: []
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 448. Find All Numbers Disappeared in an Array

## Recognition

The problem is best recognized by its direct transformation or specialized invariant. This problem uses the **In-Place Index Marking** variant.

## Current Approach

The saved solution uses **Built-in Set Difference**.

The target in-place method uses each value as an index marker, then reports positions that were never marked.

## Interview Approach

Re-derive **Other** with **In-Place Index Marking** and test it carefully. The saved set-difference shortcut uses O(n) extra space and returns a set instead of the annotated list type.

## Core Mental Model

Write the invariant in problem terms and keep each update faithful to it.

## Complexity

### Current Solution

Time: O(n)
Space: O(n)

### Target Interview Approach

Time: O(n)
Space: O(1) auxiliary excluding output

## Common Mistake

Avoid adding machinery that does not simplify the proof or implementation.

## What I Should Remember

- Recognition: The problem is best recognized by its direct transformation or specialized invariant.
- Target: Other - In-Place Index Marking.

## Redo Test

Can I derive the target interview approach without looking at code?
