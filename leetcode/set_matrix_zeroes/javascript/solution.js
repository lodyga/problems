class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: 
    * @param {number[][]} matrix
    * @return {}
    */
   setZeroes(matrix) {
      const rows = matrix.length;
      const cols = matrix[0].length;
      let zeroFirstRow = false;

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            if (matrix[row][col] === 0) {
               matrix[0][col] = 0;
               if (row === 0) {
                  zeroFirstRow = true
               } else {
                  matrix[row][0] = 0;
               }
            }
         }
      }

      for (let row = 1; row < rows; row++) {
         for (let col = 1; col < cols; col++) {
            if (
               matrix[0][col] === 0 ||
               matrix[row][0] === 0
            ) {
               matrix[row][col] = 0;
            }
         }
      }

      if (matrix[0][0] === 0) {
         for (let row = 1; row < rows; row++) {
            matrix[row][0] = 0;
         }
      }

      if (zeroFirstRow) {
         for (let col = 0; col < cols; col++) {
            matrix[0][col] = 0;
         }
      }

      return matrix
   };
}
const setZeroes = new Solution().setZeroes;


console.log(new Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
console.log(new Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]), [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
console.log(new Solution().setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]), [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])