class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        
        m = len(grid)
        n = len(grid[0])
        
        # Prefix and suffix matrices
        pref = [[1] * n for _ in range(m)]
        suff = [[1] * n for _ in range(m)]
        
        p = 1
        s = 1
        
        # Fill prefix and suffix
        for i in range(m):
            for j in range(n):
                pref[i][j] = p
                suff[m - 1 - i][n - 1 - j] = s
                
                p = (p * grid[i][j]) % MOD
                s = (s * grid[m - 1 - i][n - 1 - j]) % MOD
        
        # Construct result matrix
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                result[i][j] = (pref[i][j] * suff[i][j]) % MOD
        
        return result