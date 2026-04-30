from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[[-inf] * (k + 1) for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0

        for i in range(n):
            for j in range(m):
                for c in range(k + 1):
                    if dp[i][j][c] == -inf:
                        continue

                    if i + 1 < n:
                        nv = grid[i + 1][j]
                        nc = 1 if nv != 0 else 0
                        if nc + c <= k:
                            dp[i + 1][j][nc + c] = max(
                                dp[i + 1][j][nc + c],
                                dp[i][j][c] + nv
                            )

                    if j + 1 < m:
                        nv = grid[i][j + 1]
                        nc = 1 if nv != 0 else 0
                        if nc + c <= k:
                            dp[i][j + 1][nc + c] = max(
                                dp[i][j + 1][nc + c],
                                dp[i][j][c] + nv
                            )

        res = max(dp[-1][-1])
        return res if res != -inf else -1