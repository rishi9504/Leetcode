---
leetcode_id: 37
sync_id: "0037"
title: "Sudoku Solver"
slug: "sudoku-solver"
difficulty: "Hard"
topics: ["Array", "Hash Table", "Matrix"]
current_approach: "Backtracking"
target_pattern: "Backtracking"
pattern_variant: "Backtracking"
secondary_patterns: ["Hashing", "Matrix Traversal"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 37. Sudoku Solver

## Recognition

The answer requires enumerating constrained choices and undoing them. This problem uses the **Backtracking** variant.

## Current Approach

The saved solution uses **Backtracking**.

## Interview Approach

Use **Backtracking** with **Backtracking**. The saved implementation already demonstrates this approach.

## Core Mental Model

Choose, recurse, and undo while pruning branches that cannot lead to a valid answer.

## Complexity

### Current Solution

Time: Exponential in the decision depth
Space: O(decision depth), excluding output

## Common Mistake

Restore every mutable choice before returning.

## What I Should Remember

- Recognition: The answer requires enumerating constrained choices and undoing them.
- Target: Backtracking - Backtracking.

## Redo Test

Can I derive the target interview approach without looking at code?
