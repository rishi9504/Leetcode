---
leetcode_id: 202
sync_id: "0202"
title: "Happy Number"
slug: "happy-number"
difficulty: "Easy"
topics: ["Hash Table", "Math"]
current_approach: "String Digit Simulation with a List of Seen Values"
target_pattern: "Two Pointers"
pattern_variant: "Cycle Detection"
secondary_patterns: ["Hashing", "Math"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 202. Happy Number

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Cycle Detection** variant.

## Current Approach

The saved solution uses **String Digit Simulation with a List of Seen Values**.

## Interview Approach

Use **Two Pointers** with **Cycle Detection**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(k^2) because seen-state lookup uses a list
Space: O(k)

### Target Interview Approach

Time: O(k)
Space: O(1)

## Common Mistake

Do not move both pointers until the invariant justifies it.

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Cycle Detection.

## Redo Test

Can I derive the target interview approach without looking at code?
