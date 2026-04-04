class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        # Minimum Length Iteration
        i = 0
        res = ""
        while i < m and i < n:
            res += word1[i]
            res += word2[i]
            i += 1
        # Iteration on Remaining Word
        while i < n:
            res += word2[i]
            i += 1
        while i < m:
            res += word1[i]
            i += 1
        return res