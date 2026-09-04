---
leetcode_id: 121
sync_id: "0121"
title: "Best Time to Buy and Sell Stock"
slug: "best-time-to-buy-and-sell-stock"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Greedy"
target_pattern: "Greedy"
pattern_variant: "Greedy"
secondary_patterns: ["Dynamic Programming"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 121. Best Time to Buy and Sell Stock

## Recognition

A locally best choice can be proven to leave an equivalent smaller problem. This problem uses the **Greedy** variant.

## Current Approach

The saved solution uses **Greedy**.

## Interview Approach

Use **Greedy** with **Greedy**. The saved implementation already demonstrates this approach.

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
- Target: Greedy - Greedy.

## Redo Test

Can I derive the target interview approach without looking at code?
