---
leetcode_id: 637
sync_id: "0637"
title: "Average of Levels in Binary Tree"
slug: "average-of-levels-in-binary-tree"
difficulty: "Easy"
topics: ["Binary Tree"]
current_approach: "Depth-First Level Sum and Count Aggregation"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Depth-Indexed Aggregation"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 637. Average of Levels in Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Depth-Indexed Aggregation** variant.

## Current Approach

The saved solution uses **Depth-First Level Sum and Count Aggregation**.

## Interview Approach

Use **Tree DFS / Recursion** with **Depth-Indexed Aggregation**. The saved implementation already demonstrates this approach.

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
- Target: Tree DFS / Recursion - Depth-Indexed Aggregation.

## Redo Test

Can I derive the target interview approach without looking at code?
