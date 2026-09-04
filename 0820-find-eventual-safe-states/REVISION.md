---
leetcode_id: 802
sync_id: "0820"
title: "Find Eventual Safe States"
slug: "find-eventual-safe-states"
difficulty: "Medium"
topics: ["Graph"]
current_approach: "Memoized DFS State Coloring"
target_pattern: "Graph DFS / BFS"
pattern_variant: "DFS State Coloring"
secondary_patterns: ["DFS", "Graph Traversal", "Topological Sort"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 802. Find Eventual Safe States

## Recognition

Reachability, components, paths, or state transitions suggest graph traversal. This problem uses the **DFS State Coloring** variant.

## Current Approach

The saved solution uses **Memoized DFS State Coloring**.

## Interview Approach

Use **Graph DFS / BFS** with **DFS State Coloring**. The saved implementation already demonstrates this approach.

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
- Target: Graph DFS / BFS - DFS State Coloring.

## Redo Test

Can I derive the target interview approach without looking at code?
