---
leetcode_id: 217
sync_id: "0217"
title: "Contains Duplicate"
slug: "contains-duplicate"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
current_approach: "Hash Set Scan with an Implicit False Return"
target_pattern: "Hashing"
pattern_variant: "Seen-Set Membership"
secondary_patterns: ["Sorting"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 217. Contains Duplicate

## Recognition

Fast membership, frequency, or complement lookup is the central clue. This problem uses the **Seen-Set Membership** variant.

## Current Approach

The saved solution uses **Hash Set Scan with an Implicit False Return**.

## Interview Approach

Re-derive **Hashing** with **Seen-Set Membership** and test it carefully. The no-duplicate path falls off the function and returns `None` instead of an explicit `False`.

## Core Mental Model

Store exactly the state needed to turn a repeated search into an average O(1) lookup.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

### Target Interview Approach

Time: O(n) expected
Space: O(n)

## Common Mistake

Define what each key and value mean before updating the map.

## What I Should Remember

- Recognition: Fast membership, frequency, or complement lookup is the central clue.
- Target: Hashing - Seen-Set Membership.

## Redo Test

Can I derive the target interview approach without looking at code?
