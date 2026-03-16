from typing import List

class Solution:
    def maxDistinctElements(self, numbers: List[int], k: int) -> int:
        
        # Step 1: Sort the numbers
        numbers.sort()

        distinct_elements = 0
        last_used_value = float('-inf')

        # Step 2: Traverse each number
        for current_number in numbers:

            minimum_possible = current_number - k
            maximum_possible = current_number + k

            # Case 1: Assign the smallest possible value
            if last_used_value < minimum_possible:
                last_used_value = minimum_possible
                distinct_elements += 1

            # Case 2: Assign the next possible value
            elif last_used_value < maximum_possible:
                last_used_value = last_used_value + 1
                distinct_elements += 1

        # Step 3: Return result
        return distinct_elements