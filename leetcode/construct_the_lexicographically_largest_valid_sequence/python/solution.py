class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: backtracking
        """
        if n == 1:
            return [1]

        seq_len = n*2 - 1
        seq = [0] * seq_len
        seq[0] = n
        seq[n] = n
        used = [False] * (n - 1)
        res = []

        def backtrack(idx):
            nonlocal res
            if all(used):
                res = seq.copy()
                return

            for num in range(n - 1, 0, -1):
                if seq[idx]:
                    backtrack(idx + 1)
                    return

                elif (
                    used[num - 1] or
                    num > 1 and (idx + num >= seq_len or seq[idx + num])
                ):
                    continue

                seq[idx] = num
                used[num - 1] = True

                if num > 1:
                    seq[idx + num] = num

                if not res:
                    backtrack(idx + 1)

                used[num - 1] = False
                seq[idx] = 0

                if num > 1:
                    seq[idx + num] = 0

        backtrack(1)
        return res


print(Solution().constructDistancedSequence(1) == [1])
print(Solution().constructDistancedSequence(2) == [2, 1, 2])
print(Solution().constructDistancedSequence(4) == [4, 2, 3, 2, 4, 3, 1])
print(Solution().constructDistancedSequence(6) == [6, 4, 2, 5, 2, 4, 6, 3, 5, 1, 3])
print(Solution().constructDistancedSequence(3) == [3, 1, 2, 3, 2])
print(Solution().constructDistancedSequence(5) == [5, 3, 1, 4, 3, 5, 2, 4, 2])
print(Solution().constructDistancedSequence(7) == [7, 5, 3, 6, 4, 3, 5, 7, 4, 6, 2, 1, 2])
