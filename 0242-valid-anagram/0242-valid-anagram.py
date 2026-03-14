class Solution(object):
    def isAnagram(self, s1, s2):
        # Run time O(n), Space O(26) = O(1)
        numberOfLetters = 26
        
        s1 = s1.lower()
        s2 = s2.lower()

        if (len(s1) != len(s2)):
            return False

        count = [0 for i in range(numberOfLetters)]

        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1

        for i in range(len(s2)):
            count[ord(s2[i]) - ord('a')] -= 1

        for i in range(numberOfLetters):
            if (count[i] != 0):
                return False

        return True