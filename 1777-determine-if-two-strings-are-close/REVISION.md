---
leetcode_id: 1657
sync_id: "1777"
title: "Determine if Two Strings Are Close"
slug: "determine-if-two-strings-are-close"
difficulty: "Medium"
topics: ["Hash Table", "String"]
current_approach: "Counting"
target_pattern: "Hashing"
pattern_variant: "Counting"
secondary_patterns: ["Sorting"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1657. Determine if Two Strings Are Close

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Counting** variant.

## Current Approach

The saved solution uses **Counting**.

## Interview Approach

Use **Hashing** with **Counting**. The saved implementation already demonstrates this approach.

## Core Mental Model

Store exactly the state needed to turn a repeated search into an average O(1) lookup.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Define what each key and value mean before updating the map.

## What I Should Remember

- Recognition: Fast membership, frequency, or complement lookup is the central clue.
- Target: Hashing - Counting.

## Redo Test

Can I derive the target interview approach without looking at code?
