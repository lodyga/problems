class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number} n
    * @return {number[][]}
    */
   generateMatrix(n) {
      let left = 0;
      let top = 0;
      let right = n - 1;
      let bottom = n - 1;
      const matrix = Array.from({ length: n }, () => Array(n).fill(0));
      let number = 0;

      while (left < right) {
         // top
         for (let l = left; l < right; l++) {
            number++;
            matrix[top][l] = number;
         }
         // right
         for (let t = top; t < bottom; t++) {
            number++;
            matrix[t][right] = number;
         }
         // bottom
         for (let r = right; r > left; r--) {
            number++;
            matrix[bottom][r] = number;
         }
         // left
         for (let b = bottom; b > top; b--) {
            number++;
            matrix[b][left] = number
         }

         left++;
         top++;
         right--;
         bottom--;
      }
      if (left === right) {
         number++;
         matrix[left][right] = number
      }

      return matrix
   };
}


const generateMatrix = new Solution().generateMatrix;
console.log(new Solution().generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
console.log(new Solution().generateMatrix(4), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
console.log(new Solution().generateMatrix(1), [[1]])