class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: intervals, sorting
    * @param {number[][]} intervals
    * @return {number[][]}
    */
   merge(intervals) {
      intervals.sort((a, b) => a[0] - b[0]);
      const mergedIntervals = [intervals[0]];

      for (let index = 1; index < intervals.length; index++) {
         const start = intervals[index][0];
         const end = intervals[index][1];
         const prevEnd = mergedIntervals[mergedIntervals.length - 1][1];

         if (prevEnd >= start) {
            mergedIntervals[mergedIntervals.length - 1][1] = Math.max(prevEnd, end);
         } else {
            mergedIntervals.push([start, end]);
         }

      }
      return mergedIntervals
   };
}
const merge = new Solution().merge;


console.log(new Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
console.log(new Solution().merge([[1, 4], [4, 5]]), [[1, 5]])
console.log(new Solution().merge([[1, 4], [0, 0]]), [[0, 0], [1, 4]])
console.log(new Solution().merge([[1, 4], [2, 3]]), [[1, 4]])