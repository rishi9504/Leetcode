---
leetcode_id: 110
sync_id: "0110"
title: "Balanced Binary Tree"
slug: "balanced-binary-tree"
difficulty: "Easy"
topics: ["Binary Tree"]
current_approach: "Postorder DFS Returning Subtree Information"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Postorder Height Sentinel"
secondary_patterns: ["DFS"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 110. Balanced Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Postorder Height Sentinel** variant.

## Current Approach

The saved solution uses **Postorder DFS Returning Subtree Information**.

## Interview Approach

Re-derive **Tree DFS / Recursion** with **Postorder Height Sentinel** and test it carefully. The saved public boolean method doubles as a height-returning helper, relying on integer truthiness instead of returning an explicit boolean.

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
- Target: Tree DFS / Recursion - Postorder Height Sentinel.

## Redo Test

Can I derive the target interview approach without looking at code?
