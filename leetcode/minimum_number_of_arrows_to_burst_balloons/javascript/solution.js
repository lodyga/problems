class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: greedy, sorting
    * @param {number[][]} points
    * @return {number}
    */
   findMinArrowShots(points) {
      points.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
      let res = 1;
      let prevEnd = points[0][1];

      for (const [start, end] of points) {
         if (start <= prevEnd) {
            prevEnd = Math.min(end, prevEnd);
            continue
         }

         res++;
         prevEnd = end;
      }
      return res
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: greedy, sorting
    * @param {number[][]} points
    * @return {number}
    */
   findMinArrowShots(points) {
      points.sort((a, b) => a[1] - b[1]);
      let res = 1;
      let prevEnd = points[0][1];

      for (const [start, end] of points) {
         if (start <= prevEnd) {
            continue
         }

         res++;
         prevEnd = end;
      }
      return res
   };
}


const findMinArrowShots = new Solution().findMinArrowShots;
console.log(new Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) === 2)
console.log(new Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) === 4)
console.log(new Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) === 2)
console.log(new Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]) === 2)
console.log(new Solution().findMinArrowShots([[-2147483648, 2147483647]]) === 1)
