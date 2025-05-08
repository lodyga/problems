class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        origin_cities = set()
        destination_cities = set()

        for origin_city, destination_city in paths:
            origin_cities.add(origin_city)
            destination_cities.add(destination_city)

        for destination_city in destination_cities:
            if destination_city not in origin_cities:
                return destination_city


print(Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]), "Sao Paulo")
print(Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]), "A")
print(Solution().destCity([["A", "Z"]]), "Z")
