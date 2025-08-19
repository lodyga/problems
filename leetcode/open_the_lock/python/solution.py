from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """
        Time complexity: O(1)
            O(10**4) -> O(1) 
        Auxiliary space complexity: O(1)
        Tags: backtracking, bfs, iteration
        """
        if target == "0000":
            return 0
        elif "0000" in deadends:
            return - 1

        visited = set(deadends)
        queue = deque([("0000", 0)])

        def get_next_codes(code):
            code_list = []

            for index in range(4):
                for inc in (-1, 1):
                    digit = str((int(code[index]) + inc) % 10)
                    code_list.append(code[:index] + digit + code[index + 1:])
            return code_list

        while queue:
            code, turns = queue.popleft()

            for next_code in get_next_codes(code):
                if next_code == target:
                    return turns + 1
                elif next_code not in visited:
                    visited.add(next_code)
                    queue.append((next_code, turns + 1))

        return -1


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """
        Time complexity: O(1)
            O(10**4) -> O(1) 
        Auxiliary space complexity: O(1)
        Tags: backtracking, bfs, iteration
        """
        if target == "0000":
            return 0
        elif "0000" in deadends:
            return - 1

        visited = set(deadends)
        queue = deque(["0000"])

        def get_next_codes(code):
            code_list = []

            for index in range(4):
                for inc in (-1, 1):
                    digit = str((int(code[index]) + inc) % 10)
                    code_list.append(code[:index] + digit + code[index + 1:])
            return code_list

        turns = 0
        while queue:
            for _ in range(len(queue)):
                code = queue.popleft()

                for next_code in get_next_codes(code):
                    if next_code == target:
                        return turns + 1
                    elif next_code not in visited:
                        visited.add(next_code)
                        queue.append(next_code)
            
            turns += 1

        return -1


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6)
print(Solution().openLock(["8888"], "0009") == 1)
print(Solution().openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1)
print(Solution().openLock(["0000"], "8888") == -1)
print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0000") == 0)