---
leetcode_id: 22
sync_id: "0022"
title: "Generate Parentheses"
slug: "generate-parentheses"
difficulty: "Medium"
topics: ["String"]
current_approach: "Backtracking into a Set"
target_pattern: "Backtracking"
pattern_variant: "Balanced Choice Counts"
secondary_patterns: ["Dynamic Programming"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 22. Generate Parentheses

## Recognition

The answer requires enumerating constrained choices and undoing them. This problem uses the **Balanced Choice Counts** variant.

## Current Approach

The saved solution uses **Backtracking into a Set**.

## Interview Approach

Re-derive **Backtracking** with **Balanced Choice Counts** and test it carefully. The recursive choices are sound, but the public method returns a set despite its list return contract.

## Core Mental Model

Choose, recurse, and undo while pruning branches that cannot lead to a valid answer.

## Complexity

### Current Solution

Time: Exponential in the decision depth
Space: O(decision depth), excluding output

### Target Interview Approach

Time: Exponential in the decision depth
Space: O(decision depth)

## Common Mistake

Restore every mutable choice before returning.

## What I Should Remember

- Recognition: The answer requires enumerating constrained choices and undoing them.
- Target: Backtracking - Balanced Choice Counts.

## Redo Test

Can I derive the target interview approach without looking at code?
