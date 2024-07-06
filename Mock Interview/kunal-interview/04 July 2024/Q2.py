"""
LC 844

Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "aghb##c", t = "ard##c"
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

# s = "ab#c", t = "ad#c"


class Solution:
    def manageStack(self, string: str) -> List:
        stack = []
        for char in string:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.manageStack(s) == self.manageStack(t)
