---
leetcode_id: 146
sync_id: "0146"
title: "LRU Cache"
slug: "lru-cache"
difficulty: "Medium"
topics: ["Hash Table", "Linked List", "Design"]
current_approach: "Python Dictionary Insertion Order as LRU Order"
target_pattern: "Design"
pattern_variant: "Hash Map plus Doubly Linked List"
secondary_patterns: ["Hashing"]
solution_quality: "shortcut_or_builtin"
confidence: "yellow"
last_revised: null
redo: true
---

# 146. LRU Cache

## Recognition

A sequence of operations with required per-operation costs suggests a data-structure design. This problem uses the **Hash Map plus Doubly Linked List** variant.

## Current Approach

The saved solution uses **Python Dictionary Insertion Order as LRU Order**.

## Interview Approach

Implement **Design** with **Hash Map plus Doubly Linked List** directly. The saved code delegates the central algorithm to a language feature or hardcoded result.

## Core Mental Model

Choose state that makes the most constrained operation direct, then maintain its invariants.

## Complexity

### Current Solution

Time: Operation-dependent; see the saved methods
Space: O(n) stored state

### Target Interview Approach

Time: Operation-dependent
Space: O(n) stored state

## Common Mistake

Verify every operation meets the requested amortized complexity.

## What I Should Remember

- Recognition: A sequence of operations with required per-operation costs suggests a data-structure design.
- Target: Design - Hash Map plus Doubly Linked List.

## Redo Test

Can I derive the target interview approach without looking at code?
