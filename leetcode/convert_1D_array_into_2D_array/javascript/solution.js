class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: matrix
    * @param {number[][]} original
    * @param {number} ROWS
    * @param {number} COLS
    * @return {number[][]}
    */
   construct2DArray(original, ROWS, COLS) {
      if (original.length !== ROWS * COLS)
         return []

      const matrix = Array.from({ length: ROWS }, () => Array(COLS).fill(0));

      for (let index = 0; index < original.length; index++) {
         const row = Math.floor(index / COLS);
         const col = index % COLS;
         matrix[row][col] = original[index];
      }
      return matrix
   };
}


const construct2DArray = new Solution().construct2DArray;
console.log(new Solution().construct2DArray([1, 2, 3, 4], 2, 2), [[1, 2], [3, 4]])
console.log(new Solution().construct2DArray([1, 2, 3], 1, 3), [[1, 2, 3]])
console.log(new Solution().construct2DArray([1, 2], 1, 1), [])