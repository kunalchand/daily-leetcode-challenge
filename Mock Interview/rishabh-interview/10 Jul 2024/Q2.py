"""
452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

       ---     --------------
-----------
  -------------   --------------------
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

[2 6] [4 6] 

                 ##
[4 6] [ 7 12 ]

[1 2] [3 4]

[1 3] [3 4]


                           

Example 1:
    Input: points = [[10,16],[2,8],[1,6],[7,12]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
    - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
    - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
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


class Solution:
    # [[10,16],[2,8],[1,6],[7,12]]
    # [1,6] [2,8] [7,12] [10,16]
    # 2,6 [7,12]
    '''
    Approach: Intervals
    merge line segments into overlapping segments. Eg: [1,4], [2,5] => [2,4]
    count distinct line segments => # of arrows
    note that they need to be sorted acc to their end times
    Time: O(n * log n), sorting
    Space: O(1)
    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        def find_overlap(first_segment: List[int], second_segment: List[int]) -> List[int]:
            nonlocal arrow_count
            start, end = 0, 1
            overlap = []

            if second_segment[start] <= first_segment[end]:
            # if second_segment[start] <= first_segment[end] <= second_segment[end]:
                overlap.append(max(first_segment[start], second_segment[start]))
                overlap.append(min(first_segment[end], second_segment[end]))
                return overlap
            else:
                arrow_count += 1
                return second_segment
            
        points.sort(key = lambda x: x[1])       # sort by end time
        
        arrow_count = 1
        overlap = [points[0][0], points[0][1]]

        for i in range(1, len(points)):
            curr_point = points[i]
            if curr_point != points[i - 1]:
                overlap = find_overlap(overlap, curr_point)
            
        return arrow_count

    
    '''
    Approach: same as above, a bit cleaner code
    Time: O(n * log n), sorting
    Space: O(1)

    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])      # sort by end time

        start, end, arrow_count = 0, 1, 1
        boundary = points[0][end]

        for x_start, x_end in points:

            if boundary < x_start:
                arrow_count += 1
                boundary = x_end
            
        return arrow_count