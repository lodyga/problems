class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: intervals, greedy, sorting
    * @param {number[][]} intervals
    * @return {number[][]}
    */
   merge(intervals) {
      intervals.sort((a, b) => a[0] - b[0]);
      const res = [intervals[0]];

      for (let idx = 1; idx < intervals.length; idx++) {
         const end = res[res.length - 1][1];
         const [nextStart, nextEnd] = intervals[idx];

         if (end < nextStart) {
            res.push([nextStart, nextEnd]);
         }
         else {
            res[res.length - 1][1] = Math.max(end, nextEnd);
         }
      }

      return res;
   }
}


const merge = new Solution().merge;
console.log(new Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]).toString() === [[1, 6], [8, 10], [15, 18]].toString())
console.log(new Solution().merge([[1, 4], [4, 5]]).toString() === [[1, 5]].toString())
console.log(new Solution().merge([[1, 4], [0, 0]]).toString() === [[0, 0], [1, 4]].toString())
console.log(new Solution().merge([[1, 4], [2, 3]]).toString() === [[1, 4]].toString())
