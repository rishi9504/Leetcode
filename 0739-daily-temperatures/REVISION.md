---
leetcode_id: 739
sync_id: "0739"
title: "Daily Temperatures"
slug: "daily-temperatures"
difficulty: "Medium"
topics: ["Array", "Stack"]
current_approach: "Monotonic Stack with Debug Output"
target_pattern: "Monotonic Stack / Queue"
pattern_variant: "Next Warmer Day"
secondary_patterns: ["Stack"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 739. Daily Temperatures

## Recognition

Nearest greater/smaller queries or dominated candidates suggest a monotonic structure. This problem uses the **Next Warmer Day** variant.

## Current Approach

The saved solution uses **Monotonic Stack with Debug Output**.

## Interview Approach

Re-derive **Monotonic Stack / Queue** with **Next Warmer Day** and test it carefully. The monotonic-stack logic is appropriate, but an active print runs whenever a warmer day resolves an index.

## Core Mental Model

Discard entries that can never answer a future query while preserving useful order.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

### Target Interview Approach

Time: O(n) amortized
Space: O(n)

## Common Mistake

Store indices when distance or expiry matters.

## What I Should Remember

- Recognition: Nearest greater/smaller queries or dominated candidates suggest a monotonic structure.
- Target: Monotonic Stack / Queue - Next Warmer Day.

## Redo Test

Can I derive the target interview approach without looking at code?
