---
leetcode_id: 419
sync_id: "0419"
title: "Battleships in a Board"
slug: "battleships-in-a-board"
difficulty: "Medium"
topics: ["Array", "Matrix"]
current_approach: "Matrix Traversal"
target_pattern: "Matrix / Grid"
pattern_variant: "Matrix Traversal"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 419. Battleships in a Board

## Recognition

Neighbor relationships or row/column structure make the matrix itself the state space. This problem uses the **Matrix Traversal** variant.

## Current Approach

The saved solution uses **Matrix Traversal**.

## Interview Approach

Use **Matrix / Grid** with **Matrix Traversal**. The saved implementation already demonstrates this approach.

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
- Target: Matrix / Grid - Matrix Traversal.

## Redo Test

Can I derive the target interview approach without looking at code?
