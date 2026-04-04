class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        # Check if concatenation is same in both orders
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find GCD of lengths
        gcd_len = gcd(len(str1), len(str2))
        
        return str1[:gcd_len]
        