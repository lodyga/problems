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
    * Tags: sorting
    * @param {Interval[]} intervals
    * @returns {boolean}
    */
   canAttendMeetings(intervals) {
      intervals.sort((a, b) => a.start - b.start);

      for (let index = 1; index < intervals.length; index++) {
         const prevEnd = intervals[index - 1].end;
         const currentStart = intervals[index].start;

         if (prevEnd > currentStart) {
            return false
         }
      }
      return true
   }
}


console.log(new Solution().canAttendMeetings([new Interval(5, 10), new Interval(15, 20)]) === true)
console.log(new Solution().canAttendMeetings([new Interval(0, 30), new Interval(5, 10), new Interval(15, 20)]) === false)