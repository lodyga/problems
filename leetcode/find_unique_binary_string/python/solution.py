class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set, list
            A: backtracking
        """
        N = len(nums[0])
        bin_set = set(nums)
        binary = []

        def backtrack(idx: int) -> str:
            if idx == N:
                if "".join(binary) in bin_set:
                    return ""
                else:
                    return "".join(binary)

            binary.append("0")
            res = backtrack(idx + 1)

            if res:
                return res

            binary.pop()
            binary.append("1")
            res = backtrack(idx + 1)

            if res:
                return res

            binary.pop()
            return ""

        return backtrack(0)


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set, list
            A: backtracking
        """
        N = len(nums[0])
        bin_set = set(nums)
        binary = []

        def backtrack(idx: int) -> str:
            if idx == N:
                missing = "".join(binary)
                return "" if missing in bin_set else missing

            for char in "01":
                binary.append(char)
                missing = backtrack(idx + 1)
                
                if missing:
                    return missing
                
                binary.pop()
            
            return ""

        return backtrack(0)


print(Solution().findDifferentBinaryString(["01", "10"]) == "00")
print(Solution().findDifferentBinaryString(["00", "01"]) == "10")
print(Solution().findDifferentBinaryString(["111", "011", "001"]) == "000")
print(Solution().findDifferentBinaryString(["0"]) == "1")
