class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number[][]} matrix
    * @return {number[]}
    */
   spiralOrder(matrix) {
      let left = 0;
      let top = 0;
      let right = matrix[0].length - 1;
      let bottom = matrix.length - 1;
      const spiral = [];

      while (true) {
         for (let index = left; index <= right; index++) {
            spiral.push(matrix[top][index]);
         }
         if (top === bottom) {
            break
         }
         top++;

         for (let index = top; index <= bottom; index++) {
            spiral.push(matrix[index][right]);
         }
         if (left === right) {
            break
         }
         right--;
         
         for (let index = right; index >= left; index--) {
            spiral.push(matrix[bottom][index]);
         }
         if (top === bottom) {
            break
         }
         bottom--;

         for (let index = bottom; index >= top; index--) {
            spiral.push(matrix[index][left]);
         }
         if (left === right) {
            break
         }
         left++;
      }
      return spiral
   };
}
const spiralOrder = new Solution().spiralOrder;


console.log(new Solution().spiralOrder([[4, 5, 6]]), [4, 5, 6])
console.log(new Solution().spiralOrder([[7], [9], [6]]), [7, 9, 6])
console.log(new Solution().spiralOrder([[4, 5], [6, 7]]), [4, 5, 7, 6])
console.log(new Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
console.log(new Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])