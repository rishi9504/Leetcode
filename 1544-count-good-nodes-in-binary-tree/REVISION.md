---
leetcode_id: 1448
sync_id: "1544"
title: "Count Good Nodes in Binary Tree"
slug: "count-good-nodes-in-binary-tree"
difficulty: "Medium"
topics: ["Binary Tree"]
current_approach: "Path Maximum"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Path Maximum"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1448. Count Good Nodes in Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Path Maximum** variant.

## Current Approach

The saved solution uses **Path Maximum**.

## Interview Approach

Use **Tree DFS / Recursion** with **Path Maximum**. The saved implementation already demonstrates this approach.

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
- Target: Tree DFS / Recursion - Path Maximum.

## Redo Test

Can I derive the target interview approach without looking at code?
