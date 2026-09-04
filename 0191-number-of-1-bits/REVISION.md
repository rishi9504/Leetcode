---
leetcode_id: 191
sync_id: "0191"
title: "Number of 1 Bits"
slug: "number-of-1-bits"
difficulty: "Easy"
topics: ["Bit Manipulation"]
current_approach: "bin() String Conversion and Counting"
target_pattern: "Bit Manipulation"
pattern_variant: "Brian Kernighan Bit Clearing"
secondary_patterns: ["Divide and Conquer"]
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 191. Number of 1 Bits

## Recognition

Parity, masks, powers of two, or cancellation identities suggest bit operations. This problem uses the **Brian Kernighan Bit Clearing** variant.

## Current Approach

The saved solution uses **bin() String Conversion and Counting**.

## Interview Approach

Implement **Bit Manipulation** with **Brian Kernighan Bit Clearing** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Treat each bit position independently or exploit an identity such as x & (x - 1).

## Complexity

### Current Solution

Time: O(w)
Space: O(w)

### Target Interview Approach

Time: O(k) set bits
Space: O(1)

## Common Mistake

Remember Python's behavior for negative and unbounded integers.

## What I Should Remember

- Recognition: Parity, masks, powers of two, or cancellation identities suggest bit operations.
- Target: Bit Manipulation - Brian Kernighan Bit Clearing.

## Redo Test

Can I derive the target interview approach without looking at code?
