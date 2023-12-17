# You are given an integer array coins representing coins of different denominations and an integer amount
# representing a total amount of money.
#
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return 0.
#
# You may assume that you have an infinite number of each kind of coin.
#
# The answer is guaranteed to fit into a signed 32-bit integer.

class Solution(object):
    def change(self, amount, coins):
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]


amount = 5
coins = [1, 2, 5]
sol = Solution()
print(sol.change(amount, coins))