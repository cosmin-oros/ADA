# Given two integers a and b, return the sum of the two integers without using the operators + and -.

class Solution(object):
    def getSum(self, a, b):
        while b != 0:
            tmp = (a & b) << 1
            a = a ^ b
            b = tmp
        return a


a = 1
b = 2
sol = Solution()
print(sol.getSum(a, b))