"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones
and smash them together. Suppose the heaviest two stones have weights x and y with x <= y.
The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

"""

# from collections import heapq
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones or len(stones) == 0:
            return None
        if len(stones) == 1:
            return stones[-1]
        heap = []  ##maxheap
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            currstone1 = abs(heapq.heappop(heap))
            currstone2 = abs(heapq.heappop(heap))
            if currstone1 != currstone2:
                lessValue = min(currstone1, currstone2)
                moreValue = max(currstone1, currstone2)
                diff = moreValue - lessValue
                heapq.heappush(heap, -diff)
        if heap:
            return -heapq.heappop(heap)
        else:
            return 0
