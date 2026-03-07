class DSU:
    def __init__(self, N: int) -> None:
        self.size = [1] * N
        self.parent = list(range(N))
        self.components = N

    def find(self, u: int) -> int:
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        elif self.size[pu] < self.size[pv]:
            (pu, pv) = (pv, pu)

        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        self.components -= 1
        return True


class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        """
        Failed
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
        """
        def get_dividers(num):
            dividers = set()

            for divider in range(2, int(num**0.5) + 10):
                if num % divider == 0:
                    a = divider
                    add_a = True

                    for d in dividers:
                        if a % d == 0:
                            add_a = False
                            break

                    if add_a:
                        dividers.add(a)

            return dividers

        dsu = DSU(len(nums))
        num_to_index = {num: index 
                        for index, num in enumerate(nums)}

        for num in nums:
            for divider in get_dividers(num):
                if num != divider:
                    dsu.union(num_to_index[num], num_to_index[divider])

        return dsu.components == 1

# [2, 3, (2, 3), 2]
print(Solution().canTraverseAllPairs([2, 3, 6]) == True)
print(Solution().canTraverseAllPairs([3, 9, 5]) == False)
# print(Solution().canTraverseAllPairs([4, 3, 12, 8]) == True)
