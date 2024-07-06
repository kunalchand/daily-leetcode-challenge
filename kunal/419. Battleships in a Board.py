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


# https://leetcode.com/problems/battleships-in-a-board/
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS = len(board)
        COLS = len(board[0])

        board.insert(0, ["."] * (COLS + 2))
        board.append(["."] * (COLS + 2))

        for row in board:
            row.insert(0, ".")
            row.append(".")

        count = 0

        for x in range(1, ROWS + 1):
            for y in range(1, COLS + 1):
                if (
                    board[x][y] == "X"
                    and board[x - 1][y] == "."
                    and board[x][y - 1] == "."
                ):
                    count += 1

        return count
