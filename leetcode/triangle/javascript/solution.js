class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: array
    *     A: bottom-up, in-place
    * @param {number[][]} triangle
    * @return {number}
    */
   minimumTotal(triangle) {
      for (let row = triangle.length - 2; row >= 0; row--) {
         for (let col = 0; col <= row; col++) {
            triangle[row][col] += Math.min(
               triangle[row + 1][col],
               triangle[row + 1][col + 1]
            )
         }
      }
      return triangle[0][0]
   };
}


const minimumTotal = new Solution().minimumTotal;
console.log(new Solution().minimumTotal([[2]]) === 2)
console.log(new Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) === 11)
console.log(new Solution().minimumTotal([[-10]]) === -10)
