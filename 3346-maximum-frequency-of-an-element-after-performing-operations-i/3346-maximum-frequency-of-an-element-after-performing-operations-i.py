class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maximum = max(nums) + k+1
        count = [0] * maximum

        for n in nums:
            count[n] += 1

        for i in range(1, maximum):
            count[i] = count[i] + count[i-1]

        res = 0
        for i in range(1,maximum):
            left = max(0, i-k)
            right = min(maximum-1, i+k)
            leftmost = max(left-1, 0)
            total = count[right] - count[leftmost]
            freq = count[i] - count[i-1]
            res = max(res, freq + min(numOperations, total-freq)) 

        return res    

        