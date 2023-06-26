# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution(object):
    def subsets(self, nums):
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decide if you'll include nums[i] or not
            # including it
            subset.append(nums[i])
            dfs(i + 1)

            # not including it
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


nums = [1, 2, 3]
sol = Solution()
# print in reverse order
print(sol.subsets(nums)[::-1])
