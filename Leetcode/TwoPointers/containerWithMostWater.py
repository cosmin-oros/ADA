# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
# the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        res = 0
        # use two pointers left and right
        l, r = 0, len(height) - 1

        while l < r:
            # the area is the len from right pointer to left pointer * the smallest of the two heights
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                # if they're equal it's the same thing if you shift the left or the right
                r -= 1

        return res


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))
