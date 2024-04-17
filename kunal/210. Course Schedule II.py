import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from curses.ascii import SO
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def generateInDegreeMap(
        self, numCourses: int, prerequisites: List[List[int]], inDegreeMap: Dict
    ) -> None:
        for num in range(numCourses):
            inDegreeMap[num] = 0

        for course, prerequisite in prerequisites:
            inDegreeMap[course] += 1

    def generateOutDegreeMap(
        self, numCourses: int, prerequisites: List[List[int]], outDegreeMap: Dict
    ) -> None:
        for num in range(numCourses):
            outDegreeMap[num] = []

        for course, prerequisite in prerequisites:
            outDegreeMap[prerequisite].append(course)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegreeMap = {}
        outDegreeMap = {}

        self.generateInDegreeMap(numCourses, prerequisites, inDegreeMap)
        self.generateOutDegreeMap(numCourses, prerequisites, outDegreeMap)

        queue = deque()

        # Fill all the 0 inDegree in queue
        for (
            course,
            inDegree,
        ) in (
            inDegreeMap.copy().items()
        ):  # Cannot iterate and modify a mutable object at the same time, hence iterate on copy
            if inDegree == 0:
                inDegreeMap.pop(course)
                queue.append(course)

        ans = []

        # Keep assigning order till you exhaust all courses
        while queue:
            prerequisite = queue.popleft()
            ans.append(prerequisite)

            for course in outDegreeMap[prerequisite]:
                inDegreeMap[course] -= 1
                if inDegreeMap[course] == 0:
                    inDegreeMap.pop(course)
                    queue.append(course)

        # Cycle exists, meaning no preceuisite course exists with inDegree 0 to break the cycle
        if len(inDegreeMap) != 0:
            return []
        else:
            return ans


print(Solution().findOrder(2, [[1, 0]]))
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution().findOrder(1, []))
