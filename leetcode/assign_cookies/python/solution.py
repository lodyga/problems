class Solution:
    def findContentChildren(self, greed_list: list[int], cookies: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
            A: two pointers
        """
        greed_list.sort()
        cookies.sort()
        g_index = 0
        c_index = 0
        counter = 0

        while (
            g_index < len(greed_list) and
            c_index < len(cookies)
        ):
            greed = greed_list[g_index]
            cookie = cookies[c_index]

            if greed <= cookie:
                counter += 1
                g_index += 1

            c_index += 1

        return counter


print(Solution().findContentChildren([1, 2, 3], [1, 1]) == 1)
print(Solution().findContentChildren([1, 2], [1, 2, 3]) == 2)
print(Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]) == 2)
