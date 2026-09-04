---
leetcode_id: 605
sync_id: "0605"
title: "Can Place Flowers"
slug: "can-place-flowers"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Local Neighbor Feasibility"
target_pattern: "Greedy"
pattern_variant: "Local Neighbor Feasibility"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 605. Can Place Flowers

## Recognition

A locally best choice can be proven to leave an equivalent smaller problem. This problem uses the **Local Neighbor Feasibility** variant.

## Current Approach

The saved solution uses **Local Neighbor Feasibility**.

Plant only when both existing neighbors are empty, and mutate the bed so later checks see the new flower.

## Interview Approach

Use **Greedy** with **Local Neighbor Feasibility**. The saved implementation already demonstrates this approach.

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
- Target: Greedy - Local Neighbor Feasibility.

## Redo Test

Can I derive the target interview approach without looking at code?
