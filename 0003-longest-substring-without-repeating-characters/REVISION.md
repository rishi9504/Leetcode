---
leetcode_id: 3
sync_id: "0003"
title: "Longest Substring Without Repeating Characters"
slug: "longest-substring-without-repeating-characters"
difficulty: "Medium"
topics: ["Hash Table", "String"]
current_approach: "Sliding Window"
target_pattern: "Sliding Window"
pattern_variant: "Sliding Window"
secondary_patterns: ["Hashing"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 3. Longest Substring Without Repeating Characters

## Recognition

A contiguous range with a condition that can be updated incrementally suggests a window. This problem uses the **Sliding Window** variant.

## Current Approach

The saved solution uses **Sliding Window**.

## Interview Approach

Use **Sliding Window** with **Sliding Window**. The saved implementation already demonstrates this approach.

## Core Mental Model

Expand to gain candidates; shrink only enough to restore the window invariant.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Keep counts synchronized when either boundary moves.

## What I Should Remember

- Recognition: A contiguous range with a condition that can be updated incrementally suggests a window.
- Target: Sliding Window - Sliding Window.

## Redo Test

Can I derive the target interview approach without looking at code?
