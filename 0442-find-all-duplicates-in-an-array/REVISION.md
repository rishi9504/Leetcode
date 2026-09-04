---
leetcode_id: 442
sync_id: "0442"
title: "Find All Duplicates in an Array"
slug: "find-all-duplicates-in-an-array"
difficulty: "Medium"
topics: ["Array", "Hash Table"]
current_approach: "In-Place Index/Sign Marking"
target_pattern: "Other"
pattern_variant: "In-Place Sign Marking"
secondary_patterns: ["Hashing", "Sorting"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 442. Find All Duplicates in an Array

## Recognition

The problem is best recognized by its direct transformation or specialized invariant. This problem uses the **In-Place Sign Marking** variant.

## Current Approach

The saved solution uses **In-Place Index/Sign Marking**.

## Interview Approach

Use **Other** with **In-Place Sign Marking**. The saved implementation already demonstrates this approach.

## Core Mental Model

Write the invariant in problem terms and keep each update faithful to it.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Avoid adding machinery that does not simplify the proof or implementation.

## What I Should Remember

- Recognition: The problem is best recognized by its direct transformation or specialized invariant.
- Target: Other - In-Place Sign Marking.

## Redo Test

Can I derive the target interview approach without looking at code?
