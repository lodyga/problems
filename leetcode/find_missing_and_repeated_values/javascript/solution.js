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
      const seen = Array(N * N).fill(false);
      const res = [];

      for (let row = 0; row < N; row++) {
         for (let col = 0; col < N; col++) {
            const val = grid[row][col];

            if (seen[val - 1]) {
               res.push(val);
            }
            else {
               seen[val - 1] = true;
            }
         }
      }

      for (let idx = 0; idx < seen.length; idx++) {
         if (!seen[idx]) {
            res.push(idx + 1);
         }
      }

      return res;
   }
}


const findMissingAndRepeatedValues = new Solution().findMissingAndRepeatedValues;
console.log(new Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]).toString() === [2, 4].toString())
console.log(new Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]).toString() === [9, 5].toString())
