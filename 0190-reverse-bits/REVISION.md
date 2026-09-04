---
leetcode_id: 190
sync_id: "0190"
title: "Reverse Bits"
slug: "reverse-bits"
difficulty: "Easy"
topics: ["Bit Manipulation"]
current_approach: "Binary String Formatting and Reversal"
target_pattern: "Bit Manipulation"
pattern_variant: "Bit-by-Bit Fixed-Width Reversal"
secondary_patterns: ["Divide and Conquer"]
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 190. Reverse Bits

## Recognition

Parity, masks, powers of two, or cancellation identities suggest bit operations. This problem uses the **Bit-by-Bit Fixed-Width Reversal** variant.

## Current Approach

The saved solution uses **Binary String Formatting and Reversal**.

## Interview Approach

Implement **Bit Manipulation** with **Bit-by-Bit Fixed-Width Reversal** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Treat each bit position independently or exploit an identity such as x & (x - 1).

## Complexity

### Current Solution

Time: O(32)
Space: O(32)

### Target Interview Approach

Time: O(32)
Space: O(1)

## Common Mistake

Remember Python's behavior for negative and unbounded integers.

## What I Should Remember

- Recognition: Parity, masks, powers of two, or cancellation identities suggest bit operations.
- Target: Bit Manipulation - Bit-by-Bit Fixed-Width Reversal.

## Redo Test

Can I derive the target interview approach without looking at code?
