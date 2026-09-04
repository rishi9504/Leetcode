---
leetcode_id: 2000
sync_id: "2128"
title: "Reverse Prefix of Word"
slug: "reverse-prefix-of-word"
difficulty: "Easy"
topics: ["String", "Stack"]
current_approach: "Stack"
target_pattern: "Stack"
pattern_variant: "Stack"
secondary_patterns: ["Two Pointers"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 2000. Reverse Prefix of Word

## Recognition

Nested structure, deferred work, or last-in-first-out matching suggests a stack. This problem uses the **Stack** variant.

## Current Approach

The saved solution uses **Stack**.

## Interview Approach

Use **Stack** with **Stack**. The saved implementation already demonstrates this approach.

## Core Mental Model

The stack stores unfinished context; each pop resolves the most recent dependency.

## Complexity

### Current Solution

Time: O(n) for the main traversal
Space: O(1) to O(n), according to stored state/output

## Common Mistake

Guard every pop and preserve operand/order semantics.

## What I Should Remember

- Recognition: Nested structure, deferred work, or last-in-first-out matching suggests a stack.
- Target: Stack - Stack.

## Redo Test

Can I derive the target interview approach without looking at code?
