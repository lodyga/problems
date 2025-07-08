from collections import deque


class Solution:
    def canReach(self, number: str, min_jump: int, max_jump: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bfs
        """
        queue = deque([0])
        farthest = 0

        while queue:
            index = queue.popleft()
            start = max(index + min_jump, farthest + 1)
            end = min(index + max_jump + 1, len(number))

            for index in range(start, end):
                if number[index] == "0":
                    queue.append(index)
                    if index == len(number) - 1:
                        return True

            farthest = end - 1

        return False


class Solution:
    def canReach(self, number: str, min_jump: int, max_jump: int) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with tabulation as hash set
        """
        spots = set([0])
        
        while spots:
            next_spots = set()
            
            for spot in spots:
                for index in range(min_jump, max_jump + 1):
                    next_index = spot + index
                    if (
                        next_index < len(number) and 
                        number[next_index] == "0"
                    ):
                        next_spots.add(next_index)
                        if next_index == len(number) - 1:
                            return True

            spots = next_spots - spots
        
        return False


print(Solution().canReach("011010", 2, 3) == True)
print(Solution().canReach("01101110", 2, 3) == False)
print(Solution().canReach("01000110110", 2, 3) == True)