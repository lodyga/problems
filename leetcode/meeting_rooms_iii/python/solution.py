import heapq


class Solution:
    def mostBooked(self, room_count: int, meetings: list[list[int]]) -> int:
        """
        Time complexity: O(mlogn)
            n: room count
            m: meeting count
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: iteration
        """
        meetings.sort()
        # heap((avaibility date, room number, room use counter))
        occupied_rooms = [(0, room) for room in range(room_count)]
        # heap((room number, room use counter))
        avaible_rooms = []
        room_use_counter = [0] * room_count

        for start, end in meetings:
            meeting_duration = end - start

            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room_num = heapq.heappop(occupied_rooms)
                heapq.heappush(avaible_rooms, (room_num))

            if avaible_rooms:
                room_num = heapq.heappop(avaible_rooms)
            else:
                avaible, room_num = heapq.heappop(occupied_rooms)
                # Avabile from room overrides start from meeting.
                start = avaible
            
            meeing_end = start + meeting_duration
            heapq.heappush(occupied_rooms, (meeing_end, room_num))
            room_use_counter[room_num] += 1

        max_use_counter = max(room_use_counter)
        for room_num, use_counter in enumerate(room_use_counter):
            if use_counter == max_use_counter:
                return room_num
        

print(Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0)
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1)
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1)
print(Solution().mostBooked(3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]) == 1)
print(Solution().mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]) == 0)
print(Solution().mostBooked(2, [[10, 11], [2, 10], [1, 17], [9, 13], [18, 20]]) == 1)
