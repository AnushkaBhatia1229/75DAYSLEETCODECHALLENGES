class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        def reverse(number):
            ans = 0
            while number != 0:
                rem = number % 10
                ans = ans * 10 + rem
                number = number // 10
            return ans
        
        ans = float('inf')
        last_seen = {}
        
        for i, val in enumerate(nums):
            if val in last_seen:
                ans = min(ans, i - last_seen[val])
            
            last_seen[reverse(val)] = i
        
        return -1 if ans == float('inf') else ans