---
leetcode_id: 1
sync_id: "0001"
title: "Two Sum"
slug: "two-sum"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
current_approach: "One-Pass Hash Map Complement Lookup"
target_pattern: "Hashing"
pattern_variant: "Complement Lookup"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1. Two Sum

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Complement Lookup** variant.

## Current Approach

The saved solution uses **One-Pass Hash Map Complement Lookup**.

## Interview Approach

Use **Hashing** with **Complement Lookup**. The saved implementation already demonstrates this approach.

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
- Target: Hashing - Complement Lookup.

## Redo Test

Can I derive the target interview approach without looking at code?
