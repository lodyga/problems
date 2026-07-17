from collections import deque


class Solution:
    def canReach(self, text: str, min_jump: int, max_jump: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: bfs, iteration
        """
        if text[-1] == "1":
            return False

        N = len(text)
        queue = deque([0])
        min_start = 0

        while queue:
            idx = queue.popleft()
            start = max(idx + min_jump, min_start)
            end = min(idx + max_jump + 1, N)

            for idx in range(start, end):
                if text[idx] == "0":
                    queue.append(idx)

                    if idx == N - 1:
                        return True

            min_start = end

        return False


class Solution:
    def canReach(self, text: str, min_jump: int, max_jump: int) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        UPPER_BOUND = 10**9 + 7
        N = len(text)
        memo = [-1] * N
        memo[-1] = 1

        def dfs(idx: int) -> int:
            if memo[idx] != -1:
                return memo[idx]

            res = UPPER_BOUND
            jump_bound = min(idx + max_jump + 1, N)

            for jump_idx in range(idx + min_jump, jump_bound):
                if text[jump_idx] == "0":
                    res = min(res, dfs(jump_idx))

            memo[idx] = res
            return res

        return dfs(0) == 1


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

        N = len(text)
        jump_spots = set([0])

        while jump_spots:
            next_jump_spots = set()

            for idx in jump_spots:
                for spot in range(idx + min_jump, idx + max_jump + 1):
                    if (
                        spot < N and
                        text[spot] == "0"
                    ):
                        next_jump_spots.add(spot)
                        if spot == N - 1:
                            return True

            jump_spots = next_jump_spots - jump_spots

        return False


print(Solution().canReach("011010", 2, 3) == True)
print(Solution().canReach("01101110", 2, 3) == False)
print(Solution().canReach("01000110110", 2, 3) == True)
print(Solution().canReach("011111000111000001011111010", 6, 8) == True)
