class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # If two adjacent balloons same color
        # Then pop the one with less needed time
        l = res = 0

        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r

        return res
        