/**
 * Time complexity: 
 *     constructor: O(n2)
 *     sumRegion: O(1)
 * Auxiliary space complexity: O(n2)
 * Tags:
 *     DS: array (matrix)
 *     A: prefix sum
 */
class NumMatrix {
   /**
    * @param {number[][]} matrix
    */
   constructor(matrix) {
      const ROWS = matrix.length;
      const COLS = matrix[0].length;
      this.prefix = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(0));

      for (let row = 1; row <= ROWS; row++) {
         let rowPrefix = 0;
         for (let col = 1; col <= COLS; col++) {
            rowPrefix += matrix[row - 1][col - 1];
            this.prefix[row][col] = this.prefix[row - 1][col] + rowPrefix;
         }
      }
   };

   /** 
    * @param {number} row1 
    * @param {number} col1 
    * @param {number} row2 
    * @param {number} col2
    * @return {number}
    */
   sumRegion(row1, col1, row2, col2) {
      return (
         this.prefix[row2 + 1][col2 + 1]
         - this.prefix[row2 + 1][col1]
         - this.prefix[row1][col2 + 1]
         + this.prefix[row1][col1]
      )
   };
}


const numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
console.log(numMatrix.sumRegion(2, 1, 4, 3) === 8)
console.log(numMatrix.sumRegion(1, 1, 2, 2) === 11)
console.log(numMatrix.sumRegion(1, 2, 2, 4) === 12)
