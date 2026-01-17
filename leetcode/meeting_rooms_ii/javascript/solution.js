import { MinPriorityQueue } from '@datastructures-js/priority-queue';


/**
 * Definition of Interval:
*/
class Interval {
   constructor(start, end) {
      this.start = start;
      this.end = end;
   }
}


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: intervals, heap
    * @param {Interval[]} intervals
    * @return {number}
    */
   minMeetingRooms(intervals) {
      intervals.sort((a, b) => a.start - b.start);
      const roomHeap = new MinPriorityQueue();
      let roomCounter = 0;

      for (const interval of intervals) {
         const start = interval.start;
         const end = interval.end;
         if (roomHeap.front() <= start) {
            roomHeap.pop();
         }
         roomHeap.push(end);
         roomCounter = Math.max(roomCounter, roomHeap.size())
      }
      return roomCounter
   };
}


const minMeetingRooms = new Solution().minMeetingRooms;
console.log(new Solution().minMeetingRooms([new Interval(0, 30), new Interval(5, 10), new Interval(15, 20)]) === 2)
console.log(new Solution().minMeetingRooms([new Interval(5, 10), new Interval(15, 20)]) === 1)
console.log(new Solution().minMeetingRooms([new Interval(0, 10), new Interval(5, 10), new Interval(5, 10), new Interval(15, 25), new Interval(20, 25)]) === 3)
