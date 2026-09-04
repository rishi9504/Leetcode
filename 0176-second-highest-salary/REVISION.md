---
leetcode_id: 176
sync_id: "0176"
title: "Second Highest Salary"
slug: "second-highest-salary"
difficulty: "Medium"
topics: ["Database"]
current_approach: "SQL Aggregation"
target_pattern: "SQL / Database"
pattern_variant: "SQL Aggregation"
secondary_patterns: []
solution_quality: "interview_ready"
confidence: "yellow"
last_revised: null
redo: false
---

# 176. Second Highest Salary

## Recognition

The output is a relational filter, join, grouping, or ranking query. This problem uses the **SQL Aggregation** variant.

## Current Approach

The saved solution uses **SQL Aggregation**.

## Interview Approach

Use **SQL / Database** with **SQL Aggregation**. The saved implementation already demonstrates this approach.

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
- Target: SQL / Database - SQL Aggregation.

## Redo Test

Can I derive the target interview approach without looking at code?
