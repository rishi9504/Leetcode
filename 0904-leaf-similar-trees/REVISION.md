---
leetcode_id: 872
sync_id: "0904"
title: "Leaf-Similar Trees"
slug: "leaf-similar-trees"
difficulty: "Easy"
topics: ["Binary Tree"]
current_approach: "Recursive Leaf Lists with Repeated Concatenation"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Leaf Sequence Comparison"
secondary_patterns: []
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 872. Leaf-Similar Trees

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Leaf Sequence Comparison** variant.

## Current Approach

The saved solution uses **Recursive Leaf Lists with Repeated Concatenation**.

Tree shape is irrelevant once both DFS traversals produce the same left-to-right leaf sequence.

## Interview Approach

Use **Tree DFS / Recursion** with **Leaf Sequence Comparison**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Define exactly what the recursive call returns before combining child results.

## Complexity

### Current Solution

Time: O(n^2) worst case from list concatenation
Space: O(n)

### Target Interview Approach

Time: O(n)
Space: O(h + leaves)

## Common Mistake

Separate leaf/base cases from the combine step.

## What I Should Remember

- Recognition: Subtree answers combine naturally at a node, or a root-to-leaf state must be carried.
- Target: Tree DFS / Recursion - Leaf Sequence Comparison.

## Redo Test

Can I derive the target interview approach without looking at code?
