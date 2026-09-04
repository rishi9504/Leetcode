---
leetcode_id: 14
sync_id: "0014"
title: "Longest Common Prefix"
slug: "longest-common-prefix"
difficulty: "Easy"
topics: ["Array", "String", "Trie"]
current_approach: "Sort Strings and Compare the Endpoints"
target_pattern: "Other"
pattern_variant: "Vertical Prefix Scan"
secondary_patterns: ["Trie"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 14. Longest Common Prefix

## Recognition

The problem is best recognized by its direct transformation or specialized invariant. This problem uses the **Vertical Prefix Scan** variant.

## Current Approach

The saved solution uses **Sort Strings and Compare the Endpoints**.

## Interview Approach

Use **Other** with **Vertical Prefix Scan**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Write the invariant in problem terms and keep each update faithful to it.

## Complexity

### Current Solution

Time: O(k log k + p)
Space: O(k) for sorting references

### Target Interview Approach

Time: O(total characters)
Space: O(1) auxiliary

## Common Mistake

Avoid adding machinery that does not simplify the proof or implementation.

## What I Should Remember

- Recognition: The problem is best recognized by its direct transformation or specialized invariant.
- Target: Other - Vertical Prefix Scan.

## Redo Test

Can I derive the target interview approach without looking at code?
