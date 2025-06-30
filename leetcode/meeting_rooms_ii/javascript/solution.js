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
    * Tags: intervals, heap
    * @param {Interval[]} intervals
    * @return {number}
    */
   minMeetingRooms(intervals) {
      intervals.sort((a, b) => a.start - b.start);
      const roomHeap = new MinPriorityQueue();

      for (const interval of intervals) {
         if (roomHeap.size() && roomHeap.front() <= interval.start) {
            roomHeap.pop();
         }
         roomHeap.push(interval.end);
      }
      return roomHeap.size()
   };
}


console.log(new Solution().minMeetingRooms([new Interval(0, 30), new Interval(5, 10), new Interval(15, 20)]) === 2)
console.log(new Solution().minMeetingRooms([new Interval(5, 10), new Interval(15, 20)]) === 1)