---
leetcode_id: 236
sync_id: "0236"
title: "Lowest Common Ancestor of a Binary Tree"
slug: "lowest-common-ancestor-of-a-binary-tree"
difficulty: "Medium"
topics: ["Binary Tree"]
current_approach: "DFS"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "DFS"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 236. Lowest Common Ancestor of a Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **DFS** variant.

## Current Approach

The saved solution uses **DFS**.

## Interview Approach

Use **Tree DFS / Recursion** with **DFS**. The saved implementation already demonstrates this approach.

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
- Target: Tree DFS / Recursion - DFS.

## Redo Test

Can I derive the target interview approach without looking at code?
