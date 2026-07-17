class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number[][]} matrix
    * @return {number[]}
    */
   spiralOrder(matrix) {
      let left = 0;
      let top = 0;
      let right = matrix[0].length - 1;
      let bottom = matrix.length - 1;
      const res = [];

      while (true) {
         for (let idx = left; idx <= right; idx++) {
            res.push(matrix[top][idx]);
         }
         top++;
         if (top > bottom) {
            break;
         }

         for (let idx = top; idx <= bottom; idx++) {
            res.push(matrix[idx][right]);
         }
         right--;
         if (left > right) {
            break;
         }
         
         for (let idx = right; idx >= left; idx--) {
            res.push(matrix[bottom][idx]);
         }
         bottom--;
         if (top > bottom) {
            break;
         }

         for (let idx = bottom; idx >= top; idx--) {
            res.push(matrix[idx][left]);
         }
         left++;
         if (left > right) {
            break;
         }
      }

      return res;
   }
}


const spiralOrder = new Solution().spiralOrder;
console.log(new Solution().spiralOrder([[4, 5, 6]]).toString() === [4, 5, 6].toString())
console.log(new Solution().spiralOrder([[7], [9], [6]]).toString() === [7, 9, 6].toString())
console.log(new Solution().spiralOrder([[4, 5], [6, 7]]).toString() === [4, 5, 7, 6].toString())
console.log(new Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).toString() === [1, 2, 3, 6, 9, 8, 7, 4, 5].toString())
console.log(new Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]).toString() === [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7].toString())
console.log(new Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]).toString() === [1, 2, 3, 4, 8, 12, 16, 20, 24, 23, 22, 21, 17, 13, 9, 5, 6, 7, 11, 15, 19, 18, 14, 10].toString())
