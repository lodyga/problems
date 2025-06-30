class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number[][]} matrix
    * @return {void} Do not return anything, modify matrix in-place instead.
    */
   rotate(matrix) {
      let left = 0;
      let right = matrix.length - 1;

      while (left < right) {
         const top = left;
         const bottom = right;

         for (let index = 0; index < right - left; index++) {
            const topLeft = matrix[top][left + index];
            matrix[top][left + index] = matrix[bottom - index][left];
            matrix[bottom - index][left] = matrix[bottom][right - index];
            matrix[bottom][right - index] = matrix[top + index][right];
            matrix[top + index][right] = topLeft;
         }
         left++;
         right--;
      }
      return matrix
   };
}
const rotate = new Solution().rotate;


console.log(new Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
console.log(new Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]), [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])