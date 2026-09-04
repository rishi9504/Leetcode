---
leetcode_id: 374
sync_id: "0374"
title: "Guess Number Higher or Lower"
slug: "guess-number-higher-or-lower"
difficulty: "Easy"
topics: ["Other"]
current_approach: "Binary Search"
target_pattern: "Binary Search"
pattern_variant: "Binary Search"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 374. Guess Number Higher or Lower

## Recognition

A sorted domain or monotone yes/no predicate suggests halving the search space. This problem uses the **Binary Search** variant.

## Current Approach

The saved solution uses **Binary Search**.

## Interview Approach

Use **Binary Search** with **Binary Search**. The saved implementation already demonstrates this approach.

## Core Mental Model

Choose bounds whose meaning stays true after every update, then return the boundary requested.

## Complexity

### Current Solution

Time: O(log n), or O(log range) plus feasibility work
Space: O(1) auxiliary

## Common Mistake

Check equality, boundary movement, and the final return convention together.

## What I Should Remember

- Recognition: A sorted domain or monotone yes/no predicate suggests halving the search space.
- Target: Binary Search - Binary Search.

## Redo Test

Can I derive the target interview approach without looking at code?
