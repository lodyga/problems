import { PriorityQueue, PriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(mlogn + mlogm)
    *     n: room count
    *     m: meetins count
    * Auxiliary space complexity: O(n + m)
    * Tags: heap
    * @param {number} roomCount
    * @param {number[][]} meetings
    * @return {number}
    */
   mostBooked(roomCount, meetings) {
      meetings.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      // [(avaibility date, room number, room used)]
      const meeting_rooms = new PriorityQueue((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]);

      // [(room number, room used)]
      const avaible_rooms = new PriorityQueue((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]);
      for (let roomNumber = 0; roomNumber < roomCount; roomNumber++) {
         avaible_rooms.enqueue([roomNumber, 0]);
      }
      const roomUse = Array(roomCount).fill(0);
      let maxRoomUse = 0;

      for (const [start, end] of meetings) {
         while (!meeting_rooms.isEmpty() && start >= meeting_rooms.front()[0]) {
            const [_, roomNumber, useCount] = meeting_rooms.dequeue();
            avaible_rooms.enqueue([roomNumber, useCount]);
         }
         let rN;
         if (avaible_rooms.size() !== 0) {
            const [roomNumber, useCount] = avaible_rooms.dequeue();
            meeting_rooms.enqueue([end, roomNumber, useCount + 1]);
            rN = roomNumber;
         } else {
            let [avaible, roomNumber, useCount] = meeting_rooms.dequeue();
            avaible = Math.max(avaible, start) + (end - start);
            meeting_rooms.enqueue([avaible, roomNumber, useCount + 1]);
            rN = roomNumber;
         }
         roomUse[rN] += 1;
         maxRoomUse = Math.max(maxRoomUse, roomUse[rN]);
      }
      for (let roomNumber = 0; roomNumber < roomCount; roomNumber++)
         if (roomUse[roomNumber] === maxRoomUse)
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