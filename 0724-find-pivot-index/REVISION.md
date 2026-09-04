---
leetcode_id: 724
sync_id: "0724"
title: "Find Pivot Index"
slug: "find-pivot-index"
difficulty: "Easy"
topics: ["Array"]
current_approach: "Running Left Sum"
target_pattern: "Prefix Sum / Prefix-Suffix"
pattern_variant: "Running Left Sum"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 724. Find Pivot Index

## Recognition

Repeated range totals or information from both sides suggests precomputed aggregates. This problem uses the **Running Left Sum** variant.

## Current Approach

The saved solution uses **Running Left Sum**.

Subtract the current value from the right total before comparing it with the accumulated left total.

## Interview Approach

Use **Prefix Sum / Prefix-Suffix** with **Running Left Sum**. The saved implementation already demonstrates this approach.

## Core Mental Model

Carry left-side state forward and combine it with right-side state at each position.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Be precise about whether the current element is included in each aggregate.

## What I Should Remember

- Recognition: Repeated range totals or information from both sides suggests precomputed aggregates.
- Target: Prefix Sum / Prefix-Suffix - Running Left Sum.

## Redo Test

Can I derive the target interview approach without looking at code?
