---
leetcode_id: 993
sync_id: "1035"
title: "Cousins in Binary Tree"
slug: "cousins-in-binary-tree"
difficulty: "Easy"
topics: ["Binary Tree"]
current_approach: "Depth and Parent Tracking"
target_pattern: "Tree DFS / Recursion"
pattern_variant: "Depth and Parent Tracking"
secondary_patterns: ["DFS"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 993. Cousins in Binary Tree

## Recognition

Subtree answers combine naturally at a node, or a root-to-leaf state must be carried. This problem uses the **Depth and Parent Tracking** variant.

## Current Approach

The saved solution uses **Depth and Parent Tracking**.

## Interview Approach

Use **Tree DFS / Recursion** with **Depth and Parent Tracking**. The saved implementation already demonstrates this approach.

## Core Mental Model

Define exactly what the recursive call returns before combining child results.

## Complexity

### Current Solution

Time: O(n)
Space: O(h) recursion or O(w) queue/storage

## Common Mistake

Separate leaf/base cases from the combine step.

## What I Should Remember

- Recognition: Subtree answers combine naturally at a node, or a root-to-leaf state must be carried.
- Target: Tree DFS / Recursion - Depth and Parent Tracking.

## Redo Test

Can I derive the target interview approach without looking at code?
