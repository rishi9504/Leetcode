---
leetcode_id: 208
sync_id: "0208"
title: "Implement Trie (Prefix Tree)"
slug: "implement-trie-prefix-tree"
difficulty: "Medium"
topics: ["Hash Table", "String", "Design", "Trie"]
current_approach: "Prefix Tree with Terminal Markers"
target_pattern: "Trie"
pattern_variant: "Prefix Tree with Terminal Markers"
secondary_patterns: ["Hashing", "Design"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 208. Implement Trie (Prefix Tree)

## Recognition

Many prefix queries over the same word set suggest a trie. This problem uses the **Prefix Tree with Terminal Markers** variant.

## Current Approach

The saved solution uses **Prefix Tree with Terminal Markers**.

Traversal proves a prefix exists; a terminal marker is still required to prove a complete word exists.

## Interview Approach

Use **Trie** with **Prefix Tree with Terminal Markers**. The saved implementation already demonstrates this approach.

## Core Mental Model

Each node represents a prefix; terminal state distinguishes a full word from a prefix.

## Complexity

### Current Solution

Time: O(total processed characters)
Space: O(total stored characters)

## Common Mistake

Wildcard search may branch, so prune missing children immediately.

## What I Should Remember

- Recognition: Many prefix queries over the same word set suggest a trie.
- Target: Trie - Prefix Tree with Terminal Markers.

## Redo Test

Can I derive the target interview approach without looking at code?
