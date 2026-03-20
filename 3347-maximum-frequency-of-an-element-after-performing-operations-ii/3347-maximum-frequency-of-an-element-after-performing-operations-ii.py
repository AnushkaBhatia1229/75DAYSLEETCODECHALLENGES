class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
       nums.sort()
       counter = Counter(nums)
       targets = set()

       for n in nums:
           targets.add(n)
           targets.add(n-k)
           targets.add(n+k)

       res = 0
       for target in targets:
            freq = counter[target]
            right = bisect.bisect_right(nums, target+k)
            left  = bisect.bisect_left(nums, target-k)
            res = max(res, freq + min(numOperations, right-left-freq))
       return res    
