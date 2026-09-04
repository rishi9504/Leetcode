---
leetcode_id: 342
sync_id: "0342"
title: "Power of Four"
slug: "power-of-four"
difficulty: "Easy"
topics: ["Math", "Bit Manipulation"]
current_approach: "Floating-Point Logarithm Check"
target_pattern: "Bit Manipulation"
pattern_variant: "Power-of-Two and Bit-Position Test"
secondary_patterns: ["Math"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 342. Power of Four

## Recognition

Parity, masks, powers of two, or cancellation identities suggest bit operations. This problem uses the **Power-of-Two and Bit-Position Test** variant.

## Current Approach

The saved solution uses **Floating-Point Logarithm Check**.

## Interview Approach

Re-derive **Bit Manipulation** with **Power-of-Two and Bit-Position Test** and test it carefully. The saved code calls an unimported `log` name and also relies on a fragile floating-point integer test.

## Core Mental Model

Treat each bit position independently or exploit an identity such as x & (x - 1).

## Complexity

### Current Solution

Time: O(1) if the logarithm call succeeds
Space: O(1)

### Target Interview Approach

Time: O(1)
Space: O(1)

## Common Mistake

Remember Python's behavior for negative and unbounded integers.

## What I Should Remember

- Recognition: Parity, masks, powers of two, or cancellation identities suggest bit operations.
- Target: Bit Manipulation - Power-of-Two and Bit-Position Test.

## Redo Test

Can I derive the target interview approach without looking at code?
