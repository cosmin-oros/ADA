# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
# search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            # // will return an int
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
sol = Solution()
print(sol.search(nums, target))
