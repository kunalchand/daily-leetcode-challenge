"""
281. Zigzag Iterator (Premium)
https://leetcode.com/problems/zigzag-iterator/

Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

* ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.

* boolean hasNext() returns true if the iterator still has elements, and false otherwise.

* int next() returns the current element of the iterator and moves the iterator to the next element.

Example:
    Input: v1 = [1,2], v2 = [3,4,5,6]
    Output: [1,3,2,4,5,6]
    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
"""

import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
