---
leetcode_id: 771
sync_id: "0782"
title: "Jewels and Stones"
slug: "jewels-and-stones"
difficulty: "Easy"
topics: ["Hash Table", "String"]
current_approach: "Membership Scan that Rebuilds the Jewel Set"
target_pattern: "Hashing"
pattern_variant: "Hashing"
secondary_patterns: []
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 771. Jewels and Stones

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Hashing** variant.

## Current Approach

The saved solution uses **Membership Scan that Rebuilds the Jewel Set**.

## Interview Approach

Use **Hashing** with **Hashing**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Store exactly the state needed to turn a repeated search into an average O(1) lookup.

## Complexity

### Current Solution

Time: O(|S| * |J|) because the set is rebuilt
Space: O(|J|)

### Target Interview Approach

Time: O(|S| + |J|)
Space: O(|J|)

## Common Mistake

Define what each key and value mean before updating the map.

## What I Should Remember

- Recognition: Fast membership, frequency, or complement lookup is the central clue.
- Target: Hashing - Hashing.

## Redo Test

Can I derive the target interview approach without looking at code?
