class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[][]} matrix
    * @return {number}
    */
   maxMatrixSum(matrix) {
      let isPositive = true;
      let minVal = Math.abs(matrix[0][0]);
      let total = 0;

      for (let row = 0; row < matrix.length; row++)
         for (let col = 0; col < matrix[0].length; col++) {
            total += Math.abs(matrix[row][col]);

            if (matrix[row][col] < 0) {
               isPositive = !isPositive;
            }

            if (Math.abs(matrix[row][col]) < minVal) {
               minVal = Math.abs(matrix[row][col]);
            }
         }

      return isPositive ? total : total - minVal * 2
   };
}


const maxMatrixSum = new Solution().maxMatrixSum;
console.log(new Solution().maxMatrixSum([[1, -1], [-1, 1]]) === 4)
console.log(new Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) === 16)
