---
leetcode_id: 175
sync_id: "0175"
title: "Combine Two Tables"
slug: "combine-two-tables"
difficulty: "Easy"
topics: ["Database"]
current_approach: "SQL Join"
target_pattern: "SQL / Database"
pattern_variant: "SQL Join"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 175. Combine Two Tables

## Recognition

The output is a relational filter, join, grouping, or ranking query. This problem uses the **SQL Join** variant.

## Current Approach

The saved solution uses **SQL Join**.

## Interview Approach

Use **SQL / Database** with **SQL Join**. The saved implementation already demonstrates this approach.

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
- Target: SQL / Database - SQL Join.

## Redo Test

Can I derive the target interview approach without looking at code?
