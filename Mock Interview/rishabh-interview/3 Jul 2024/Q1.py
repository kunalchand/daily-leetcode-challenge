"""
997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/

In a town, there are n people labeled from 1 to n. 
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

a -> b

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. 
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

n = 1, trust = [] => 1

a 
b   d
c 

Example 1:
    Input: n = 2, trust = [[1,2]]
    Output: 2
    
    1: []
    2: [1]

Example 2:
    Input: n = 3, trust = [[1,3],[2,3]]
    Output: 3
    
    3: [1, 2]
    1: []
    2: []

Example 3:
    Input: n = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1
    
    1: [3]
    2: []
    3: [1]
    
    

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
    '''
    Approach: make a person -> followers map
    find potential candidate (he would have n-1 followers and should not be present in any of the followers list)
    verify that candidate
    '''
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return n

        p_f = defaultdict(list)     # person -> [list of followeres who trust this person]
        
        # make map      
        for a, b in trust:
            p_f[b].append(a)
            
        # find candidate
        candidate = -1
        for k, v in p_f.items():
            if len(v) == n - 1:
                candidate = k
        
        # verify if candidate can be town judge or not
        for k, v in p_f.items():
            if candidate in v or candidate == -1:
                return -1
                
        return candidate
                
        
    '''
    APPROACH: graph, edge direction represents trust
    create indegree(# of edegs entering a node) 
    and outdegree(# of edges going out from a node) arrays
    town-judge node will have other nodes pointing to it, 
    and no edge will go out from it (t-j trusts no one)
    TIME: O(N)
    SPACE: O(N)
    '''
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        # if indegree of a node is (n-1) and 
        # outdegree of a node is 0 then it's a town judge
        indegree = [0 for _ in range(n + 1)] 
        outdegree = [0 for _ in range(n + 1)] 

        for a,b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(n + 1):
            if outdegree[i] == 0 and indegree[i] == n - 1: return i
        return -1