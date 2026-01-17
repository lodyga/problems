from collections import deque


class Solution:
    def canReach(self, text: str, min_jump: int, max_jump: int) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: bottom-up
        """
        if text[-1] == "1":
            return False

        jump_spots = set([0])

        while jump_spots:
            next_jump_spots = set()

            for index in jump_spots:
                for spot in range(index + min_jump, index + max_jump + 1):
                    if (
                        spot < len(text) and
                        text[spot] == "0"
                    ):
                        next_jump_spots.add(spot)
                        if spot == len(text) - 1:
                            return True

            jump_spots = next_jump_spots - jump_spots

        return False


class Solution:
    def canReach(self, text: str, min_jump: int, max_jump: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: bfs, iteration, level-order traversal
        """
        if text[-1] == "1":
            return False

        queue = deque([0])
        min_start = 0

        while queue:
            index = queue.popleft()
            start = max(index + min_jump, min_start + 1)
            end = min(index + max_jump, len(text) - 1)

            for index in range(start, end + 1):
                if text[index] == "0":
                    queue.append(index)
                    if index == len(text) - 1:
                        return True

            min_start = end

        return False


print(Solution().canReach("011010", 2, 3) == True)
print(Solution().canReach("01101110", 2, 3) == False)
print(Solution().canReach("01000110110", 2, 3) == True)
print(Solution().canReach("011111000111000001011111010", 6, 8) == True)
