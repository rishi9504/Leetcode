---
leetcode_id: 207
sync_id: "0207"
title: "Course Schedule"
slug: "course-schedule"
difficulty: "Medium"
topics: ["Graph"]
current_approach: "Topological Sort"
target_pattern: "Topological Sort"
pattern_variant: "Topological Sort"
secondary_patterns: ["DFS", "BFS", "Graph Traversal"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 207. Course Schedule

## Recognition

Prerequisites or dependencies form a directed ordering problem. This problem uses the **Topological Sort** variant.

## Current Approach

The saved solution uses **Topological Sort**.

## Interview Approach

Use **Topological Sort** with **Topological Sort**. The saved implementation already demonstrates this approach.

## Core Mental Model

Remove zero-indegree nodes or use three-state DFS; a remaining cycle makes the order impossible.

## Complexity

### Current Solution

Time: O(V + E)
Space: O(V + E)

## Common Mistake

Distinguish currently visiting from fully processed nodes.

## What I Should Remember

- Recognition: Prerequisites or dependencies form a directed ordering problem.
- Target: Topological Sort - Topological Sort.

## Redo Test

Can I derive the target interview approach without looking at code?
