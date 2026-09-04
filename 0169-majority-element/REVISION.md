---
leetcode_id: 169
sync_id: "0169"
title: "Majority Element"
slug: "majority-element"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
current_approach: "Boyer-Moore Majority Vote"
target_pattern: "Greedy"
pattern_variant: "Boyer-Moore Voting"
secondary_patterns: ["Divide and Conquer", "Sorting", "Counting"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 169. Majority Element

## Recognition

A locally best choice can be proven to leave an equivalent smaller problem. This problem uses the **Boyer-Moore Voting** variant.

## Current Approach

The saved solution uses **Boyer-Moore Majority Vote**.

## Interview Approach

Use **Greedy** with **Boyer-Moore Voting**. The saved implementation already demonstrates this approach.

## Core Mental Model

Track the strongest feasible state so far and commit only when delaying cannot help.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

State the exchange or dominance argument; intuition alone is not enough.

## What I Should Remember

- Recognition: A locally best choice can be proven to leave an equivalent smaller problem.
- Target: Greedy - Boyer-Moore Voting.

## Redo Test

Can I derive the target interview approach without looking at code?
