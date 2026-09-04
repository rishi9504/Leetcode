---
leetcode_id: 1431
sync_id: "1528"
title: "Kids With the Greatest Number of Candies"
slug: "kids-with-the-greatest-number-of-candies"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Compare Against the Global Maximum"
target_pattern: "Other"
pattern_variant: "Compare Against the Global Maximum"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1431. Kids With the Greatest Number of Candies

## Recognition

The problem is best recognized by its direct transformation or specialized invariant. This problem uses the **Compare Against the Global Maximum** variant.

## Current Approach

The saved solution uses **Compare Against the Global Maximum**.

Compute the current maximum once, then compare every child against that threshold after adding the extra candies.

## Interview Approach

Use **Other** with **Compare Against the Global Maximum**. The saved implementation already demonstrates this approach.

## Core Mental Model

Write the invariant in problem terms and keep each update faithful to it.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Avoid adding machinery that does not simplify the proof or implementation.

## What I Should Remember

- Recognition: The problem is best recognized by its direct transformation or specialized invariant.
- Target: Other - Compare Against the Global Maximum.

## Redo Test

Can I derive the target interview approach without looking at code?
