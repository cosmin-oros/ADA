# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
# Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output
# will be given as a signed integer type. They should not affect your implementation, as the integer's internal
# binary representation is the same, whether it is signed or unsigned. In Java, the compiler represents the signed
# integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3
# and the output represents the signed integer -1073741825.

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

sol = Solution()
n = 0o0000010100101000001111010011100
print(sol.reverseBits(n))