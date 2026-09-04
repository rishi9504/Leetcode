---
leetcode_id: 1071
sync_id: "1146"
title: "Greatest Common Divisor of Strings"
slug: "greatest-common-divisor-of-strings"
difficulty: "Easy"
topics: ["Math", "String"]
current_approach: "Concatenation Compatibility plus GCD"
target_pattern: "Simulation / Math"
pattern_variant: "Concatenation Compatibility plus GCD"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1071. Greatest Common Divisor of Strings

## Recognition

The problem follows explicit rules or a compact arithmetic identity. This problem uses the **Concatenation Compatibility plus GCD** variant.

## Current Approach

The saved solution uses **Concatenation Compatibility plus GCD**.

The strings can share a divisor only when `str1 + str2 == str2 + str1`; the divisor length is the GCD of their lengths.

## Interview Approach

Use **Simulation / Math** with **Concatenation Compatibility plus GCD**. The saved implementation already demonstrates this approach.

## Core Mental Model

Translate each rule into state updates, or prove the identity before replacing simulation.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Handle signs, overflow boundaries, and zero explicitly.

## What I Should Remember

- Recognition: The problem follows explicit rules or a compact arithmetic identity.
- Target: Simulation / Math - Concatenation Compatibility plus GCD.

## Redo Test

Can I derive the target interview approach without looking at code?
