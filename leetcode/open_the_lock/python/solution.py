from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """
        Time complexity: O(1)
            O(10**4) -> O(1) 
        Auxiliary space complexity: O(1)
        Tags: backtracking, bfs, iteration
        """
        visited = set(deadends)
        if target == "0000":
            return 0
        elif "0000" in visited:
            return -1

        def bfs():
            turns = 0
            queue = deque(["0000"])
            
            while queue:
                for _ in range(len(queue)):
                    code = queue.popleft()
                    if code == target:
                        return turns

                    for index in range(4):
                        for j in {-1, 1}:
                            digit = str((int(code[index]) + j) % 10)
                            next_code = code[:index] + digit + code[index + 1:]
                            if next_code not in visited:
                                queue.append(next_code)
                                visited.add(next_code)
                
                turns += 1
            return False

        sol = bfs()
        return -1 if sol == False else sol


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6)
print(Solution().openLock(["8888"], "0009") == 1)
print(Solution().openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1)
print(Solution().openLock(["0000"], "8888") == -1)
print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0000") == 0)