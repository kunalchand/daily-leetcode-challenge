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


# Time-O(n) Space-O(k)
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.iterator = deque()
        if v1:
            self.iterator.append([0, v1])
        if v2:
            self.iterator.append([0, v2])

    def next(self) -> int:
        pointer, v = self.iterator.popleft()
        value = v[pointer]
        pointer += 1
        if pointer < len(v):
            self.iterator.append([pointer, v])
        return value

    def hasNext(self) -> bool:
        return True if len(self.iterator) > 0 else False


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
