class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        result = [[0 for _ in range(m - k + 1)] for _ in range(n - k + 1)]

        if k == 1:
            return result

        for r in range(n - k + 1):
            for c in range(m - k + 1):
                new_list = []

                for i in range(k):
                    for j in range(k):
                        new_list.append(grid[r + i][c + j])

                new_list.sort()

                diff = new_list[-1] - new_list[0]

                for i in range(1, len(new_list)):
                    if new_list[i] == new_list[i - 1]:
                        continue
                    diff = min(diff, new_list[i] - new_list[i - 1])

                result[r][c] = diff

        return result   