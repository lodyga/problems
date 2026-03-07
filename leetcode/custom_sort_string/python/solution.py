class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bucket sort
        """
        order_position_by_char = [-1] * 26
        ordered_chars = [""] * 26
        unordered_chars = []

        for index, char in enumerate(order):
            letter_index = ord(char) - ord("a")
            order_position_by_char[letter_index] = index

        for char in s:
            letter_index = ord(char) - ord("a")
            index = order_position_by_char[letter_index]

            if index == -1:
                unordered_chars.append(char)
            else:
                ordered_chars[index] = (
                    ordered_chars[index] + char
                )

        return "".join(ordered_chars) + "".join(unordered_chars)


print(Solution().customSortString("cba", "abcd") == "cbad")
print(Solution().customSortString("bcafg", "abcd") == "bcad")
