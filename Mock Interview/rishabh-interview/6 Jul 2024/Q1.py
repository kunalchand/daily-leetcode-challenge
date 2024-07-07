"""
419. Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', 
return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. 
In other words, they can only be made of the shape 1 x k (1 row, k columns) 
or k x 1 (k rows, 1 column), where k can be of any size. 
At least one horizontal or vertical cell separates between two battleships 
(i.e., there are no adjacent battleships).

Example 1:
    Input: board = 
    [
        [".","X",".","X"],
        [".","X",".","X"],
        ["X",".",".","X"]
        
        ]
        3
        
        X 0
        0 X
        
    Output: 2
    
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

'''

[".","X",".","X"],
[".","X",".","X"],
["X",".",".","X"]

'''

class Solution:
    def neighbor_is_x(self, row: int, col: int, board: List[List[str]]) -> bool:
        if board[row][col] == "X":
            return True
            
        return False
                
    
    def countBattleships(self, board: List[List[str]]) -> int:
    
        self.ROWS, self.COLS = len(board), len(board[0])
        b_count = 0
        
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if r-1 in range(self.ROWS) and c-1 in range(self.COLS):
                    if self.neighbor_is_x(r - 1, c - 1, board):
                        continue
                if board[r][c] == "X":
                    b_count += 1
                
            
        return b_count        
                        
                        
