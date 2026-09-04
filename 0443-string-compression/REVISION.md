---
leetcode_id: 443
sync_id: "0443"
title: "String Compression"
slug: "string-compression"
difficulty: "Medium"
topics: ["String"]
current_approach: "Build a Separate Compressed String, Then Replace the Input"
target_pattern: "Two Pointers"
pattern_variant: "Two Pointers"
secondary_patterns: []
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 443. String Compression

## Recognition

Look for ordered data, paired choices, or an in-place partition/traversal. This problem uses the **Two Pointers** variant.

## Current Approach

The saved solution uses **Build a Separate Compressed String, Then Replace the Input**.

## Interview Approach

Use **Two Pointers** with **Two Pointers**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Move the pointer whose side can no longer improve or satisfy the invariant.

## Complexity

### Current Solution

Time: O(n^2) in the worst case due to immutable string appends
Space: O(n)

### Target Interview Approach

Time: O(n)
Space: O(1) auxiliary

## Common Mistake

Do not move both pointers until the invariant justifies it.

## What I Should Remember

- Recognition: Look for ordered data, paired choices, or an in-place partition/traversal.
- Target: Two Pointers - Two Pointers.

## Redo Test

Can I derive the target interview approach without looking at code?
