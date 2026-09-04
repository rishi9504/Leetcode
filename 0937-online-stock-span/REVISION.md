---
leetcode_id: 901
sync_id: "0937"
title: "Online Stock Span"
slug: "online-stock-span"
difficulty: "Medium"
topics: ["Stack", "Design"]
current_approach: "Price and Aggregated Span Stack"
target_pattern: "Monotonic Stack / Queue"
pattern_variant: "Price and Aggregated Span Stack"
secondary_patterns: ["Stack", "Design", "Data Stream"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 901. Online Stock Span

## Recognition

Nearest greater/smaller queries or dominated candidates suggest a monotonic structure. This problem uses the **Price and Aggregated Span Stack** variant.

## Current Approach

The saved solution uses **Price and Aggregated Span Stack**.

Pop lower-or-equal prices and absorb their stored spans so every historical price is pushed and popped at most once.

## Interview Approach

Use **Monotonic Stack / Queue** with **Price and Aggregated Span Stack**. The saved implementation already demonstrates this approach.

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
- Target: Monotonic Stack / Queue - Price and Aggregated Span Stack.

## Redo Test

Can I derive the target interview approach without looking at code?
