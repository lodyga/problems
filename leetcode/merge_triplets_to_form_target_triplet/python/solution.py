class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        target_a, target_b, target_c = target
        a_found = b_found = c_found = False
        
        for a, b, c in triplets:
            if (
                a > target_a or
                b > target_b or
                c > target_c
            ):
                continue
            
            if a == target_a:
                a_found = True
            if b == target_b:
                b_found = True
            if c == target_c:
                c_found = True
        
            if a_found and b_found and c_found:
                return True
        
        return False


print(Solution().mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) == True)
print(Solution().mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) == False)
print(Solution().mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]) == True)