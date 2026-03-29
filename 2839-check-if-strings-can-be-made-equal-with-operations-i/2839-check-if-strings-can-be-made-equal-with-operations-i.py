class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1, s2 = list(s1), list(s2)

        if s1[0] != s2[0]:
            s1[0], s1[2] = s1[2], s1[0]

        if s1[0] != s2[0]:
            return False
        else:
            if s1[2] != s2[2]:
                return False
            else:
                if s1[1] != s2[1]:
                    s1[1], s1[3] = s1[3], s1[1]

                if s1[1] != s2[1]:
                    return False
                else:
                    return s1[3] == s2[3]