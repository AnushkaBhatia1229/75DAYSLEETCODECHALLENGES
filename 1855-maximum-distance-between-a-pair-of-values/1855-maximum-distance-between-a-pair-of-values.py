class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0

        while i < n and j < m:
            if i > j:
                j = i

            if j < m and nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans