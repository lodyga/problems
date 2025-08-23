class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number[][]} matrix
    * @return {number[][]}
    */
   transpose(matrix) {
      const ROWS = matrix.length;
      const COLS = matrix[0].length;
      const transposed = Array.from({ length: COLS }, () => Array(ROWS).fill(0));

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            transposed[col][row] = matrix[row][col];
         }
      }
      return transposed
   };
}
const transpose = new Solution().transpose;


console.log(new Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
console.log(new Solution().transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])