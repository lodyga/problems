import heapq


class Solution:
    def smallestChair(self, times: list[list[int]], target_friend: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        friends = [(start, end, friend_id) 
                   for friend_id, (start, end) in enumerate(times)]
        friends.sort()
        # friends_order = list(range(len(times)))
        # friends_order.sort(key=lambda i: times[i][0])
        # heap((friend leave time, chair index), ...) chairs currently occupied by friends
        occupied_chiars = []
        # heap(chair index, ) avaible chairs
        avaible_chairs = []
        min_chair = 0

        for friend in friends:
        # for friend_id in friends_order:
        #     friend = times[index]
            start, end, friend_id = friend
            
            while occupied_chiars and occupied_chiars[0][0] <= start:
                _, chair = heapq.heappop(occupied_chiars)
                heapq.heappush(avaible_chairs, chair)

            if not avaible_chairs:
                chair_index = heapq.heappush(avaible_chairs, min_chair)
                min_chair += 1
            chair_index = heapq.heappop(avaible_chairs)

            if friend_id == target_friend:
                return chair_index

            heapq.heappush(occupied_chiars, (end, chair_index))


print(Solution().smallestChair([[1, 4], [2, 3], [4, 6]], 1) == 1)
print(Solution().smallestChair([[3, 10], [1, 5], [2, 6]], 0) == 2)