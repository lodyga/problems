class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: iteration
        """
        srcs = set()
        dsts = set()

        for src, dst in paths:
            srcs.add(src)
            dsts.add(dst)

        for dst in dsts:
            if dst not in srcs:
                return dst
        return ""


print(Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]) == "Sao Paulo")
print(Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]) == "A")
print(Solution().destCity([["A", "Z"]]) == "Z")
