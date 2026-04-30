class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in nums_set:
                    curr_len += 1
                    curr_num += 1

                max_len = max(max_len, curr_len)

        return max_len


nums = [3,2,5,8,6,0,0,0,1]

nums_set = {3,2,5,8,6,0,1}
max_len = 4
curr_num = 3
curr_len = 4