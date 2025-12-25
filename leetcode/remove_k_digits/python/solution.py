class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: greedy
        Fails 35 / 43
        """
        if len(nums) == k:
            return "0"

        # monotonic increasing stack
        stack = []
        length = len(nums) - k

        for index, num in enumerate(nums):
            if not stack or stack[-1] <= num:
                stack.append(num)
                continue

            while stack and stack[-1] >= num:
                stack.pop()
                k -= 1
                if k == 0:
                    while index < len(nums) and nums[index] == "0":
                        index += 1
                    res = "".join(stack) + nums[index:]
                    return res if res else "0"
            stack.append(num)

        return "".join(stack[: length])


class Solution:
    def removeKdigits(self, numbers: str, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: two pointers
        """
        if len(numbers) == k:
            return "0"
        
        # monotonic increasing stack
        stack = []

        for number in numbers:
            while (
                k and stack and
                stack[-1] > number
            ):
                stack.pop()
                k -= 1
            stack.append(number)

        right = len(stack) - k
        
        left = 0
        while left < len(stack) and stack[left] == "0":
            left += 1

        result = "".join(stack[left: right])
        return result if result else "0"


print(Solution().removeKdigits("12345", 2) == "123")
print(Solution().removeKdigits("54321", 2) == "321")
print(Solution().removeKdigits("1432219", 3) == "1219")
print(Solution().removeKdigits("10200", 1) == "200")
print(Solution().removeKdigits("10", 2) == "0")
print(Solution().removeKdigits("9", 1) == "0")
print(Solution().removeKdigits("112", 1) == "11")
print(Solution().removeKdigits("1173", 2) == "11")
print(Solution().removeKdigits("10", 1) == "0")
print(Solution().removeKdigits("33526221184202197273", 19) == "0")
