---
leetcode_id: 752
sync_id: "0753"
title: "Open the Lock"
slug: "open-the-lock"
difficulty: "Medium"
topics: ["Array", "Hash Table", "String"]
current_approach: "Breadth-First Search with a Malformed Initial Visited Set"
target_pattern: "Graph DFS / BFS"
pattern_variant: "Shortest Unweighted State Search"
secondary_patterns: ["Hashing"]
solution_quality: "needs_review"
confidence: "yellow"
last_revised: null
redo: true
---

# 752. Open the Lock

## Recognition

Reachability, components, paths, or state transitions suggest graph traversal. This problem uses the **Shortest Unweighted State Search** variant.

## Current Approach

The saved solution uses **Breadth-First Search with a Malformed Initial Visited Set**.

## Interview Approach

Re-derive **Graph DFS / BFS** with **Shortest Unweighted State Search** and test it carefully. The saved initialization `set('0000')` creates `{'0'}` rather than marking the starting combination `'0000'` as visited.

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
- Target: Graph DFS / BFS - Shortest Unweighted State Search.

## Redo Test

Can I derive the target interview approach without looking at code?
