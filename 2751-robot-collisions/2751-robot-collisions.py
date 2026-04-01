class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        # Step 1: sort indices based on positions
        indices = list(range(n))
        indices.sort(key=lambda i: positions[i])

        stack = []

        # Step 2: process robots
        for idx in indices:
            if directions[idx] == 'R':
                stack.append(idx)
            else:
                # moving left
                while stack and healths[idx] > 0:
                    top = stack.pop()

                    if healths[top] > healths[idx]:
                        healths[top] -= 1
                        healths[idx] = 0
                        stack.append(top)

                    elif healths[top] < healths[idx]:
                        healths[idx] -= 1
                        healths[top] = 0

                    else:
                        healths[idx] = 0
                        healths[top] = 0

        # Step 3: collect survivors
        result = []
        for i in range(n):
            if healths[i] > 0:
                result.append(healths[i])

        return result