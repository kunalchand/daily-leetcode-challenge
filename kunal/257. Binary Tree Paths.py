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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-paths/
class Solution:
    def DFS(self, root: Optional[TreeNode], path: List) -> None:
        if not root:
            return
        else:
            path.append(str(root.val))
            self.DFS(root.left, path)
            self.DFS(root.right, path)

            if root.left == None and root.right == None:
                self.result.append("->".join(path))

            path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.result = []
        self.DFS(root, [])
        return self.result
