class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list, hash set
            A: backtracking
        """
        binary = []
        bin_set = set(nums)
        bin_len = len(nums[0])

        def backtrack(index):
            if index == bin_len:
                missing = "".join(binary)
                return "" if missing in bin_set else missing

            for digit in "01":
                binary.append(digit)
                missing = backtrack(index + 1)
                if missing:
                    return missing
                binary.pop()

        return backtrack(0)


print(Solution().findDifferentBinaryString(["0"]) == "1")
print(Solution().findDifferentBinaryString(["01", "10"]) == "00")
print(Solution().findDifferentBinaryString(["00", "01"]) == "10")
print(Solution().findDifferentBinaryString(["111", "011", "001"]) == "000")
