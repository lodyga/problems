class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {number} n
    * @return {number[][]}
    */
   generateMatrix(n) {
      let left = 0;
      let top = 0;
      let right = n - 1;
      let bottom = n - 1;
      const res = Array.from({ length: n }, () => Array(n).fill(0));
      let num = 1;

      while (left < right) {
         // top
         for (let l = left; l < right; l++) {
            res[top][l] = num;
            num++;
         }
         // right
         for (let t = top; t < bottom; t++) {
            res[t][right] = num;
            num++;
         }
         // bottom
         for (let r = right; r > left; r--) {
            res[bottom][r] = num;
            num++;
         }
         // left
         for (let b = bottom; b > top; b--) {
            res[b][left] = num
            num++;
         }

         left++;
         top++;
         right--;
         bottom--;
      }
      if (left === right) {
         res[top][left] = num
      }

      return res
   };
}


const generateMatrix = new Solution().generateMatrix;
console.log(new Solution().generateMatrix(3).toString() === [[1, 2, 3], [8, 9, 4], [7, 6, 5]].toString())
console.log(new Solution().generateMatrix(4).toString() === [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]].toString())
console.log(new Solution().generateMatrix(1).toString() === [[1]].toString())
