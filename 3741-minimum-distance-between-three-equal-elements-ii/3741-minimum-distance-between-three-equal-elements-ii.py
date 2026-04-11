class Solution:
    def minimumDistance(self, nums):
        n = len(nums)
        nxt = [-1] * n
        occur = {}
        ans = n + 1

        # Step 1: Fill next occurrence array
        for i in range(n - 1, -1, -1):
            if nums[i] in occur:
                nxt[i] = occur[nums[i]]
            occur[nums[i]] = i

        # Step 2: Find minimum distance for 3 equal elements
        for i in range(n):
            if nxt[i] != -1 and nxt[nxt[i]] != -1:
                ans = min(ans, nxt[nxt[i]] - i)

        # Step 3: Return result
        return -1 if ans == n + 1 else ans * 2