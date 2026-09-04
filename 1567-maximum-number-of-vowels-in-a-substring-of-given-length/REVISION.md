---
leetcode_id: 1456
sync_id: "1567"
title: "Maximum Number of Vowels in a Substring of Given Length"
slug: "maximum-number-of-vowels-in-a-substring-of-given-length"
difficulty: "Medium"
topics: ["String"]
current_approach: "Fixed-Size Vowel Window"
target_pattern: "Sliding Window"
pattern_variant: "Fixed-Size Vowel Window"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1456. Maximum Number of Vowels in a Substring of Given Length

## Recognition

A contiguous range with a condition that can be updated incrementally suggests a window. This problem uses the **Fixed-Size Vowel Window** variant.

## Current Approach

The saved solution uses **Fixed-Size Vowel Window**.

Update one vowel count by removing the outgoing character and adding the incoming character.

## Interview Approach

Use **Sliding Window** with **Fixed-Size Vowel Window**. The saved implementation already demonstrates this approach.

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
- Target: Sliding Window - Fixed-Size Vowel Window.

## Redo Test

Can I derive the target interview approach without looking at code?
