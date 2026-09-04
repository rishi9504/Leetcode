---
leetcode_id: 242
sync_id: "0242"
title: "Valid Anagram"
slug: "valid-anagram"
difficulty: "Easy"
topics: ["Hash Table", "String"]
current_approach: "Hashing"
target_pattern: "Hashing"
pattern_variant: "Hashing"
secondary_patterns: ["Sorting"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 242. Valid Anagram

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Hashing** variant.

## Current Approach

The saved solution uses **Hashing**.

## Interview Approach

Use **Hashing** with **Hashing**. The saved implementation already demonstrates this approach.

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
- Target: Hashing - Hashing.

## Redo Test

Can I derive the target interview approach without looking at code?
