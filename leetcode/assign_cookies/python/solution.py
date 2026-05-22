class Solution:
    def findContentChildren(self, greed_list: list[int], cookies: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: two pointers, sorting
        """
        greed_list.sort()
        cookies.sort()
        res = 0

        for cookie in cookies:
            if res == len(greed_list):
                break
            
            if greed_list[res] <= cookie:
                res += 1

        return res


print(Solution().findContentChildren([1, 2, 3], [1, 1]) == 1)
print(Solution().findContentChildren([1, 2], [1, 2, 3]) == 2)
print(Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]) == 2)
