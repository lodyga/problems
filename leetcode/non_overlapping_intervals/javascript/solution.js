class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: intervals, greedy, sorting
    * @param {number[][]} intervals
    * @return {number}
    */
   eraseOverlapIntervals(intervals) {
      const N = intervals.length;
      intervals.sort((a, b) => a[0] - b[0]);
      let end = intervals[0][1];
      let res = 0;

      for (let idx = 1; idx < N; idx++) {
         const [nextStart, nextEnd] = intervals[idx];

         if (end > nextStart) {
            end = Math.min(end, nextEnd);
            res++;
         }
         else {
            end = nextEnd;
         }
      }

      return res;
   }
}


const eraseOverlapIntervals = new Solution().eraseOverlapIntervals;
console.log(new Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) === 1)
console.log(new Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) === 2)
console.log(new Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) === 0)
console.log(new Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) === 2)
console.log(new Solution().eraseOverlapIntervals([[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2], [30, 47], [-40, -26]]) === 7)
