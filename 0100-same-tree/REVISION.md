---
leetcode_id: 100
sync_id: "0100"
title: "Same Tree"
slug: "same-tree"
difficulty: "Easy"
topics: ["Binary Tree"]
current_approach: "Lockstep Tree Comparison with Debug Output"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Lockstep Tree Comparison"
secondary_patterns: ["DFS", "BFS"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 100. Same Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Lockstep Tree Comparison** variant.

## Current Approach

The saved solution uses **Lockstep Tree Comparison with Debug Output**.

## Interview Approach

Re-derive **Tree DFS / Recursion** with **Lockstep Tree Comparison** and test it carefully. The recursive algorithm is appropriate, but an active `print(p, q)` runs on structural mismatches.

## Core Mental Model

Define exactly what the recursive call returns before combining child results.

## Complexity

### Current Solution

Time: O(n)
Space: O(h) recursion or O(w) queue/storage

### Target Interview Approach

Time: O(n)
Space: O(h)

## Common Mistake

Separate leaf/base cases from the combine step.

## What I Should Remember

- Recognition: Subtree answers combine naturally at a node, or a root-to-leaf state must be carried.
- Target: Tree DFS / Recursion - Lockstep Tree Comparison.

## Redo Test

Can I derive the target interview approach without looking at code?
