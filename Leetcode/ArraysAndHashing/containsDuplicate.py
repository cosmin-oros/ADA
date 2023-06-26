# Given an integer array nums, return true if any value appears at least twice in the array, and return false if
# every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


nums = [1, 2, 3, 1]
sol = Solution()
print(sol.containsDuplicate(nums))
