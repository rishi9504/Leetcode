---
leetcode_id: 2493
sync_id: "2583"
title: "Divide Nodes Into the Maximum Number of Groups"
slug: "divide-nodes-into-the-maximum-number-of-groups"
difficulty: "Hard"
topics: ["Graph"]
current_approach: "BFS"
target_pattern: "Graph DFS / BFS"
pattern_variant: "BFS"
secondary_patterns: ["DFS", "Graph Traversal"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 2493. Divide Nodes Into the Maximum Number of Groups

## Recognition

Reachability, components, paths, or state transitions suggest graph traversal. This problem uses the **BFS** variant.

## Current Approach

The saved solution uses **BFS**.

## Interview Approach

Use **Graph DFS / BFS** with **BFS**. The saved implementation already demonstrates this approach.

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
- Target: Graph DFS / BFS - BFS.

## Redo Test

Can I derive the target interview approach without looking at code?
