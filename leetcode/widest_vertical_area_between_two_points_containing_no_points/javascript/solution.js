class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: sorting
    * @param {number[][]} points
    * @return {number}
    */
   maxWidthOfVerticalArea(points) {
      const xPoints = points.map(([x, ]) => x).sort((a, b) => a - b);
      let res = 0;

      for (let index = 1; index < xPoints.length; index++) {
         const x1 = xPoints[index - 1];
         const x2 = xPoints[index];
         res = Math.max(res, x2 - x1);
      }

      return res
   };
   
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set, array
    *     A: sorting
    * @param {number[][]} points
    * @return {number}
    */
   maxWidthOfVerticalArea(points) {
      const xPoints = new Set();

      for (const [x,] of points) {
         xPoints.add(x);
      }
      
      const xPointsSort = [...xPoints].sort((a, b) => a - b);
      let res = 0;

      for (let index = 1; index < xPointsSort.length; index++) {
         const x1 = xPointsSort[index - 1];
         const x2 = xPointsSort[index];
         res = Math.max(res, x2 - x1);
      }

      return res
   };
}


const maxWidthOfVerticalArea = new Solution().maxWidthOfVerticalArea;
console.log(new Solution().maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]) === 1)
console.log(new Solution().maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) === 3)
