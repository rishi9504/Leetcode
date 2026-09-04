---
leetcode_id: 2336
sync_id: "2413"
title: "Smallest Number in Infinite Set"
slug: "smallest-number-in-infinite-set"
difficulty: "Medium"
topics: ["Hash Table", "Design", "Heap"]
current_approach: "Heap / Priority Queue"
target_pattern: "Heap / Priority Queue"
pattern_variant: "Heap / Priority Queue"
secondary_patterns: ["Hashing", "Design"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 2336. Smallest Number in Infinite Set

## Recognition

Repeatedly needing the next smallest/largest item or a bounded top-k set suggests a heap. This problem uses the **Heap / Priority Queue** variant.

## Current Approach

The saved solution uses **Heap / Priority Queue**.

## Interview Approach

Use **Heap / Priority Queue** with **Heap / Priority Queue**. The saved implementation already demonstrates this approach.

## Core Mental Model

Keep only candidates that can still affect the answer and let the heap expose the next one.

## Complexity

### Current Solution

Time: O(n log k) for a bounded heap
Space: O(k)

## Common Mistake

Confirm whether the heap should contain k items or all active items.

## What I Should Remember

- Recognition: Repeatedly needing the next smallest/largest item or a bounded top-k set suggests a heap.
- Target: Heap / Priority Queue - Heap / Priority Queue.

## Redo Test

Can I derive the target interview approach without looking at code?
