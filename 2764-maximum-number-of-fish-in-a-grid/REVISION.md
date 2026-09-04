---
leetcode_id: 2658
sync_id: "2764"
title: "Maximum Number of Fish in a Grid"
slug: "maximum-number-of-fish-in-a-grid"
difficulty: "Medium"
topics: ["Array", "Matrix"]
current_approach: "DFS"
target_pattern: "Matrix / Grid"
pattern_variant: "DFS"
secondary_patterns: ["BFS", "Matrix Traversal"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 2658. Maximum Number of Fish in a Grid

## Recognition

Neighbor relationships or row/column structure make the matrix itself the state space. This problem uses the **DFS** variant.

## Current Approach

The saved solution uses **DFS**.

## Interview Approach

Use **Matrix / Grid** with **DFS**. The saved implementation already demonstrates this approach.

## Core Mental Model

Map each cell operation to bounded neighbors or row/column aggregates.

## Complexity

### Current Solution

Time: O(mn)
Space: O(mn) worst case

## Common Mistake

Mark visited cells before exploring neighbors.

## What I Should Remember

- Recognition: Neighbor relationships or row/column structure make the matrix itself the state space.
- Target: Matrix / Grid - DFS.

## Redo Test

Can I derive the target interview approach without looking at code?
