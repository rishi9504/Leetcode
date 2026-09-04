---
leetcode_id: 1081
sync_id: "1159"
title: "Smallest Subsequence of Distinct Characters"
slug: "smallest-subsequence-of-distinct-characters"
difficulty: "Medium"
topics: ["String", "Stack"]
current_approach: "Monotonic Stack with Repeated Linear Membership Checks"
target_pattern: "Monotonic Stack / Queue"
pattern_variant: "Monotonic Stack"
secondary_patterns: ["Stack", "Greedy"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 1081. Smallest Subsequence of Distinct Characters

## Recognition

Nearest greater/smaller queries or dominated candidates suggest a monotonic structure. This problem uses the **Monotonic Stack** variant.

## Current Approach

The saved solution uses **Monotonic Stack with Repeated Linear Membership Checks**.

## Interview Approach

Use **Monotonic Stack / Queue** with **Monotonic Stack**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Discard entries that can never answer a future query while preserving useful order.

## Complexity

### Current Solution

Time: O(n^2)
Space: O(n)

### Target Interview Approach

Time: O(n)
Space: O(alphabet size)

## Common Mistake

Store indices when distance or expiry matters.

## What I Should Remember

- Recognition: Nearest greater/smaller queries or dominated candidates suggest a monotonic structure.
- Target: Monotonic Stack / Queue - Monotonic Stack.

## Redo Test

Can I derive the target interview approach without looking at code?
