---
leetcode_id: 290
sync_id: "0290"
title: "Word Pattern"
slug: "word-pattern"
difficulty: "Easy"
topics: ["Hash Table", "String"]
current_approach: "First-Occurrence Index Comparison"
target_pattern: "Hashing"
pattern_variant: "Bijection Maps"
secondary_patterns: []
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 290. Word Pattern

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Bijection Maps** variant.

## Current Approach

The saved solution uses **First-Occurrence Index Comparison**.

## Interview Approach

Use **Hashing** with **Bijection Maps**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Store exactly the state needed to turn a repeated search into an average O(1) lookup.

## Complexity

### Current Solution

Time: O(n^2)
Space: O(n)

### Target Interview Approach

Time: O(n)
Space: O(n)

## Common Mistake

Define what each key and value mean before updating the map.

## What I Should Remember

- Recognition: Fast membership, frequency, or complement lookup is the central clue.
- Target: Hashing - Bijection Maps.

## Redo Test

Can I derive the target interview approach without looking at code?
