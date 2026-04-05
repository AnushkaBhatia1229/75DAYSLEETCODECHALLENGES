class Solution:
    def judgeCircle(self, moves: str) -> bool:
        f = Counter(moves)
        return f['U'] == f['D'] and f['L'] == f['R']