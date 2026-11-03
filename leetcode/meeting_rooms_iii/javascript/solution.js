import { PriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(mlogn)
    *     n: room count
    *     m: meeting count
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap
    *     A: iteration
    * @param {number} roomCount
    * @param {number[][]} meetings
    * @return {number}
    */
   mostBooked(roomCount, meetings) {
      meetings.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      // PriorityQueue([avaibility date, room number], )
      const bookedRooms = new PriorityQueue((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]);

      for (let room = 0; room < roomCount; room++) {
         bookedRooms.push([0, room]);
      }

      // PriorityQueue([room number], )
      const avaibleRooms = new PriorityQueue((a, b) => a - b);
      const roomUseCounter = Array(roomCount).fill(0);

      for (let [start, end] of meetings) {
         const meetingDuration = end - start;

         while (!bookedRooms.isEmpty() && bookedRooms.front()[0] <= start) {
            const [, roomNum] = bookedRooms.pop();
            avaibleRooms.push(roomNum);
         }

         let roomNum;

         if (!avaibleRooms.isEmpty()) {
            roomNum = avaibleRooms.pop();
         }
         else {
            const [prevStart, prevRoom] = bookedRooms.pop();
            roomNum = prevRoom;
            // Avabile from room overrides start from meeting.
            start = prevStart;
         }

         const meeingEnd = start + meetingDuration;
         bookedRooms.push([meeingEnd, roomNum]);
         roomUseCounter[roomNum] += 1;
      }

      const maxUseCounter = Math.max(...roomUseCounter);

      for (let roomNum = 0; roomNum < roomCount; roomNum++)
         if (roomUseCounter[roomNum] === maxUseCounter) {
            return roomNum;
         }
   }
}


const mostBooked = new Solution().mostBooked;
console.log(new Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) === 0)
console.log(new Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) === 1)
console.log(new Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) === 1)
console.log(new Solution().mostBooked(3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]) === 1)
console.log(new Solution().mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]) === 0)
console.log(new Solution().mostBooked(2, [[10, 11], [2, 10], [1, 17], [9, 13], [18, 20]]) === 1)
