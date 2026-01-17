class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    DS: array (matrix)
    *    A: iteration
    * @param {number[][]} matrix
    * @return {void} Do not return anything, modify matrix in-place instead.
    */
   rotate(matrix) {
      let left = 0;
      let top = 0;
      let right = matrix.length - 1;
      let bottom = matrix.length - 1;

      while (left < right) {
         for (let index = 0; index < right - left; index++) {
            const topLeft = matrix[top][left + index];
            matrix[top][left + index] = matrix[bottom - index][left];
            matrix[bottom - index][left] = matrix[bottom][right - index];
            matrix[bottom][right - index] = matrix[top + index][right];
            matrix[top + index][right] = topLeft;
         }
         left++;
         top++
         right--;
         bottom--;
      }
      return matrix
   };
}


const rotate = new Solution().rotate;
console.log(new Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).toString() === [[7, 4, 1], [8, 5, 2], [9, 6, 3]].toString())
console.log(new Solution().rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]).toString() === [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]].toString())
console.log(new Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]).toString() === [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]].toString())
console.log(new Solution().rotate([[2, 29, 20, 26, 16, 28], [12, 27, 9, 25, 13, 21], [32, 33, 32, 2, 28, 14], [13, 14, 32, 27, 22, 26], [33, 1, 20, 7, 21, 7], [4, 24, 1, 6, 32, 34]]).toString() === [[4, 33, 13, 32, 12, 2], [24, 1, 14, 33, 27, 29], [1, 20, 32, 32, 9, 20], [6, 7, 27, 2, 25, 26], [32, 21, 22, 28, 13, 16], [34, 7, 26, 14, 21, 28]].toString())
