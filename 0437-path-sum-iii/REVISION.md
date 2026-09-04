---
leetcode_id: 437
sync_id: "0437"
title: "Path Sum III"
slug: "path-sum-iii"
difficulty: "Medium"
topics: ["Binary Tree"]
current_approach: "Prefix Sum"
target_pattern: "Prefix Sum / Prefix-Suffix"
pattern_variant: "Prefix Sum"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 437. Path Sum III

## Recognition

Repeated range totals or information from both sides suggests precomputed aggregates. This problem uses the **Prefix Sum** variant.

## Current Approach

The saved solution uses **Prefix Sum**.

## Interview Approach

Use **Prefix Sum / Prefix-Suffix** with **Prefix Sum**. The saved implementation already demonstrates this approach.

## Core Mental Model

Carry left-side state forward and combine it with right-side state at each position.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Be precise about whether the current element is included in each aggregate.

## What I Should Remember

- Recognition: Repeated range totals or information from both sides suggests precomputed aggregates.
- Target: Prefix Sum / Prefix-Suffix - Prefix Sum.

## Redo Test

Can I derive the target interview approach without looking at code?
