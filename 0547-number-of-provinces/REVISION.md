---
leetcode_id: 547
sync_id: "0547"
title: "Number of Provinces"
slug: "number-of-provinces"
difficulty: "Medium"
topics: ["Graph"]
current_approach: "DFS"
target_pattern: "Graph DFS / BFS"
pattern_variant: "DFS"
secondary_patterns: ["BFS", "Graph Traversal"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 547. Number of Provinces

## Recognition

Reachability, components, paths, or state transitions suggest graph traversal. This problem uses the **DFS** variant.

## Current Approach

The saved solution uses **DFS**.

## Interview Approach

Use **Graph DFS / BFS** with **DFS**. The saved implementation already demonstrates this approach.

## Core Mental Model

Model nodes and edges first, then mark each state before it can be scheduled twice.

## Complexity

### Current Solution

Time: O(V + E)
Space: O(V + E)

## Common Mistake

Choose DFS for recursive structure and BFS for shortest unweighted distance.

## What I Should Remember

- Recognition: Reachability, components, paths, or state transitions suggest graph traversal.
- Target: Graph DFS / BFS - DFS.

## Redo Test

Can I derive the target interview approach without looking at code?
