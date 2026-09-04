---
leetcode_id: 128
sync_id: "0128"
title: "Longest Consecutive Sequence"
slug: "longest-consecutive-sequence"
difficulty: "Medium"
topics: ["Array", "Hash Table"]
current_approach: "Sequence-Start Hash-Set Expansion with Debug Output"
target_pattern: "Hashing"
pattern_variant: "Sequence-Start Expansion"
secondary_patterns: []
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 128. Longest Consecutive Sequence

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Sequence-Start Expansion** variant.

## Current Approach

The saved solution uses **Sequence-Start Hash-Set Expansion with Debug Output**.

Expand only from numbers whose predecessor is absent; that makes each sequence count once.

## Interview Approach

Re-derive **Hashing** with **Sequence-Start Expansion** and test it carefully. The algorithm is appropriate, but an active `print(m)` exposes the full set during execution.

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
- Target: Hashing - Sequence-Start Expansion.

## Redo Test

Can I derive the target interview approach without looking at code?
