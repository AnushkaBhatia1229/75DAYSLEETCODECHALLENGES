class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()

        count = 0

        lastDy = None
        lastDx = None

        for (ax, ay), (bx, by) in zip(stockPrices, stockPrices[1:]):
            dy = by - ay
            dx = bx - ax

            if lastDy is None or lastDy * dx != dy * lastDx:
                count += 1

            lastDy = dy
            lastDx = dx

        return count