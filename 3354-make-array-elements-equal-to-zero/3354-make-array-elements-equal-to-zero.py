class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        pr = [nums[0]] * n
        su = [nums[-1]] * n

        for i in range(1, n):
            pr[i] = pr[i - 1] + nums[i]

        for i in range(n - 2, -1, -1):
            su[i] = su[i + 1] + nums[i]

        res = 0

        for i in range(n):
            if nums[i] == 0:
                if pr[i] == su[i]:
                    res += 2
                elif abs(pr[i] - su[i]) == 1:
                    res += 1

        return res
        