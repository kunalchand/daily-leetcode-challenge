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


# https://leetcode.com/problems/design-memory-allocator/
class Allocator:

    def __init__(self, n: int):
        self.heap = [(0, [0] * n)]
        self.memory = [0] * n
        self.memoryID = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        dump = []
        return_index = -1
        while self.heap:
            index, free_memory = heappop(self.heap)
            if len(free_memory) >= size:
                return_index = index
                for idx in range(index, index + size):
                    self.memory[idx] = mID
                    self.memoryID[mID].append(idx)
                left_over = len(free_memory) - size
                if left_over > 0:
                    dump.append((index + size, [0] * left_over))
                break
            else:
                dump.append((index, free_memory))
        self.heap += dump
        heapify(self.heap)
        return return_index

    def free(self, mID: int) -> int:
        for index in self.memoryID[mID]:
            self.memory[index] = 0
        memoryFreed = len(self.memoryID[mID])
        self.memoryID[mID] = []

        self.heap = []

        i = 0
        while i < len(self.memory):
            if self.memory[i] == 0:
                free_memory = []
                idx, index = i, i
                while index < len(self.memory) and self.memory[index] == 0:
                    free_memory.append(0)
                    index += 1
                self.heap.append((idx, free_memory))
                i = index + 1
            else:
                i += 1

        heapify(self.heap)

        return memoryFreed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
