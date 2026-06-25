class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: intervals, sorting
    * @param {Interval[]} intervals
    * @returns {boolean}
    */
   canAttendMeetings(intervals) {
      intervals.sort((a, b) => a - b);

      for (let idx = 0; idx < intervals.length - 1; idx++) {
         const meetingEnd = intervals[idx][1];
         const nextMeetingStart = intervals[idx + 1][0];

         if (meetingEnd > nextMeetingStart) {
            return false;
         }
      }

      return true;
   }
}


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
    *     A: intervals, sorting
    * @param {Interval[]} intervals
    * @returns {boolean}
    */
   canAttendMeetings(intervals) {
      intervals.sort((a, b) => a.start - b.start);

      for (let idx = 1; idx < intervals.length; idx++) {
         const prevEnd = intervals[idx - 1].end;
         const currentStart = intervals[idx].start;

         if (prevEnd > currentStart) {
            return false;
         }
      }

      return true;
   }
}


console.log(new Solution().canAttendMeetings([new Interval(5, 10), new Interval(15, 20)]) === true)
console.log(new Solution().canAttendMeetings([new Interval(0, 30), new Interval(5, 10), new Interval(15, 20)]) === false)
