# You are given an integer array nums. You are initially positioned at the array's first index, and each element in
# the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.

class Solution(object):
    def canJump(self, nums):
        goal = len(nums) - 1

        # start from the end
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


nums = [2, 3, 1, 1, 4]
sol = Solution()
print(sol.canJump(nums))