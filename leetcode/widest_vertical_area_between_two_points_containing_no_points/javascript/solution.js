class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: sorting
    * @param {number[][]} points
    * @return {number}
    */
   maxWidthOfVerticalArea(points) {
      const xes = new Set();

      for (const [x, _] of points) {
         xes.add(x);
      }
      const sortedXes = [...xes].sort((a, b) => a - b);
      let maxX = 0;

      for (let index = 1; index < sortedXes.length; index++) 
         maxX = Math.max(maxX, sortedXes[index] - sortedXes[index - 1]);

      return maxX
   };
}


const maxWidthOfVerticalArea = new Solution().maxWidthOfVerticalArea;
console.log(new Solution().maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]) === 1)
console.log(new Solution().maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) === 3)