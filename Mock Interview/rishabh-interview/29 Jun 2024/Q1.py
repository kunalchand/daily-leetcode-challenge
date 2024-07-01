"""
669. Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/

Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change 
the relative structure of the elements that will remain in the tree (i.e., any node's descendant 
should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. 
Note that the root may change depending on the given bounds.

Example 1:
    Input: root = [1,0,2], low = 1, high = 2
    Output: [1,null,2]

Example 2:
    Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
    Output: [3,2,null,1]    
    


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

'''
node.val < low => exclude this node and left subtree
node.val > high => exclude this node and right subtree
low <= node.val <= high => it'll stay
'''

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return None
            
            if node.val < low:
                return dfs(node.right)
            
            if high < node.val:
                return dfs(node.left)
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        
        return dfs(root)
