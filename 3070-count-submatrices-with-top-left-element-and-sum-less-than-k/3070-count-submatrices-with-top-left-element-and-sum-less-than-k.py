from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        curr_row = [0] * COLS
        
        for row in range(ROWS):
            curr_val = 0
            
            for col in range(COLS):
                curr_val += grid[row][col]
                
                # Safe check: ensure index exists
                if col < len(curr_row) and curr_val + curr_row[col] <= k:
                    curr_row[col] += curr_val
                    res += 1
                else:
                    # truncate safely
                    curr_row = curr_row[:col]
                    break
        
        return res