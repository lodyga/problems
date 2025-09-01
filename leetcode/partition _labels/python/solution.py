class Solution:
    def partitionLabels(self, text: str) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        letter_last_position = {}
        for index, letter in enumerate(text):
            letter_last_position[letter] = index

        partition_lengths = []
        counter = 0
        end = 0
        
        for index, letter in enumerate(text):
            counter += 1
            end = max(end, letter_last_position[letter])

            if index == end:
                partition_lengths.append(counter)
                counter = 0

        return partition_lengths


print(Solution().partitionLabels("ababcc") == [4, 2])
print(Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8])
print(Solution().partitionLabels("eccbbbbdec") == [10])