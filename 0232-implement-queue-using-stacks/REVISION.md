---
leetcode_id: 232
sync_id: "0232"
title: "Implement Queue using Stacks"
slug: "implement-queue-using-stacks"
difficulty: "Easy"
topics: ["Stack", "Design", "Queue"]
current_approach: "Single Python List with Front Insertion"
target_pattern: "Stack"
pattern_variant: "Stack"
secondary_patterns: ["Design", "Queue"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 232. Implement Queue using Stacks

## Recognition

Nested structure, deferred work, or last-in-first-out matching suggests a stack. This problem uses the **Stack** variant.

## Current Approach

The saved solution uses **Single Python List with Front Insertion**.

## Interview Approach

Use **Stack** with **Stack**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

The stack stores unfinished context; each pop resolves the most recent dependency.

## Complexity

### Current Solution

Time: push O(n); pop/peek O(1)
Space: O(n)

### Target Interview Approach

Time: amortized O(1) per operation
Space: O(n)

## Common Mistake

Guard every pop and preserve operand/order semantics.

## What I Should Remember

- Recognition: Nested structure, deferred work, or last-in-first-out matching suggests a stack.
- Target: Stack - Stack.

## Redo Test

Can I derive the target interview approach without looking at code?
