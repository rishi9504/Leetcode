---
leetcode_id: 649
sync_id: "0649"
title: "Dota2 Senate"
slug: "dota2-senate"
difficulty: "Medium"
topics: ["String", "Queue"]
current_approach: "Two List Queues with pop(0) and Debug Output"
target_pattern: "Other"
pattern_variant: "Indexed Queue Simulation"
secondary_patterns: ["Greedy"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 649. Dota2 Senate

## Recognition

The problem is best recognized by its direct transformation or specialized invariant. This problem uses the **Indexed Queue Simulation** variant.

## Current Approach

The saved solution uses **Two List Queues with pop(0) and Debug Output**.

## Interview Approach

Re-derive **Other** with **Indexed Queue Simulation** and test it carefully. The saved list queues use O(n) `pop(0)` operations and print every paired senate index.

## Core Mental Model

Write the invariant in problem terms and keep each update faithful to it.

## Complexity

### Current Solution

Time: O(n^2) worst case with pop(0)
Space: O(n)

### Target Interview Approach

Time: O(n)
Space: O(n)

## Common Mistake

Avoid adding machinery that does not simplify the proof or implementation.

## What I Should Remember

- Recognition: The problem is best recognized by its direct transformation or specialized invariant.
- Target: Other - Indexed Queue Simulation.

## Redo Test

Can I derive the target interview approach without looking at code?
