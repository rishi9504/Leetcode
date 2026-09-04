---
leetcode_id: 1356
sync_id: "1458"
title: "Sort Integers by The Number of 1 Bits"
slug: "sort-integers-by-the-number-of-1-bits"
difficulty: "Easy"
topics: ["Array", "Bit Manipulation"]
current_approach: "bin().count() Followed by Sorting"
target_pattern: "Bit Manipulation"
pattern_variant: "Bit Manipulation"
secondary_patterns: ["Sorting", "Counting"]
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 1356. Sort Integers by The Number of 1 Bits

## Recognition

Parity, masks, powers of two, or cancellation identities suggest bit operations. This problem uses the **Bit Manipulation** variant.

## Current Approach

The saved solution uses **bin().count() Followed by Sorting**.

## Interview Approach

Implement **Bit Manipulation** with **Bit Manipulation** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Treat each bit position independently or exploit an identity such as x & (x - 1).

## Complexity

### Current Solution

Time: O(n log n * w)
Space: O(n)

## Common Mistake

Remember Python's behavior for negative and unbounded integers.

## What I Should Remember

- Recognition: Parity, masks, powers of two, or cancellation identities suggest bit operations.
- Target: Bit Manipulation - Bit Manipulation.

## Redo Test

Can I derive the target interview approach without looking at code?
