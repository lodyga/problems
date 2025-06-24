class Solution:
    def findDifferentBinaryString(self, numbers: list[str]) -> str:
        """
        Time complexity: O(n^2)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        number_set = set(numbers)
        number = []

        def dfs(index):
            if len(number) == len(numbers[0]):
                full_number = "".join(number)
                if full_number in number_set:
                    return
                else:
                    return full_number
        
            for digit in "01":
                number.append(digit)
                full_number = dfs(index + 1)
                if full_number:
                    return full_number
                number.pop()

        return dfs(0)


print(Solution().findDifferentBinaryString(["0"]), "1")
print(Solution().findDifferentBinaryString(["01", "10"]), "00")
print(Solution().findDifferentBinaryString(["00", "01"]), "10")
print(Solution().findDifferentBinaryString(["111", "011", "001"]), "000")