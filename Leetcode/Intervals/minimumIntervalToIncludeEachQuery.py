# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval
# starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it
# contains, or more formally righti - lefti + 1.
#
# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i
# such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.
#
# Return an array containing the answers to the queries.
import heapq


class Solution(object):
    def minInterval(self, intervals, queries):
        intervals.sort()

        minHeap = []
        res, i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]


intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
sol = Solution()
print(sol.minInterval(intervals, queries))
