---
leetcode_id: 1765
sync_id: "1876"
title: "Map of Highest Peak"
slug: "map-of-highest-peak"
difficulty: "Medium"
topics: ["Array", "Matrix"]
current_approach: "BFS"
target_pattern: "Matrix / Grid"
pattern_variant: "BFS"
secondary_patterns: ["Matrix Traversal"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1765. Map of Highest Peak

## Recognition

Neighbor relationships or row/column structure make the matrix itself the state space. This problem uses the **BFS** variant.

## Current Approach

The saved solution uses **BFS**.

## Interview Approach

Use **Matrix / Grid** with **BFS**. The saved implementation already demonstrates this approach.

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
- Target: Matrix / Grid - BFS.

## Redo Test

Can I derive the target interview approach without looking at code?
