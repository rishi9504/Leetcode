---
leetcode_id: 268
sync_id: "0268"
title: "Missing Number"
slug: "missing-number"
difficulty: "Easy"
topics: ["Array", "Hash Table", "Math", "Bit Manipulation"]
current_approach: "Expected Sum Minus Actual Sum"
target_pattern: "Bit Manipulation"
pattern_variant: "Bit Manipulation"
secondary_patterns: ["Hashing", "Math", "Binary Search", "Sorting"]
solution_quality: "alternate_approach"
confidence: "yellow"
last_revised: null
redo: true
---

# 268. Missing Number

## Recognition

Parity, masks, powers of two, or cancellation identities suggest bit operations. This problem uses the **Bit Manipulation** variant.

## Current Approach

The saved solution uses **Expected Sum Minus Actual Sum**.

## Interview Approach

Know **Bit Manipulation** with **Bit Manipulation**. The saved implementation is a valid alternate approach, but compare its tradeoffs with the target technique.

## Core Mental Model

Treat each bit position independently or exploit an identity such as x & (x - 1).

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

### Target Interview Approach

Time: O(word size) or O(number of set bits)
Space: O(1)

## Common Mistake

Remember Python's behavior for negative and unbounded integers.

## What I Should Remember

- Recognition: Parity, masks, powers of two, or cancellation identities suggest bit operations.
- Target: Bit Manipulation - Bit Manipulation.

## Redo Test

Can I derive the target interview approach without looking at code?
