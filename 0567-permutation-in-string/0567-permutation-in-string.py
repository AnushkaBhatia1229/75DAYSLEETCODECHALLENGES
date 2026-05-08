class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1 abc acb bca
        s2 i+len(s1)
        eidbaooo eid

        map1
        a 1
        b 1
        c 1

        map2
        e 1
        i 1
        d 1
        """

        map1 = Counter(s1)

        for i in range(len(s2)):
            sub = s2[i:i + len(s1)]
            map2 = Counter(sub)

            if map1 == map2:
                return True

        return False