---
leetcode_id: 1268
sync_id: "1397"
title: "Search Suggestions System"
slug: "search-suggestions-system"
difficulty: "Medium"
topics: ["Array", "String", "Trie", "Heap"]
current_approach: "Sorted Trie with Top-Three Prefix Suggestions"
target_pattern: "Trie"
pattern_variant: "Sorted Trie with Top-Three Prefix Suggestions"
secondary_patterns: ["Binary Search", "Sorting", "Heap / Priority Queue"]
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 1268. Search Suggestions System

## Recognition

Many prefix queries over the same word set suggest a trie. This problem uses the **Sorted Trie with Top-Three Prefix Suggestions** variant.

## Current Approach

The saved solution uses **Sorted Trie with Top-Three Prefix Suggestions**.

Sort products before insertion so each trie node can retain its first three lexicographic suggestions.

## Interview Approach

Use **Trie** with **Sorted Trie with Top-Three Prefix Suggestions**. The saved implementation already demonstrates this approach.

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
- Target: Trie - Sorted Trie with Top-Three Prefix Suggestions.

## Redo Test

Can I derive the target interview approach without looking at code?
