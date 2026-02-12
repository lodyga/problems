class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number[][]} original
    * @param {number} ROWS
    * @param {number} COLS
    * @return {number[][]}
    */
   construct2DArray(original, ROWS, COLS) {
      if (original.length !== ROWS * COLS) {
         return []
      }

      const res = Array.from({ length: ROWS }, () => Array(COLS));

      for (let index = 0; index < original.length; index++) {
         const row = Math.floor(index / COLS);
         const col = index % COLS;
         res[row][col] = original[index];
      }
      return res
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number[][]} original
    * @param {number} ROWS
    * @param {number} COLS
    * @return {number[][]}
    */
   construct2DArray(original, ROWS, COLS) {
      if (original.length !== ROWS * COLS) {
         return []
      }

      const res = Array.from({ length: ROWS }, () => Array(COLS));
      let index = 0;

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            res[row][col] = original[index];
            index++;
         }
      }

      return res
   };
}


const construct2DArray = new Solution().construct2DArray;
console.log(new Solution().construct2DArray([1, 2, 3, 4], 2, 2).toString() === [[1, 2], [3, 4]].toString())
console.log(new Solution().construct2DArray([1, 2, 3], 1, 3).toString() === [[1, 2, 3]].toString())
console.log(new Solution().construct2DArray([1, 2], 1, 1).toString() === [].toString())
