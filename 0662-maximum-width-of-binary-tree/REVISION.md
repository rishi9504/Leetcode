---
leetcode_id: 662
sync_id: "0662"
title: "Maximum Width of Binary Tree"
slug: "maximum-width-of-binary-tree"
difficulty: "Medium"
topics: ["Binary Tree"]
current_approach: "DFS with Heap-Style Position Indices"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Heap-Style Position Indexing"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 662. Maximum Width of Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Heap-Style Position Indexing** variant.

## Current Approach

The saved solution uses **DFS with Heap-Style Position Indices**.

## Interview Approach

Use **Tree DFS / Recursion** with **Heap-Style Position Indexing**. The saved implementation already demonstrates this approach.

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
- Target: Tree DFS / Recursion - Heap-Style Position Indexing.

## Redo Test

Can I derive the target interview approach without looking at code?
