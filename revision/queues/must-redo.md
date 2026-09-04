# Must Redo

Generated from `redo: true`. Work from recognition and the problem statement before opening the saved solution.

## Hashing

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 128 | [Longest Consecutive Sequence](../../0128-longest-consecutive-sequence/REVISION.md) | Sequence-Start Hash-Set Expansion with Debug Output | Sequence-Start Expansion | needs_review |
| 217 | [Contains Duplicate](../../0217-contains-duplicate/REVISION.md) | Hash Set Scan with an Implicit False Return | Seen-Set Membership | needs_review |
| 290 | [Word Pattern](../../0290-word-pattern/REVISION.md) | First-Occurrence Index Comparison | Bijection Maps | valid_but_suboptimal |
| 349 | [Intersection of Two Arrays](../../0349-intersection-of-two-arrays/REVISION.md) | Built-in Set Intersection | Hash-Set Membership | shortcut_or_builtin |
| 771 | [Jewels and Stones](../../0782-jewels-and-stones/REVISION.md) | Membership Scan that Rebuilds the Jewel Set | Hashing | valid_but_suboptimal |

## Two Pointers

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 26 | [Remove Duplicates from Sorted Array](../../0026-remove-duplicates-from-sorted-array/REVISION.md) | Set Conversion Followed by Sorting | Write Pointer | shortcut_or_builtin |
| 88 | [Merge Sorted Array](../../0088-merge-sorted-array/REVISION.md) | Copy the Second Array, Then Sort Everything | Two Pointers | valid_but_suboptimal |
| 189 | [Rotate Array](../../0189-rotate-array/REVISION.md) | Array Slicing and Concatenation | Two Pointers | valid_but_suboptimal |
| 202 | [Happy Number](../../0202-happy-number/REVISION.md) | String Digit Simulation with a List of Seen Values | Cycle Detection | valid_but_suboptimal |
| 287 | [Find the Duplicate Number](../../0287-find-the-duplicate-number/REVISION.md) | Hash Set Duplicate Detection | Floyd Cycle Detection | valid_but_suboptimal |
| 350 | [Intersection of Two Arrays II](../../0350-intersection-of-two-arrays-ii/REVISION.md) | Sort and Two Pointers with an Active Delay | Sort and Merge | needs_review |
| 443 | [String Compression](../../0443-string-compression/REVISION.md) | Build a Separate Compressed String, Then Replace the Input | Two Pointers | valid_but_suboptimal |
| 821 | [Shortest Distance to a Character](../../0841-shortest-distance-to-a-character/REVISION.md) | Store Every Target Position, Then Sweep | Two Pointers | alternate_approach |
| 1089 | [Duplicate Zeros](../../1168-duplicate-zeros/REVISION.md) | Repeated List Insert and Pop | Two Pointers | valid_but_suboptimal |

## Prefix Sum / Prefix-Suffix

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 3334 | [Find the Maximum Factor Score of Array](../../3593-find-the-maximum-factor-score-of-array/REVISION.md) | Prefix/Suffix GCD with Recomputed LCM per Removal | Prefix/Suffix GCD and LCM | valid_but_suboptimal |
| 3354 | [Make Array Elements Equal to Zero](../../3616-make-array-elements-equal-to-zero/REVISION.md) | Full Simulation from Every Zero and Direction | Left/Right Sum Balance | valid_but_suboptimal |

## Binary Search

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 4 | [Median of Two Sorted Arrays](../../0004-median-of-two-sorted-arrays/REVISION.md) | Partition Binary Search with Reversed Boundary Variables | Partition on the Smaller Array | needs_review |
| 69 | [Sqrt(x)](../../0069-sqrtx/REVISION.md) | Linear Trial of Consecutive Integers | Binary Search | valid_but_suboptimal |
| 74 | [Search a 2D Matrix](../../0074-search-a-2d-matrix/REVISION.md) | Flatten the Matrix, Then Binary Search | Binary Search | valid_but_suboptimal |
| 81 | [Search in Rotated Sorted Array II](../../0081-search-in-rotated-sorted-array-ii/REVISION.md) | Python Linear Membership Test | Duplicate-Aware Rotated Search | shortcut_or_builtin |
| 222 | [Count Complete Tree Nodes](../../0222-count-complete-tree-nodes/REVISION.md) | Breadth-First Count of Every Node | Complete-Tree Height Counting | valid_but_suboptimal |
| 658 | [Find K Closest Elements](../../0658-find-k-closest-elements/REVISION.md) | Shrink Opposing Ends Until k Elements Remain | Binary Search for Window Start | valid_but_suboptimal |
| 744 | [Find Smallest Letter Greater Than Target](../../0745-find-smallest-letter-greater-than-target/REVISION.md) | Linear Scan with Wraparound | Upper Bound with Wraparound | valid_but_suboptimal |

## Stack

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 232 | [Implement Queue using Stacks](../../0232-implement-queue-using-stacks/REVISION.md) | Single Python List with Front Insertion | Stack | valid_but_suboptimal |

## Monotonic Stack / Queue

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 316 | [Remove Duplicate Letters](../../0316-remove-duplicate-letters/REVISION.md) | Monotonic Stack with Repeated Linear Membership Checks | Monotonic Stack | valid_but_suboptimal |
| 739 | [Daily Temperatures](../../0739-daily-temperatures/REVISION.md) | Monotonic Stack with Debug Output | Next Warmer Day | needs_review |
| 1081 | [Smallest Subsequence of Distinct Characters](../../1159-smallest-subsequence-of-distinct-characters/REVISION.md) | Monotonic Stack with Repeated Linear Membership Checks | Monotonic Stack | valid_but_suboptimal |

## Linked List Techniques

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 19 | [Remove Nth Node From End of List](../../0019-remove-nth-node-from-end-of-list/REVISION.md) | Length Count Followed by a Second Traversal | Fast and Slow Pointer Gap | valid_but_suboptimal |
| 1721 | [Swapping Nodes in a Linked List](../../0528-swapping-nodes-in-a-linked-list/REVISION.md) | Length Count Followed by a Second Traversal | Fast & Slow Pointers | valid_but_suboptimal |

## Tree DFS / Recursion

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 100 | [Same Tree](../../0100-same-tree/REVISION.md) | Lockstep Tree Comparison with Debug Output | Lockstep Tree Comparison | needs_review |
| 110 | [Balanced Binary Tree](../../0110-balanced-binary-tree/REVISION.md) | Postorder DFS Returning Subtree Information | Postorder Height Sentinel | needs_review |
| 872 | [Leaf-Similar Trees](../../0904-leaf-similar-trees/REVISION.md) | Recursive Leaf Lists with Repeated Concatenation | Leaf Sequence Comparison | valid_but_suboptimal |

## Tree BFS

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 515 | [Find Largest Value in Each Tree Row](../../0515-find-largest-value-in-each-tree-row/REVISION.md) | List-Based BFS with pop(0) | BFS | valid_but_suboptimal |

## BST

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 230 | [Kth Smallest Element in a BST](../../0230-kth-smallest-element-in-a-bst/REVISION.md) | Full Reverse-Inorder List Materialization | Early-Stopping Inorder Traversal | valid_but_suboptimal |

## Graph DFS / BFS

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 752 | [Open the Lock](../../0753-open-the-lock/REVISION.md) | Breadth-First Search with a Malformed Initial Visited Set | Shortest Unweighted State Search | needs_review |

## Union Find

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 684 | [Redundant Connection](../../0684-redundant-connection/REVISION.md) | Incremental DFS Cycle Detection | Disjoint-Set Cycle Detection | valid_but_suboptimal |

## Heap / Priority Queue

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 347 | [Top K Frequent Elements](../../0347-top-k-frequent-elements/REVISION.md) | Frequency Map and Bucket Sort | Heap / Priority Queue | alternate_approach |

## Backtracking

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 22 | [Generate Parentheses](../../0022-generate-parentheses/REVISION.md) | Backtracking into a Set | Balanced Choice Counts | needs_review |

## Dynamic Programming

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 118 | [Pascal's Triangle](../../0118-pascals-triangle/REVISION.md) | Hardcoded Rows Through the Constraint Limit | Build Each Row from the Previous Row | shortcut_or_builtin |
| 139 | [Word Break](../../0139-word-break/REVISION.md) | Bottom-Up Dynamic Programming with Linear wordDict Membership | 1D Dynamic Programming | valid_but_suboptimal |

## Bit Manipulation

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 190 | [Reverse Bits](../../0190-reverse-bits/REVISION.md) | Binary String Formatting and Reversal | Bit-by-Bit Fixed-Width Reversal | shortcut_or_builtin |
| 191 | [Number of 1 Bits](../../0191-number-of-1-bits/REVISION.md) | bin() String Conversion and Counting | Brian Kernighan Bit Clearing | shortcut_or_builtin |
| 268 | [Missing Number](../../0268-missing-number/REVISION.md) | Expected Sum Minus Actual Sum | Bit Manipulation | alternate_approach |
| 342 | [Power of Four](../../0342-power-of-four/REVISION.md) | Floating-Point Logarithm Check | Power-of-Two and Bit-Position Test | needs_review |
| 1356 | [Sort Integers by The Number of 1 Bits](../../1458-sort-integers-by-the-number-of-1-bits/REVISION.md) | bin().count() Followed by Sorting | Bit Manipulation | shortcut_or_builtin |

## Trie

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 211 | [Design Add and Search Words Data Structure](../../0211-design-add-and-search-words-data-structure/REVISION.md) | Length-Bucketed Set with Linear Wildcard Scan | Trie with Wildcard DFS | valid_but_suboptimal |

## Simulation / Math

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 7 | [Reverse Integer](../../0007-reverse-integer/REVISION.md) | String Conversion and Slice Reversal | Arithmetic Digit Extraction | shortcut_or_builtin |
| 9 | [Palindrome Number](../../0009-palindrome-number/REVISION.md) | String Reversal Comparison | Reverse Half the Number | alternate_approach |
| 43 | [Multiply Strings](../../0043-multiply-strings/REVISION.md) | Python Integer Conversion and Multiplication | Grade-School Multiplication | shortcut_or_builtin |
| 50 | [Pow(x, n)](../../0050-powx-n/REVISION.md) | Python Built-in Exponentiation | Fast Exponentiation / Divide and Conquer | shortcut_or_builtin |
| 65 | [Valid Number](../../0065-valid-number/REVISION.md) | Python float() Parsing | Finite-State Number Parsing | shortcut_or_builtin |
| 66 | [Plus One](../../0066-plus-one/REVISION.md) | Digit List to Python Integer Conversion | Right-to-Left Carry Propagation | shortcut_or_builtin |
| 67 | [Add Binary](../../0067-add-binary/REVISION.md) | Base-2 Integer Conversion and bin() | Bit-by-Bit Addition with Carry | shortcut_or_builtin |
| 258 | [Add Digits](../../0258-add-digits/REVISION.md) | Repeated String Digit Summation | Simulation | valid_but_suboptimal |
| 382 | [Linked List Random Node](../../0382-linked-list-random-node/REVISION.md) | Materialize All Values and random.choice() | Reservoir Sampling | valid_but_suboptimal |
| 709 | [To Lower Case](../../0742-to-lower-case/REVISION.md) | Python str.lower() | ASCII Case Conversion | shortcut_or_builtin |
| 1025 | [Divisor Game](../../1086-divisor-game/REVISION.md) | Quadratic Bottom-Up Dynamic Programming | Parity Proof | valid_but_suboptimal |
| 1844 | [Replace All Digits with Characters](../../1954-replace-all-digits-with-characters/REVISION.md) | Repeated Immutable String Slicing | Simulation | valid_but_suboptimal |

## Design

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 146 | [LRU Cache](../../0146-lru-cache/REVISION.md) | Python Dictionary Insertion Order as LRU Order | Hash Map plus Doubly Linked List | shortcut_or_builtin |
| 225 | [Implement Stack using Queues](../../0225-implement-stack-using-queues/REVISION.md) | Rotated Python List Queue with Debug Output | Single-Queue Rotation | needs_review |

## Other

| LC | Problem | Current Approach | Variant | Quality |
| ---: | --- | --- | --- | --- |
| 14 | [Longest Common Prefix](../../0014-longest-common-prefix/REVISION.md) | Sort Strings and Compare the Endpoints | Vertical Prefix Scan | valid_but_suboptimal |
| 58 | [Length of Last Word](../../0058-length-of-last-word/REVISION.md) | Split into Words and Read the Last Word | String Scanning | valid_but_suboptimal |
| 448 | [Find All Numbers Disappeared in an Array](../../0448-find-all-numbers-disappeared-in-an-array/REVISION.md) | Built-in Set Difference | In-Place Index Marking | needs_review |
| 649 | [Dota2 Senate](../../0649-dota2-senate/REVISION.md) | Two List Queues with pop(0) and Debug Output | Indexed Queue Simulation | needs_review |
