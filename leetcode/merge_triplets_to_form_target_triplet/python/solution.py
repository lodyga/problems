class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        t_a, t_b, t_c = target
        is_a = is_b = is_c = False

        for a, b, c in triplets:
            if a > t_a or b > t_b or c > t_c:
                continue

            is_a = is_a or a == t_a
            is_b = is_b or b == t_b
            is_c = is_c or c == t_c

            if is_a and is_b and is_c:
                return True

        return False


print(Solution().mergeTriplets(
    [[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) == True)
print(Solution().mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) == False)
print(Solution().mergeTriplets(
    [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]) == True)
