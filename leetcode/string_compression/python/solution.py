class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: two pointers
        """
        prev_char = None
        chars.append(None)
        counter = 0
        left = 0

        for char in chars:
            if char == prev_char:
                counter += 1
                continue

            if counter > 1:
                for digit in str(counter):
                    chars[left] = digit
                    left += 1

            if char:
                chars[left] = char

            left += 1
            prev_char = char
            counter = 1

        chars.pop()
        return chars
        return left - 1


print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]) == ["a", "2", "b", "2", "c", "3", "c"])
print(Solution().compress(["a"]) == ["a"])
print(Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == ["a", "b", "1", "2", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
print(Solution().compress(["a", "a", "a", "b", "b", "a", "a"]) == ["a", "3", "b", "2", "a", "2", "a"])
print(Solution().compress(["v", "r", "r", "r", "r", "r", "r", "r", "r", "r"]) == ["v", "r", "9", "r", "r", "r", "r", "r", "r", "r"])
print(Solution().compress(["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == ["a", "1", "0", "0", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"])
