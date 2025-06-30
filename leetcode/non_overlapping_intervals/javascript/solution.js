class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number[][]} intervals
    * @return {number}
    */
   eraseOverlapIntervals(intervals) {
      intervals.sort((a, b) => a[0] - b[0]);
      let cleanCounter = 0;
      let prevEnd = intervals[0][1];

      for (let index = 1; index < intervals.length; index++) {
         const start = intervals[index][0];
         const end = intervals[index][1];

         if (prevEnd > start) {
            prevEnd = Math.min(prevEnd, end)
            cleanCounter++;
         } else {
            prevEnd = end;
         }
      }
      return cleanCounter
   };
}
const eraseOverlapIntervals = new Solution().eraseOverlapIntervals;


console.log(new Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) === 1)
console.log(new Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) === 2)
console.log(new Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) === 0)
console.log(new Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) === 2)
console.log(new Solution().eraseOverlapIntervals([[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2], [30, 47], [-40, -26]]) === 7)