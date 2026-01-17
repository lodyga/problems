class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: intervals, greedy
    * @param {number[][]} intervals
    * @param {number[]} newInterval
    * @return {number[][]}
    */
   insert(intervals, newInterval) {
      let [newStart, newEnd] = newInterval;
      const newIntervals = [];

      for (const [start, end] of intervals) {
         // New interval already added
         // or new interval is after current interval.
         if (
            newInterval === null ||
            end < newStart
         )
            newIntervals.push([start, end]);

         // New interval is before current interval.
         else if (newEnd < start) {
            newIntervals.push(newInterval);
            newIntervals.push([start, end]);
            newInterval = null;
         }

         // New and current intervals overlaps.
         else {
            newInterval = [Math.min(start, newStart), Math.max(end, newEnd)];
            [newStart, newEnd] = newInterval;
         }
      }

      if (newInterval)
         newIntervals.push(newInterval);

      return newIntervals
   };
}


const insert = new Solution().insert;
console.log(new Solution().insert([[1, 3], [6, 9]], [2, 5]).toString() === [[1, 5], [6, 9]].toString())
console.log(new Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]).toString() === [[1, 2], [3, 10], [12, 16]].toString())
console.log(new Solution().insert([], [5, 7]).toString() === [[5, 7]].toString())
console.log(new Solution().insert([[1, 5]], [2, 3]).toString() === [[1, 5]].toString())
console.log(new Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1]).toString() === [[0, 1], [2, 5], [6, 7], [8, 9]].toString())
console.log(new Solution().insert([[1, 5]], [6, 8]).toString() === [[1, 5], [6, 8]].toString())
