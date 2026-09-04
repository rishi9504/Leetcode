---
leetcode_id: 347
sync_id: "0347"
title: "Top K Frequent Elements"
slug: "top-k-frequent-elements"
difficulty: "Medium"
topics: ["Array", "Hash Table", "Heap"]
current_approach: "Frequency Map and Bucket Sort"
target_pattern: "Heap / Priority Queue"
pattern_variant: "Heap / Priority Queue"
secondary_patterns: ["Hashing", "Divide and Conquer", "Sorting", "Counting", "Quickselect"]
solution_quality: "alternate_approach"
confidence: "yellow"
last_revised: null
redo: true
---

# 347. Top K Frequent Elements

## Recognition

Repeatedly needing the next smallest/largest item or a bounded top-k set suggests a heap. This problem uses the **Heap / Priority Queue** variant.

## Current Approach

The saved solution uses **Frequency Map and Bucket Sort**.

## Interview Approach

Know **Heap / Priority Queue** with **Heap / Priority Queue**. The saved implementation is a valid alternate approach, but compare its tradeoffs with the target technique.

## Core Mental Model

Keep only candidates that can still affect the answer and let the heap expose the next one.

## Complexity

### Current Solution

Time: O(n log k) for a bounded heap
Space: O(k)

### Target Interview Approach

Time: O(n log k)
Space: O(k)

## Common Mistake

Confirm whether the heap should contain k items or all active items.

## What I Should Remember

- Recognition: Repeatedly needing the next smallest/largest item or a bounded top-k set suggests a heap.
- Target: Heap / Priority Queue - Heap / Priority Queue.

## Redo Test

Can I derive the target interview approach without looking at code?
