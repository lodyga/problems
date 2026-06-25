class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: iteration
        """
        src_cities = set()

        for src, _ in paths:
            src_cities.add(src)
        
        for _, dst in paths:
            if dst not in src_cities:
                return dst


print(Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]) == "Sao Paulo")
print(Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]) == "A")
print(Solution().destCity([["A", "Z"]]) == "Z")
