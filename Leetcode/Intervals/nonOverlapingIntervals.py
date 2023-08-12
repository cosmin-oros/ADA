# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals
# you need to remove to make the rest of the intervals non-overlapping.

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res


intervals = [[1,2],[2,3],[3,4],[1,3]]
sol = Solution()
print(sol.eraseOverlapIntervals(intervals))