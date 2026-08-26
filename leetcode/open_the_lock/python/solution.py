from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """
        Time complexity: O(1)
            O(10**4) -> O(1) 
        Auxiliary space complexity: O(1)
        Tags:
            DS: array, hash set, string
            A: bfs, iteration, level-order traversal
        """
        deadend_set = set(deadends)

        if "0000" in deadend_set or target in deadend_set:
            return -1

        queue = deque(["0000"])
        deadend_set.add("0000")
        res = 0

        while queue:
            for _ in range(len(queue)):
                code = queue.popleft()

                if code == target:
                    return res

                for idx in range(4):
                    for dx in (-1, 1):
                        digit = ord(code[idx]) - ord('0')
                        new_digit = (digit + dx) % 10
                        new_code = (
                            code[: idx]
                            + chr(new_digit + ord('0'))
                            + code[idx + 1:]
                        )

                        if new_code in deadend_set:
                            continue

                        queue.append(new_code)
                        deadend_set.add(new_code)

            res += 1

        return -1


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """
        Time complexity: O(1)
            O(10**4) -> O(1) 
        Auxiliary space complexity: O(1)
        Tags:
            DS: array, tuple, string, hash set
            A: bfs, iteration, level-order traversal
        """
        deadend_set = set(tuple(int(digit) for digit in deadend)
                          for deadend in deadends)

        if (
            tuple(int(digit) for digit in target) in deadend_set
            or (0, 0, 0, 0) in deadend_set 
        ):
            return -1

        target = [int(digit) for digit in target]
        queue = deque([(0, 0, 0, 0)])
        res = 0

        while queue:
            for _ in range(len(queue)):
                code = list(queue.popleft())

                if code == target:
                    return res

                for idx in range(4):
                    for dx in (-1, 1):
                        code[idx] = (code[idx] + dx) % 10
                        tup_code = tuple(code)

                        if tup_code not in deadend_set:
                            queue.append(tup_code)
                            deadend_set.add(tup_code)

                        code[idx] = (code[idx] - dx) % 10

            res += 1

        return -1


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6)
print(Solution().openLock(["8888"], "0009") == 1)
print(Solution().openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1)
print(Solution().openLock(["0000"], "8888") == -1)
print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0000") == 0)
