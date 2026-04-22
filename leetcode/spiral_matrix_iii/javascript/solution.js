class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number} rows
    * @param {number} cols
    * @param {number} rStart
    * @param {number} cStart
    * @return {number[][]}
    */
   spiralMatrixIII(rows, cols, rStart, cStart) {
      const DIM = rows * cols;
      // left, down, up, right
      let directions = [1, 1, 2, 2];
      let x = cStart;
      let y = rStart;
      const res = [[y, x]];

      while (res.length < DIM) {
         for (let index = 1; index <= directions[0]; index++) {
            x++;
            if (-1 < y && y < rows && -1 < x && x < cols) {
               res.push([y, x]);
            }
         }

         for (let index = 1; index <= directions[1]; index++) {
            y++;
            if (-1 < y && y < rows && -1 < x && x < cols) {
               res.push([y, x]);
            }
         }

         for (let index = 1; index <= directions[2]; index++) {
            x--;
            if (-1 < y && y < rows && -1 < x && x < cols) {
               res.push([y, x]);
            }
         }

         for (let index = 1; index <= directions[3]; index++) {
            y--;
            if (-1 < y && y < rows && -1 < x && x < cols) {
               res.push([y, x]);
            }
         }

         for (let index = 0; index < 4; index++) {
            directions[index] += 2;
         }
      }

      return res
   };
}


const spiralMatrixIII = new Solution().spiralMatrixIII;
console.log(new Solution().spiralMatrixIII(1, 4, 0, 0).toString() === [[0, 0], [0, 1], [0, 2], [0, 3]].toString())
console.log(new Solution().spiralMatrixIII(5, 6, 1, 4).toString() === [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]].toString())
console.log(new Solution().spiralMatrixIII(3, 3, 1, 1).toString() === [[1, 1], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2]].toString())
console.log(new Solution().spiralMatrixIII(3, 3, 2, 2).toString() === [[2, 2], [2, 1], [1, 1], [1, 2], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2]].toString())
