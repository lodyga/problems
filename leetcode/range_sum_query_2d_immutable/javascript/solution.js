/**
 * Time complexity: 
 *     constructor: O(n2)
 *     sumRegion: O(1)
 * Auxiliary space complexity: O(n2)
 * Tags: prefix sum
 */
class NumMatrix {
   /**
    * @param {number[][]} matrix
    */
   constructor(matrix) {
      const rows = matrix.length;
      const cols = matrix[0].length;
      this.prefixMatrix = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));

      for (let row = 1; row <= rows; row++) {
         let prefix = 0;
         for (let col = 1; col <= cols; col++) {
            prefix += matrix[row - 1][col - 1];
            this.prefixMatrix[row][col] = (
               this.prefixMatrix[row - 1][col] +
               prefix
            );
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
         this.prefixMatrix[row2 + 1][col2 + 1]
         - this.prefixMatrix[row2 + 1][col1]
         - this.prefixMatrix[row1][col2 + 1]
         + this.prefixMatrix[row1][col1]
      )
   };
}


const numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
console.log(numMatrix.sumRegion(2, 1, 4, 3))  // return 8 (i.e sum of the red rectangle)
console.log(numMatrix.sumRegion(1, 1, 2, 2))  // return 11 (i.e sum of the green rectangle)
console.log(numMatrix.sumRegion(1, 2, 2, 4))  // return 12 (i.e sum of the blue rectangle)