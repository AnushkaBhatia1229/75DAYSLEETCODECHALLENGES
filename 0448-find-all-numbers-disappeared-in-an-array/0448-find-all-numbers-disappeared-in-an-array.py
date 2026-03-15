class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # Step 1: Mark visited numbers
        for number in nums:
            index = abs(number) - 1
            nums[index] = -1 * abs(nums[index])
        
        # Step 2: Find missing numbers
        result = []
        for index, number in enumerate(nums):
            if number > 0:
                result.append(index + 1)
        
        return result
        