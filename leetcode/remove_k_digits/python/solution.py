class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: greedy
        """
        # monotonic increasing stack
        stack = []
        idxs_to_remove = []
        res = []
        start = 0

        for idx, num in enumerate(nums):
            while stack and stack[-1][0] > num:
                _, idx_to_remove = stack.pop()
                idxs_to_remove.append(idx_to_remove)
            else:
                stack.append((num, idx))

        idxs_to_remove = set(idxs_to_remove[: k])

        for idx, char in enumerate(nums):
            if k and idx in idxs_to_remove:
                k -= 1
                continue

            res.append(char)

        while k and res:
            res.pop()
            k -= 1

        while start < len(res) and res[start] == "0":
            start += 1

        res = "".join(res[start:])
        
        return "0" if res == "" else res


print(Solution().removeKdigits("1432219", 3) == "1219")
print(Solution().removeKdigits("10200", 1) == "200")
print(Solution().removeKdigits("10", 2) == "0")
print(Solution().removeKdigits("12345", 2) == "123")
print(Solution().removeKdigits("54321", 2) == "321")
print(Solution().removeKdigits("9", 1) == "0")
print(Solution().removeKdigits("112", 1) == "11")
print(Solution().removeKdigits("1173", 2) == "11")
print(Solution().removeKdigits("10", 1) == "0")
print(Solution().removeKdigits("33526221184202197273", 19) == "0")
print(Solution().removeKdigits("52660469", 2) == "260469")
