class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        week = 0
        
        while n > 0:
            # har week ka starting amount
            day_amount = 1 + week
            
            for day in range(7):
                if n == 0:
                    break
                ans += day_amount
                day_amount += 1
                n -= 1
            
            week += 1
        
        return ans