---
leetcode_id: 139
sync_id: "0139"
title: "Word Break"
slug: "word-break"
difficulty: "Medium"
topics: ["Array", "Hash Table", "String", "Trie"]
current_approach: "Bottom-Up Dynamic Programming with Linear wordDict Membership"
target_pattern: "Dynamic Programming"
pattern_variant: "1D Dynamic Programming"
secondary_patterns: ["Hashing", "Trie"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 139. Word Break

## Recognition

Overlapping subproblems with a small state and reusable transitions suggest DP. This problem uses the **1D Dynamic Programming** variant.

## Current Approach

The saved solution uses **Bottom-Up Dynamic Programming with Linear wordDict Membership**.

## Interview Approach

Use **Dynamic Programming** with **1D Dynamic Programming**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Define the state, base case, and transition before choosing memoization or tabulation.

## Complexity

### Current Solution

Time: O(n^2 * W * L) worst case with list membership
Space: O(n)

### Target Interview Approach

Time: O(n^2 * L) with a hash set
Space: O(n + W)

## Common Mistake

Check iteration order so every dependency is already available.

## What I Should Remember

- Recognition: Overlapping subproblems with a small state and reusable transitions suggest DP.
- Target: Dynamic Programming - 1D Dynamic Programming.

## Redo Test

Can I derive the target interview approach without looking at code?
