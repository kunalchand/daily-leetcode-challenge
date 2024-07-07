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


class Solution:
    # Return [Depth, Diameter]
    """
    def DFS(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if root == None:
            return (0, 0)

        left_depth, left_diameter = self.DFS(root.left)
        right_depth, right_diameter = self.DFS(root.right)

        node_diameter = left_depth + right_depth

        return (
            1 + max(left_depth, right_depth),
            max(node_diameter, left_diameter, right_diameter),
        )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, diameter = self.DFS(root)
        return diameter
    """

    # Return [Depth] {Global Diameter Variable}
    def traversal(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        else:
            leftDepth = self.traversal(node.left)
            rightDepth = self.traversal(node.right)
            self.maxDiameter = max(self.maxDiameter, leftDepth + rightDepth)

            return 1 + max(leftDepth, rightDepth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.traversal(root)
        return self.maxDiameter
