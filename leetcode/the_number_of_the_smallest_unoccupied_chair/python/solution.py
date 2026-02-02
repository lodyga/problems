import heapq


class Solution:
    def smallestChair(self, times: list[list[int]], target_friend: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap, list
            A: sorting
        """
        N = len(times)
        friend_data = [(start, end, index)
                       for index, (start, end) in enumerate(times)]
        friend_data.sort()

        avaible_chairs = list(range(N))
        # heapq.heapify(avaible_chairs)
        # heap([(end, chair id), ])
        occupied_chars = []

        for start, end, friend_id in friend_data:
            while occupied_chars and occupied_chars[0][0] <= start:
                _, chair_id = heapq.heappop(occupied_chars)
                heapq.heappush(avaible_chairs, chair_id)

            chair_id = heapq.heappop(avaible_chairs)
            heapq.heappush(occupied_chars, (end, chair_id))

            if friend_id == target_friend:
                return chair_id



print(Solution().smallestChair([[1, 4], [2, 3], [4, 6]], 1) == 1)
print(Solution().smallestChair([[3, 10], [1, 5], [2, 6]], 0) == 2)
