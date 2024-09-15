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


# https://leetcode.com/problems/maximum-multiplication-score
class Solution:
    # 2D DP TLE
    """
    @cache
    def rec(self, ai: int, bi: int, n: int) -> int:
        if n == 0 or ai >= len(self.a) or bi >= len(self.b) - (n-1):
            return 0
        else:
            score = float('-inf')
            for new_bi in range(bi, len(self.b) - (n-1)):
                score = max(score, self.a[ai] * self.b[new_bi] + self.rec(ai + 1, new_bi + 1, n-1))
            return score

    def maxScore(self, a: List[int], b: List[int]) -> int:
        self.a = a
        self.b = b

        return self.rec(0, 0, 4)
    """

    # 1D DP
    # Reference: https://www.twitch.tv/videos/2251478815
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [[float("-inf") for _ in range(4)] for _ in range(len(b) + 1)]

        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i - 1][0], b[i - 1] * a[0])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + b[i - 1] * a[1])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + b[i - 1] * a[2])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + b[i - 1] * a[3])

        return dp[len(dp) - 1][3]
