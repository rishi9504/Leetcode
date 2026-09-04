---
leetcode_id: 219
sync_id: "0219"
title: "Contains Duplicate II"
slug: "contains-duplicate-ii"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
current_approach: "Hash Map of Last-Seen Indices"
target_pattern: "Hashing"
pattern_variant: "Last-Seen Index"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 219. Contains Duplicate II

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Last-Seen Index** variant.

## Current Approach

The saved solution uses **Hash Map of Last-Seen Indices**.

## Interview Approach

Use **Hashing** with **Last-Seen Index**. The saved implementation already demonstrates this approach.

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
- Target: Hashing - Last-Seen Index.

## Redo Test

Can I derive the target interview approach without looking at code?
