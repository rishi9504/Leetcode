---
leetcode_id: 222
sync_id: "0222"
title: "Count Complete Tree Nodes"
slug: "count-complete-tree-nodes"
difficulty: "Easy"
topics: ["Bit Manipulation", "Binary Tree"]
current_approach: "Breadth-First Count of Every Node"
target_pattern: "Binary Search"
pattern_variant: "Complete-Tree Height Counting"
secondary_patterns: ["Bit Manipulation"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 222. Count Complete Tree Nodes

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Complete-Tree Height Counting** variant.

## Current Approach

The saved solution uses **Breadth-First Count of Every Node**.

The saved BFS counts every node, while the target uses equal subtree heights to count perfect portions without visiting them.

## Interview Approach

Use **Binary Search** with **Complete-Tree Height Counting**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(n)
Space: O(n)

### Target Interview Approach

Time: O(log^2 n)
Space: O(log n)

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Complete-Tree Height Counting.

## Redo Test

Can I derive the target interview approach without looking at code?
