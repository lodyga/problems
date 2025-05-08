class Solution:
    def findContentChildren(self, greed_list: list[int], cookies: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        greed_list.sort()
        greed_index = len(greed_list) - 1
        cookies.sort()
        cookie_index = len(cookies) - 1
        content_count = 0

        while greed_index >= 0 and cookie_index >= 0:
            if cookies[cookie_index] >= greed_list[greed_index]:
                content_count += 1
                cookie_index -= 1
            greed_index -= 1
        
        return content_count


print(Solution().findContentChildren([1, 2, 3], [1, 1]), 1)
print(Solution().findContentChildren([1, 2], [1, 2, 3]), 2)
print(Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]), 2)