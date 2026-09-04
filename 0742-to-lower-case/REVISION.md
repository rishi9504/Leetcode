---
leetcode_id: 709
sync_id: "0742"
title: "To Lower Case"
slug: "to-lower-case"
difficulty: "Easy"
topics: ["String"]
current_approach: "Python str.lower()"
target_pattern: "Simulation / Math"
pattern_variant: "ASCII Case Conversion"
secondary_patterns: []
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 709. To Lower Case

## Recognition

The problem follows explicit rules or a compact arithmetic identity. This problem uses the **ASCII Case Conversion** variant.

## Current Approach

The saved solution uses **Python str.lower()**.

## Interview Approach

Implement **Simulation / Math** with **ASCII Case Conversion** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Translate each rule into state updates, or prove the identity before replacing simulation.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

### Target Interview Approach

Time: Problem-dependent, commonly O(n) or O(log n)
Space: Usually O(1) auxiliary

## Common Mistake

Handle signs, overflow boundaries, and zero explicitly.

## What I Should Remember

- Recognition: The problem follows explicit rules or a compact arithmetic identity.
- Target: Simulation / Math - ASCII Case Conversion.

## Redo Test

Can I derive the target interview approach without looking at code?
