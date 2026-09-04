---
leetcode_id: 821
sync_id: "0841"
title: "Shortest Distance to a Character"
slug: "shortest-distance-to-a-character"
difficulty: "Easy"
topics: ["Array", "String"]
current_approach: "Store Every Target Position, Then Sweep"
target_pattern: "Two Pointers"
pattern_variant: "Two Pointers"
secondary_patterns: []
solution_quality: "alternate_approach"
confidence: "yellow"
last_revised: null
redo: true
---

# 821. Shortest Distance to a Character

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Two Pointers** variant.

## Current Approach

The saved solution uses **Store Every Target Position, Then Sweep**.

## Interview Approach

Know **Two Pointers** with **Two Pointers**. The saved implementation is a valid alternate approach, but compare its tradeoffs with the target technique.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

### Target Interview Approach

Time: O(n), after any required sorting
Space: O(1) auxiliary

## Common Mistake

Do not move both pointers until the invariant justifies it.

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Two Pointers.

## Redo Test

Can I derive the target interview approach without looking at code?
