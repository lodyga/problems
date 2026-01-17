from collections import deque


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
        deadend_set = set(tuple(int(digit) for digit in deadend) for deadend in deadends)
        target = tuple(int(digit) for digit in target)
        
        if (
            (0, 0, 0, 0) in deadend_set or 
            target in deadend_set
        ):
            return -1

        def bfs() -> int:
            queue = deque([(0, 0, 0, 0)])
            turns = 0

            while queue:
                for _ in range(len(queue)):
                    code = queue.popleft()
                
                    if code == target:
                        return turns
                    
                    code = list(code)

                    for i in range(4):
                        for j in (-1, 1):
                            code[i] = (code[i] + j) % 10
                            tup_code = tuple(code)
            
                            if tup_code not in deadend_set:
                                queue.append(tup_code)
                                deadend_set.add(tup_code)

                            code[i] = (code[i] - j) % 10
                
                turns += 1
            
            return -1

        return bfs()


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6)
print(Solution().openLock(["8888"], "0009") == 1)
print(Solution().openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1)
print(Solution().openLock(["0000"], "8888") == -1)
print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0000") == 0)
