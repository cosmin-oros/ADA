# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the
# start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an
# interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.

class Solution(object):
    def insert(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res


intervals = [[1, 3],[6, 9]]
newInterval = [2 ,5]
sol = Solution()
print(sol.insert(intervals, newInterval))
