class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: sorting
    * @param {number[][]} points
    * @return {number}
    */
   findMinArrowShots(points) {
      // points.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      points.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
      let arrowCounter = 0;

      let index = 0;
      while (index < points.length) {
         let earliestEnd = points[index][1];
         arrowCounter++;
         index++;
         while (
            index < points.length &&
            points[index][0] <= earliestEnd
         ) {
            const end = points[index][1];
            earliestEnd = Math.min(earliestEnd, end);
            index++;
         }
      }
      return arrowCounter
   };
}


const findMinArrowShots = new Solution().findMinArrowShots;
console.log(new Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) === 2)
console.log(new Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) === 4)
console.log(new Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) === 2)
console.log(new Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]) === 2)
console.log(new Solution().findMinArrowShots([[-2147483648, 2147483647]]) === 1)