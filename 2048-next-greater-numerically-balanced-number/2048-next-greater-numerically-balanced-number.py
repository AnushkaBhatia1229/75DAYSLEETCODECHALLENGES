class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        digits = [1, 2, 3, 4, 5, 6]
        balanced_numbers = set()
        balanced_numbers.add(1224444)

        for r in range(1, len(digits) + 1):
            for comb in itertools.combinations(digits, r):
                s = []
                total_len = 0
                for d in comb:
                    s += [str(d)] * d
                    total_len += d
                if total_len > 7:
                    continue

                for p in set(itertools.permutations(s)):
                    num = int(''.join(p))
                    if num < 1224444:
                        balanced_numbers.add(num)

        for b in sorted(balanced_numbers):
            if b > n:
                return b

        return -1