---
leetcode_id: 387
sync_id: "0387"
title: "First Unique Character in a String"
slug: "first-unique-character-in-a-string"
difficulty: "Easy"
topics: ["Hash Table", "String", "Queue"]
current_approach: "Counting"
target_pattern: "Hashing"
pattern_variant: "Counting"
secondary_patterns: ["Queue"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 387. First Unique Character in a String

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
