class Solution:
    def partitionLabels(self, text: str) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: greedy
        """
        last_indexes = {}

        for index, letter in enumerate(text):
            last_indexes[letter] = index

        part_lens = []
        right = 0
        part_len = 0

        for left, letter in enumerate(text):
            right = max(right, last_indexes[letter])
            part_len += 1

            if left == right:
                part_lens.append(part_len)
                part_len = 0

        return part_lens


print(Solution().partitionLabels("ababcc") == [4, 2])
print(Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8])
print(Solution().partitionLabels("eccbbbbdec") == [10])
