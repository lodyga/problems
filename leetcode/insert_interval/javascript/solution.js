class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: intervals, greedy
    * @param {number[][]} intervals
    * @param {number[]} newInterval
    * @return {number[][]}
    */
   insert(intervals, newInterval) {
      const mergedInervals = [];

      for (let index = 0; index < intervals.length; index++) {
         const start = intervals[index][0];
         const end = intervals[index][1];
         const newStart = newInterval[0];
         const newEnd = newInterval[1];

         if (newEnd < start) {
            mergedInervals.push(newInterval);
            mergedInervals.push(...intervals.slice(index,));
            return mergedInervals  // early exit
         } else if (newStart > end) {
            mergedInervals.push([start, end]);
         } else {
            newInterval = [
               Math.min(start, newStart),
               Math.max(end, newEnd)
            ];
         }
      }
      mergedInervals.push(newInterval);
      return mergedInervals
   };
}
const insert = new Solution().insert;


console.log(new Solution().insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
console.log(new Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]])
console.log(new Solution().insert([], [5, 7]), [[5, 7]])
console.log(new Solution().insert([[1, 5]], [2, 3]), [[1, 5]])
console.log(new Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1]), [[0, 1], [2, 5], [6, 7], [8, 9]])