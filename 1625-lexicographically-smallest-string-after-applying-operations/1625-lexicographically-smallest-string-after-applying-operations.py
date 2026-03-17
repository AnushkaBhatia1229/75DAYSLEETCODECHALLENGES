class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        queue = deque([s])
        visited = set([s])
        smallest = s

        while queue:
            current = queue.popleft()

            # Update smallest string
            if current < smallest:
                smallest = current

            # Operation 1: Add 'a' to odd indices
            chars = list(current)
            for i in range(1, len(chars), 2):
                digit = (int(chars[i]) + a) % 10
                chars[i] = str(digit)

            added_string = "".join(chars)

            if added_string not in visited:
                visited.add(added_string)
                queue.append(added_string)

            # Operation 2: Rotate string by b positions
            rotated_string = current[-b:] + current[:-b]

            if rotated_string not in visited:
                visited.add(rotated_string)
                queue.append(rotated_string)

        return smallest