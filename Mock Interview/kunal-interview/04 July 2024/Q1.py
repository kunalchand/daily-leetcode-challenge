"""
LC 637 

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levelOrder = []
        # [[3] [9, 20], [15, 7]]
        # [ (3, 0), (9,1)]

        queue = deque()
        queue.append([root, 0])

        while queue:
            node, level = queue.popleft()
            while level + 1 > len(levelOrder):
                levelOrder.append([])
            levelOrder[level].append(node.val)

            if node.right:
                queue.append([node.right, level + 1])
            if node.left:
                queue.append([node.left, level + 1])

        for index in range(len(levelOrder)):
            level = levelOrder[index]
            average = sum(level) / len(level)
            levelOrder[index] = average

        return levelOrder
