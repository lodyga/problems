import heapq


class Solution:
    def mostBooked(self, room_count: int, meetings: list[list[int]]) -> int:
        """
        Time complexity: O(mlogn)
            n: room count, m: meegins count
        Auxiliary space complexity: O(m)
        Tags: heap
        """
        meetings.sort()
        meeting_room = []
        # heap((meeting end time, room number, room use count), )
        heapq.heapify(meeting_room)
        avaible_room = [(room_number, 0) for room_number in range(room_count)]
        heapq.heapify(avaible_room)  # heap((room number, room use count))

        for start, end in meetings:
            while meeting_room and meeting_room[0][0] <= start:
                _, room_number, use_count = heapq.heappop(meeting_room)
                heapq.heappush(avaible_room, (room_number, use_count))

            if avaible_room:
                room_number, use_count = heapq.heappop(avaible_room)
                heapq.heappush(meeting_room, (end, room_number, use_count + 1))
            else:
                prev_end, room_number, use_count = heapq.heappop(meeting_room)
                meeting_end = (max(prev_end, start) + (end - start))
                heapq.heappush(
                    meeting_room,
                    (meeting_end, room_number, use_count + 1)
                )

        max_use_room_number = meeting_room[0][1]
        max_use_count = meeting_room[0][2]
        while meeting_room or avaible_room:
            if meeting_room:
                _, room_number, use_count = heapq.heappop(meeting_room)
            elif avaible_room:
                room_number, use_count = heapq.heappop(avaible_room)
            if use_count > max_use_count:
                max_use_count = use_count
                max_use_room_number = room_number
            elif use_count == max_use_count:
                max_use_room_number = min(max_use_room_number, room_number)

        return max_use_room_number


print(Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]), 0)
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]), 1)
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]), 1)
print(Solution().mostBooked(3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]), 1)
print(Solution().mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]), 0)
print(Solution().mostBooked(2, [[10, 11], [2, 10], [1, 17], [9, 13], [18, 20]]), 1)