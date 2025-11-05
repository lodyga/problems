class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[][]} matrix
    * @return {number}
    */
   maxMatrixSum(matrix) {
      let negativeMark = false;
      let minElement = Math.abs(matrix[0][0]);
      let total = 0;

      for (let row = 0; row < matrix.length; row++)
         for (let col = 0; col < matrix[0].length; col++) {
            total += Math.abs(matrix[row][col]);
            minElement = Math.min(minElement, Math.abs(matrix[row][col]));
            if (matrix[row][col] < 0)
               negativeMark = negativeMark ? false : true;
         }

      total -= negativeMark ? minElement * 2 : 0;
      return total
   };
}


const maxMatrixSum = new Solution().maxMatrixSum;
console.log(new Solution().maxMatrixSum([[1, -1], [-1, 1]]) === 4)
console.log(new Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) === 16)
