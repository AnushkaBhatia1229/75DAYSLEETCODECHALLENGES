class Solution:
    def helper(self, x, y, power, coins, n, m, dp):
        if x >= n or y >= m:
            return float("-inf")

        if dp[x][y][power] != None:
            return dp[x][y][power]

        if x == n - 1 and y == m - 1:
            if coins[x][y] < 0 and power > 0:
                return 0
            return coins[x][y]

        if coins[x][y] >= 0:
            right = coins[x][y] + self.helper(x, y + 1, power, coins, n, m, dp)
            down = coins[x][y] + self.helper(x + 1, y, power, coins, n, m, dp)

        else:
            if power > 0:
                right = self.helper(x, y + 1, power - 1, coins, n, m, dp)
                right_most = coins[x][y] + self.helper(x, y + 1, power, coins, n, m, dp)

                down = self.helper(x + 1, y, power - 1, coins, n, m, dp)
                down_most = coins[x][y] + self.helper(x + 1, y, power, coins, n, m, dp)

                dp[x][y][power] = max(right, right_most, down, down_most)
                return dp[x][y][power]

            else:
                right = coins[x][y] + self.helper(x, y + 1, power, coins, n, m, dp)
                down = coins[x][y] + self.helper(x + 1, y, power, coins, n, m, dp)

        dp[x][y][power] = max(right, down)
        return dp[x][y][power]

    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])

        dp = [[[None for _ in range(3)] for _ in range(m)] for _ in range(n)]

        return self.helper(0, 0, 2, coins, n, m, dp)