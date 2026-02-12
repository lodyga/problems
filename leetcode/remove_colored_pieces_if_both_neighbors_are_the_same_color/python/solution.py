class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        N = len(colors)
        a_counter = 0
        b_counter = 0

        for index in range(1, N - 1):
            color = colors[index]
            if colors[index - 1] == color == colors[index + 1]:
                if color == "A":
                    a_counter += 1
                else:
                    b_counter += 1

        return a_counter > b_counter


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        prev = "Z"
        counter = 0
        a_counter = 0
        b_counter = 0

        for color in colors:
            if color == prev:
                counter += 1
            else:
                if counter >= 3:
                    if prev == "A":
                        a_counter += counter - 2
                    else:
                        b_counter += counter - 2
                prev = color
                counter = 1
        
        if counter >= 3:
            if prev == "A":
                a_counter += counter - 2
            else:
                b_counter += counter - 2

        return a_counter > b_counter


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 0
        counter = 0
        for right in range(len(colors)):
            if colors[right] != colors[left]:
                left = right
            elif right - left + 1 >= 3:
                counter += 1 if colors[left] == "A" else -1
        return counter > 0


print(Solution().winnerOfGame("AAABABB") == True)
print(Solution().winnerOfGame("AA") == False)
print(Solution().winnerOfGame("ABBBBBBBAAA") == False)
print(Solution().winnerOfGame("AAAABBBB") == False)
