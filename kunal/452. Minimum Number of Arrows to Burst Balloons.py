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


# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        heap = []

        count = 0

        for start, end in points:
            if not heap:
                heappush(heap, [end, start])
            else:
                top_end, top_start = heap[0]

                if top_end >= start:
                    heappush(heap, [end, start])
                else:
                    count += 1
                    heap = []
                    heappush(heap, [end, start])

        return count + 1
