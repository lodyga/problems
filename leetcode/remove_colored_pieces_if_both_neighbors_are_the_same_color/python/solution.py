class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        def find_triplet(left, letter):
            for index in range(left, len(colors) - 1):
                if colors[index - 1] == colors[index] == colors[index + 1] == letter:
                    index += 1
                    return index
            return 0
        
        left_a = 1
        left_b = 1
        
        while True:
            left_a = find_triplet(left_a, "A")
            if left_a == 0:
                return False

            left_b = find_triplet(left_b, "B")
            if left_b == 0:
                return True


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        counter = 0
        for right in range(len(colors)):
            if colors[right] != colors[left]:
                left = right
                continue
            if right - left + 1 < 3:
                continue
            counter += 1 if colors[left] == "A" else -1
        return counter > 0


print(Solution().winnerOfGame("AAABABB") == True)
print(Solution().winnerOfGame("AA") == False)
print(Solution().winnerOfGame("ABBBBBBBAAA") == False)