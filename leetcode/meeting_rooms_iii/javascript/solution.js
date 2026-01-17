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
      const occupiedRooms = new PriorityQueue((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]);
      for (let room = 0; room < roomCount; room++) {
         occupiedRooms.enqueue([0, room]);
      }
      // PriorityQueue([room number], )
      const avaibleRooms = new PriorityQueue((a, b) => a - b);
      const roomUseCounter = Array(roomCount).fill(0);

      for (let [start, end] of meetings) {
         const meetingDuration = end - start;

         while (occupiedRooms.size() && occupiedRooms.front()[0] <= start) {
            const [_, roomNumber] = occupiedRooms.dequeue();
            avaibleRooms.enqueue(roomNumber);
         }

         let roomNumber = roomCount;
         if (avaibleRooms.size()) {
            roomNumber = avaibleRooms.dequeue();
         } else {
            const [avaible, rN] = occupiedRooms.dequeue();
            roomNumber = rN;
            // Avabile from room overrides start from meeting.
            start = avaible;
         }
         const meeingEnd = start + meetingDuration;
         occupiedRooms.enqueue([meeingEnd, roomNumber]);
         roomUseCounter[roomNumber] += 1;
      }
      const maxUseCounter = Math.max(...roomUseCounter);
      for (let roomNumber = 0; roomNumber < roomCount; roomNumber++)
         if (roomUseCounter[roomNumber] === maxUseCounter)
            return roomNumber
   };
}


const mostBooked = new Solution().mostBooked;
console.log(new Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) === 0)
console.log(new Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) === 1)
console.log(new Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) === 1)
console.log(new Solution().mostBooked(3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]) === 1)
console.log(new Solution().mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]) === 0)
console.log(new Solution().mostBooked(2, [[10, 11], [2, 10], [1, 17], [9, 13], [18, 20]]) === 1)
