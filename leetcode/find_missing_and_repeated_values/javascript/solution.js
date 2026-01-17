class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number[][]} grid
    * @return {number[]}
    */
   findMissingAndRepeatedValues(grid) {
      const N = grid.length;
      const DIMS = grid.length ** 2;
      const seen = Array(DIMS).fill(false);
      const res = [];

      for (let row = 0; row < N; row++) {
         for (let col = 0; col < N; col++) {
            const num = grid[row][col];
            if (seen[num - 1]) {
               res.push(num);
            }
            seen[num - 1] = true;
         }
      }

      for (let index = 0; index < DIMS; index++) {
         if (!seen[index]) {
            res.push(index + 1);
         }
      }
      return res
   };
}


const findMissingAndRepeatedValues = new Solution().findMissingAndRepeatedValues;
console.log(new Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]).toString() === [2, 4].toString())
console.log(new Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]).toString() === [9, 5].toString())
