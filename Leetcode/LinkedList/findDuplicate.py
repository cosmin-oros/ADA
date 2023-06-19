# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution(object):
    def findDuplicate(self, nums):
        s, f = 0, 0

        while True:
            # slow moves one step, fast two steps
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s2 = 0

        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s


sol = Solution()
nums = [1, 3, 4, 2, 2]
print(sol.findDuplicate(nums))