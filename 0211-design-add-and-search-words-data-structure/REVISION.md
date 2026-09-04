---
leetcode_id: 211
sync_id: "0211"
title: "Design Add and Search Words Data Structure"
slug: "design-add-and-search-words-data-structure"
difficulty: "Medium"
topics: ["String", "Design", "Trie"]
current_approach: "Length-Bucketed Set with Linear Wildcard Scan"
target_pattern: "Trie"
pattern_variant: "Trie with Wildcard DFS"
secondary_patterns: ["DFS", "Design"]
solution_quality: "valid_but_suboptimal"
confidence: "yellow"
last_revised: null
redo: true
---

# 211. Design Add and Search Words Data Structure

## Recognition

Many prefix queries over the same word set suggest a trie. This problem uses the **Trie with Wildcard DFS** variant.

## Current Approach

The saved solution uses **Length-Bucketed Set with Linear Wildcard Scan**.

## Interview Approach

Use **Trie** with **Trie with Wildcard DFS**. The saved implementation is valid, but it gives up an expected time or space improvement.

## Core Mental Model

Each node represents a prefix; terminal state distinguishes a full word from a prefix.

## Complexity

### Current Solution

Time: add O(L); search O(WL) within a length bucket
Space: O(total characters)

### Target Interview Approach

Time: add O(L); search proportional to visited trie states
Space: O(total characters)

## Common Mistake

Wildcard search may branch, so prune missing children immediately.

## What I Should Remember

- Recognition: Many prefix queries over the same word set suggest a trie.
- Target: Trie - Trie with Wildcard DFS.

## Redo Test

Can I derive the target interview approach without looking at code?
