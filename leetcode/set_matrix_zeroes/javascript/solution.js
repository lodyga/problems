class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number[][]} matrix
    * @return {}
    */
   setZeroes(matrix) {
      const ROWS = matrix.length;
      const COLS = matrix[0].length;

      const zeroRows = Array(ROWS).fill(false);
      const zeroCols = Array(COLS).fill(false);

      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            if (matrix[row][col] === 0) {
               zeroRows[row] = true;
               zeroCols[col] = true;
            }

      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            if (zeroRows[row] || zeroCols[col])
               matrix[row][col] = 0;

      return matrix
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number[][]} matrix
    * @return {}
    */
   setZeroes(matrix) {
      const ROWS = matrix.length;
      const COLS = matrix[0].length;
      let firstRowIsZero = false;
      let firstColIsZero = false;

      for (let row = 0; row < ROWS; row++)
         if (matrix[row][0] === 0) {
            firstColIsZero = true;
            break
         }

      for (let col = 0; col < COLS; col++)
         if (matrix[0][col] === 0) {
            firstRowIsZero = true;
            break
         }

      for (let row = 1; row < ROWS; row++) {
         for (let col = 1; col < COLS; col++) {
            if (matrix[row][col] === 0) {
               matrix[row][0] = 0;
               matrix[0][col] = 0;
            }
         }
      }

      for (let row = 1; row < ROWS; row++) {
         for (let col = 1; col < COLS; col++) {
            if (
               matrix[row][0] === 0 ||
               matrix[0][col] === 0
            ) {
               matrix[row][col] = 0;
            }
         }
      }

      if (firstColIsZero) {
         for (let row = 0; row < ROWS; row++) {
            matrix[row][0] = 0;
         }
      }

      if (firstRowIsZero) {
         for (let col = 0; col < COLS; col++) {
            matrix[0][col] = 0;
         }
      }

      return matrix
   };
}


const setZeroes = new Solution().setZeroes;
console.log(new Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]).toString() === [[1, 0, 1], [0, 0, 0], [1, 0, 1]].toString())
console.log(new Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]).toString() === [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]].toString())
console.log(new Solution().setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]).toString() === [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]].toString())
