# Given an integer array nums that may contain duplicates, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                # copy
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res


nums = [1, 2, 2]
sol = Solution()
print(sol.subsetsWithDup(nums))
