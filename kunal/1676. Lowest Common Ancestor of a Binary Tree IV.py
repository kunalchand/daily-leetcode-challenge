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


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recursion(self, node: "TreeNode") -> List:
        if not node:
            return []
        else:
            leftList = self.recursion(node.left)
            rightList = self.recursion(node.right)
            currentList = leftList + rightList
            if node.val in self.hashset:
                currentList += [node.val]

            if len(currentList) == len(self.hashset) and not self.LCA:
                self.LCA = node
            return currentList

    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        self.hashset = set()
        for node in nodes:
            self.hashset.add(node.val)
        self.LCA = None
        self.recursion(root)
        return self.LCA
