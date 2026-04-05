class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [(curNum + extraCandies) >= maxCandies for curNum in candies]