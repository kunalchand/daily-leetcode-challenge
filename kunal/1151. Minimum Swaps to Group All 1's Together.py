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


# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        zeroes = len(data) - ones

        if ones == 0 or zeroes == 0:
            return 0

        window = Counter(data[:ones])
        minSwaps = min(inf, window[0])

        left = 0
        for right in range(ones, len(data)):
            window[data[left]] -= 1
            window[data[right]] += 1

            minSwaps = min(minSwaps, window[0])
            left += 1

        return minSwaps
