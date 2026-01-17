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
      const merged = [intervals[0]];

      for (let index = 1; index < intervals.length; index++) {
         const start = intervals[index][0];
         const end = intervals[index][1];
         const prevEnd = merged[merged.length - 1][1];

         if (prevEnd >= start) {
            merged[merged.length - 1][1] = Math.max(prevEnd, end);
         } else {
            merged.push([start, end]);
         }
      }
      return merged
   };
}


const merge = new Solution().merge;
console.log(new Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]).toString() === [[1, 6], [8, 10], [15, 18]].toString())
console.log(new Solution().merge([[1, 4], [4, 5]]).toString() === [[1, 5]].toString())
console.log(new Solution().merge([[1, 4], [0, 0]]).toString() === [[0, 0], [1, 4]].toString())
console.log(new Solution().merge([[1, 4], [2, 3]]).toString() === [[1, 4]].toString())
