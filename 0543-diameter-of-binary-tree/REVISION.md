---
leetcode_id: 543
sync_id: "0543"
title: "Diameter of Binary Tree"
slug: "diameter-of-binary-tree"
difficulty: "Easy"
topics: ["Binary Tree"]
current_approach: "Postorder DFS Returning Subtree Information"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Postorder Heights Update the Diameter"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 543. Diameter of Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Postorder Heights Update the Diameter** variant.

## Current Approach

The saved solution uses **Postorder DFS Returning Subtree Information**.

Each postorder call returns a height while the best left-height plus right-height updates the diameter.

## Interview Approach

Use **Tree DFS / Recursion** with **Postorder Heights Update the Diameter**. The saved implementation already demonstrates this approach.

## Core Mental Model

Define exactly what the recursive call returns before combining child results.

## Complexity

### Current Solution

Time: O(n)
Space: O(h) recursion or O(w) queue/storage

## Common Mistake

Separate leaf/base cases from the combine step.

## What I Should Remember

- Recognition: Subtree answers combine naturally at a node, or a root-to-leaf state must be carried.
- Target: Tree DFS / Recursion - Postorder Heights Update the Diameter.

## Redo Test

Can I derive the target interview approach without looking at code?
