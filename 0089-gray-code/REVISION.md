---
leetcode_id: 89
sync_id: "0089"
title: "Gray Code"
slug: "gray-code"
difficulty: "Medium"
topics: ["Math", "Bit Manipulation"]
current_approach: "Binary-to-Gray XOR Formula"
target_pattern: "Bit Manipulation"
pattern_variant: "Binary-to-Gray XOR Formula"
secondary_patterns: ["Math"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 89. Gray Code

## Recognition

Parity, masks, powers of two, or cancellation identities suggest bit operations. This problem uses the **Binary-to-Gray XOR Formula** variant.

## Current Approach

The saved solution uses **Binary-to-Gray XOR Formula**.

## Interview Approach

Use **Bit Manipulation** with **Binary-to-Gray XOR Formula**. The saved implementation already demonstrates this approach.

## Core Mental Model

Treat each bit position independently or exploit an identity such as x & (x - 1).

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Remember Python's behavior for negative and unbounded integers.

## What I Should Remember

- Recognition: Parity, masks, powers of two, or cancellation identities suggest bit operations.
- Target: Bit Manipulation - Binary-to-Gray XOR Formula.

## Redo Test

Can I derive the target interview approach without looking at code?
