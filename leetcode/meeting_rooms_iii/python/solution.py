import heapq


class Solution:
    def mostBooked(self, room_count: int, meetings: list[list[int]]) -> int:
        """
        Time complexity: O(mlogn)
            n: room count
            m: meegins count
        Auxiliary space complexity: O(m)
        Tags: heap
        """
        meetings.sort()
        meeting_rooms = []  # [(avaibility date, room number, room used)]
        avaible_rooms = [(room_number, 0) for room_number in range(room_count)]  # [(room number, room used)]
        heapq.heapify(avaible_rooms)
        room_use = [0] * room_count
        max_room_use = 0
        
        for start, end in meetings:
            while meeting_rooms and start >= meeting_rooms[0][0]:
                _, room_number, use_count = heapq.heappop(meeting_rooms)
                heapq.heappush(avaible_rooms, (room_number, use_count))
            
            if avaible_rooms:
                room_number, use_count = heapq.heappop(avaible_rooms)
                heapq.heappush(meeting_rooms, (end, room_number, use_count + 1))
            else:
                avaible, room_number, use_count = heapq.heappop(meeting_rooms)
                avaible = max(avaible, start) + (end - start)  # when to start + meeting duration
                heapq.heappush(meeting_rooms, (avaible, room_number, use_count + 1))
            
            room_use[room_number] += 1
            max_room_use = max(max_room_use, room_use[room_number])

        for room_number in range(room_count):
            if room_use[room_number] == max_room_use:
                return room_number


class Solution:
    def mostBooked(self, room_count: int, meetings: list[list[int]]) -> int:
        """
        Time complexity: O(mlogn + mlogm)
            n: room count
            m: meetins count
        Auxiliary space complexity: O(n + m)
        Tags: heap
        """
        meetings.sort()
        meeting_rooms = []  # [(avaibility date, room number, room used)]
        avaible_rooms = [(room_number, 0) for room_number in range(room_count)]  # [(room number, room used)]
        heapq.heapify(avaible_rooms)
        
        for start, end in meetings:
            while meeting_rooms and start >= meeting_rooms[0][0]:
                _, room_number, use_count = heapq.heappop(meeting_rooms)
                heapq.heappush(avaible_rooms, (room_number, use_count))
            
            if avaible_rooms:
                room_number, use_count = heapq.heappop(avaible_rooms)
                heapq.heappush(meeting_rooms, (end, room_number, use_count + 1))
            else:
                avaible, room_number, use_count = heapq.heappop(meeting_rooms)
                avaible = max(avaible, start) + (end - start)  # when to start + meeting duration
                heapq.heappush(meeting_rooms, (avaible, room_number, use_count + 1))

        most_booked_room = []  # [(-room used, room numebr)]
        while meeting_rooms or avaible_rooms:
            if meeting_rooms:
                _, room_number, use_count = heapq.heappop(meeting_rooms)
            else:
                room_number, use_count = heapq.heappop(avaible_rooms)
            heapq.heappush(most_booked_room , (-use_count, room_number))

        return most_booked_room[0][1]


print(Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0)
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1)
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1)
print(Solution().mostBooked(3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]) == 1)
print(Solution().mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]) == 0)
print(Solution().mostBooked(2, [[10, 11], [2, 10], [1, 17], [9, 13], [18, 20]]) == 1)