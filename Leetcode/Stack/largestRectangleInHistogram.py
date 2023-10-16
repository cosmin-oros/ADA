# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.

class Solution(object):
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - start))
                start = index
            stack.append((start, h))

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea


heights = [2, 1, 5, 6, 2, 3]
sol = Solution()
print(sol.largestRectangleArea(heights))
