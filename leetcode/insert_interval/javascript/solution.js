class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: intervals, greedy
    * @param {number[][]} intervals
    * @param {number[]} newInterval
    * @return {number[][]}
    */
   insert(intervals, newInterval) {
      const N = intervals.length;
      let [newStart, newEnd] = newInterval;
      const res = [];

      for (let idx = 0; idx < N; idx++) {
         const [start, end] = intervals[idx];
    
         // New interval is earlier than current interval without overlap.
         if (newEnd < start) {
            res.push([newStart, newEnd]);
            res.push(...intervals.slice(idx,));
            return res;
         }
         // New interval is later than current interval without overlap.
         else if (newStart > end) {
            res.push([start, end]);
         }
         // New interval overlap current interterval.
         else {
            newStart = Math.min(start, newStart);
            newEnd = Math.max(end, newEnd);
         }
      }

      res.push([newStart, newEnd]);
      return res;
   }
}


const insert = new Solution().insert;
console.log(new Solution().insert([[1, 3], [6, 9]], [2, 5]).toString() === [[1, 5], [6, 9]].toString())
console.log(new Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]).toString() === [[1, 2], [3, 10], [12, 16]].toString())
console.log(new Solution().insert([], [5, 7]).toString() === [[5, 7]].toString())
console.log(new Solution().insert([[1, 5]], [2, 3]).toString() === [[1, 5]].toString())
console.log(new Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1]).toString() === [[0, 1], [2, 5], [6, 7], [8, 9]].toString())
console.log(new Solution().insert([[1, 5]], [6, 8]).toString() === [[1, 5], [6, 8]].toString())
