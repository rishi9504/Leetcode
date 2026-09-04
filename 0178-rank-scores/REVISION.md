---
leetcode_id: 178
sync_id: "0178"
title: "Rank Scores"
slug: "rank-scores"
difficulty: "Medium"
topics: ["Database"]
current_approach: "SQL Window Ranking"
target_pattern: "SQL / Database"
pattern_variant: "SQL Window/Ranking"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 178. Rank Scores

## Recognition

The output is a relational filter, join, grouping, or ranking query. This problem uses the **SQL Window/Ranking** variant.

## Current Approach

The saved solution uses **SQL Window Ranking**.

## Interview Approach

Use **SQL / Database** with **SQL Window/Ranking**. The saved implementation already demonstrates this approach.

## Core Mental Model

Build the required row set first, then aggregate or rank at the correct grain.

## Complexity

### Current Solution

Time: Optimizer- and index-dependent
Space: Result/intermediate-set dependent

## Common Mistake

Account for NULL semantics and duplicate rows.

## What I Should Remember

- Recognition: The output is a relational filter, join, grouping, or ranking query.
- Target: SQL / Database - SQL Window/Ranking.

## Redo Test

Can I derive the target interview approach without looking at code?
