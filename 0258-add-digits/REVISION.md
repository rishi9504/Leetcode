---
leetcode_id: 258
sync_id: "0258"
title: "Add Digits"
slug: "add-digits"
difficulty: "Easy"
topics: ["Math"]
current_approach: "Repeated String Digit Summation"
target_pattern: "Simulation / Math"
pattern_variant: "Simulation"
secondary_patterns: ["Math"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 258. Add Digits

## Recognition

The problem follows explicit rules or a compact arithmetic identity. This problem uses the **Simulation** variant.

## Current Approach

The saved solution uses **Repeated String Digit Summation**.

## Interview Approach

Use **Simulation / Math** with **Simulation**. The saved implementation is valid, but it gives up an expected time or space improvement.

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
- Target: Simulation / Math - Simulation.

## Redo Test

Can I derive the target interview approach without looking at code?
