# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?

class Solution(object):
    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p] # swap
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)


nums = [3, 2, 1, 5, 6, 4]
k = 2
sol = Solution()
print(sol.findKthLargest(nums, k))
