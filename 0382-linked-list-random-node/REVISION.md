---
leetcode_id: 382
sync_id: "0382"
title: "Linked List Random Node"
slug: "linked-list-random-node"
difficulty: "Medium"
topics: ["Linked List", "Math"]
current_approach: "Materialize All Values and random.choice()"
target_pattern: "Simulation / Math"
pattern_variant: "Reservoir Sampling"
secondary_patterns: ["Randomized"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 382. Linked List Random Node

## Recognition

The problem follows explicit rules or a compact arithmetic identity. This problem uses the **Reservoir Sampling** variant.

## Current Approach

The saved solution uses **Materialize All Values and random.choice()**.

## Interview Approach

Use **Simulation / Math** with **Reservoir Sampling**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Translate each rule into state updates, or prove the identity before replacing simulation.

## Complexity

### Current Solution

Time: construction O(n); getRandom O(1)
Space: O(n)

### Target Interview Approach

Time: construction O(1); getRandom O(n)
Space: O(1)

## Common Mistake

Handle signs, overflow boundaries, and zero explicitly.

## What I Should Remember

- Recognition: The problem follows explicit rules or a compact arithmetic identity.
- Target: Simulation / Math - Reservoir Sampling.

## Redo Test

Can I derive the target interview approach without looking at code?
