---
leetcode_id: 853
sync_id: "0883"
title: "Car Fleet"
slug: "car-fleet"
difficulty: "Medium"
topics: ["Array", "Stack"]
current_approach: "Monotonic Stack"
target_pattern: "Monotonic Stack / Queue"
pattern_variant: "Monotonic Stack"
secondary_patterns: ["Stack", "Sorting"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 853. Car Fleet

## Recognition

Nearest greater/smaller queries or dominated candidates suggest a monotonic structure. This problem uses the **Monotonic Stack** variant.

## Current Approach

The saved solution uses **Monotonic Stack**.

## Interview Approach

Use **Monotonic Stack / Queue** with **Monotonic Stack**. The saved implementation already demonstrates this approach.

## Core Mental Model

Discard entries that can never answer a future query while preserving useful order.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Store indices when distance or expiry matters.

## What I Should Remember

- Recognition: Nearest greater/smaller queries or dominated candidates suggest a monotonic structure.
- Target: Monotonic Stack / Queue - Monotonic Stack.

## Redo Test

Can I derive the target interview approach without looking at code?
