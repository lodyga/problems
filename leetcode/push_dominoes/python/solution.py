class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: greedy
        """
        stack = []
        r_idx = 0

        for domino in dominoes:
            if domino == "R":
                stack.append((domino, 0))
                r_idx = 1

            elif domino == "L":
                r_idx = 0
                idx = 0

                while (
                    stack and stack[-1][0] == "." and
                    stack[-1][1] > idx
                ):
                    stack.pop()
                    idx += 1

                while (
                    stack and stack[-1][0] == "R" and
                    stack[-1][1] > idx
                ):
                    if stack[-1][1] == idx + 1:
                        stack.pop()
                        stack.append((".", -1))
                        break
                    stack.pop()
                    idx += 1

                for _ in range(idx + 1):
                    stack.append(("L", -1))

            elif domino == ".":
                if r_idx:
                    stack.append(("R", r_idx))
                    r_idx += 1
                else:
                    stack.append((".", len(dominoes)))

        return "".join(direction for (direction, _) in stack)


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: gredy, Multi-source BFS
        """
        from collections import deque
        doms = list(dominoes)
        q = deque()

        for idx, domino in enumerate(dominoes):
            if domino != ".":
                q.append((domino, idx))

        while q:
            domino, idx = q.popleft()

            if (
                domino == "L" and
                idx > 0 and
                doms[idx - 1] == "."
            ):
                doms[idx - 1] = "L"
                q.append(("L", idx - 1))

            elif (
                domino == "R" and
                idx + 1 < len(doms) and
                doms[idx + 1] == "."
            ):
                if (q and q[0] == ("L", idx + 2)):
                    q.popleft()
                else:
                    doms[idx + 1] = "R"
                    q.append(("R", idx + 1))

        return "".join(doms)


print(Solution().pushDominoes("RR.L") == "RR.L")
print(Solution().pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL..")
