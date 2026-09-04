---
leetcode_id: 349
sync_id: "0349"
title: "Intersection of Two Arrays"
slug: "intersection-of-two-arrays"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
current_approach: "Built-in Set Intersection"
target_pattern: "Hashing"
pattern_variant: "Hash-Set Membership"
secondary_patterns: ["Two Pointers", "Binary Search", "Sorting"]
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 349. Intersection of Two Arrays

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Hash-Set Membership** variant.

## Current Approach

The saved solution uses **Built-in Set Intersection**.

## Interview Approach

Implement **Hashing** with **Hash-Set Membership** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Store exactly the state needed to turn a repeated search into an average O(1) lookup.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

### Target Interview Approach

Time: O(n) expected
Space: O(n)

## Common Mistake

Define what each key and value mean before updating the map.

## What I Should Remember

- Recognition: Fast membership, frequency, or complement lookup is the central clue.
- Target: Hashing - Hash-Set Membership.

## Redo Test

Can I derive the target interview approach without looking at code?
