class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: sorting, iteration
        """
        data = sorted((p, d, h, i)
                      for i, (p, h, d) in enumerate(zip(positions, healths, directions)))
        stack = []

        for _, d, h, i in data:
            if (
                stack and 
                stack[-1][0] == "R" and
                d == "L"
            ):
                prev_d, prev_h, prev_i = stack[-1]

                if prev_h == h:
                    stack.pop()
                elif prev_h > h:
                    stack.pop()
                    stack.append((prev_d, prev_h - 1, prev_i))
                elif prev_h < h:
                    is_alive = True
                    
                    while (
                        stack and 
                        stack[-1][0] == "R" and
                        d == "L" and 
                        h
                    ):
                        prev_h = stack[-1][1]

                        if prev_h == h:
                            stack.pop()
                            is_alive = False
                            break
                        elif prev_h < h:
                            stack.pop()
                            h -= 1
                        elif prev_h > h:
                            prev_d, prev_h, prev_i = stack.pop()
                            stack.append((prev_d, prev_h - 1, prev_i))
                            is_alive = False
                            break

                    if is_alive and h:
                        stack.append((d, h, i))

            else:
                stack.append((d, h, i))

        stack.sort(key=lambda x: x[2])
        return [h for _, h, _ in stack]


print(Solution().survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR") == [2, 17, 9, 15, 10])
print(Solution().survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], "RLRL") == [14])
print(Solution().survivedRobotsHealths([1, 2, 5, 6], [10, 10, 11, 11], "RLRL") == [])
print(Solution().survivedRobotsHealths([11, 44, 16], [1, 20, 17], "RLR") == [18])
print(Solution().survivedRobotsHealths([17, 24, 18], [1, 39, 30], "LLR") == [1, 38])
print(Solution().survivedRobotsHealths([34, 50, 42, 2], [6, 27, 17, 38], "LLRR") == [36])
