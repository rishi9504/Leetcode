---
leetcode_id: 111
sync_id: "0111"
title: "Minimum Depth of Binary Tree"
slug: "minimum-depth-of-binary-tree"
difficulty: "Easy"
topics: ["Binary Tree"]
current_approach: "One-Child-Aware Minimum Depth"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "One-Child-Aware Minimum Depth"
secondary_patterns: ["BFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 111. Minimum Depth of Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **One-Child-Aware Minimum Depth** variant.

## Current Approach

The saved solution uses **One-Child-Aware Minimum Depth**.

A missing child is not a zero-length route to a leaf, so a one-child node must recurse through its existing child.

## Interview Approach

Use **Tree DFS / Recursion** with **One-Child-Aware Minimum Depth**. The saved implementation already demonstrates this approach.

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
- Target: Tree DFS / Recursion - One-Child-Aware Minimum Depth.

## Redo Test

Can I derive the target interview approach without looking at code?
