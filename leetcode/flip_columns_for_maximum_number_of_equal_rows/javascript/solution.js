class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, string
    *     A: iteration
    * @param {number[][]} matrix
    * @return {number}
    */
   maxEqualRowsAfterFlips(matrix) {
      const binCount = new Map();

      for (const row of matrix) {
         let rowHash = '';

         if (row[0] === 0) {
            rowHash = row.join('');
         } else {
            rowHash = row.map((val => val ? 0 : 1)).join('');
         }

         binCount.set(rowHash, (binCount.get(rowHash) || 0) + 1);
      }

      return Math.max(...binCount.values())
   };
}


const maxEqualRowsAfterFlips = new Solution().maxEqualRowsAfterFlips;
console.log(new Solution().maxEqualRowsAfterFlips([[0, 1], [1, 1]]) === 1)
console.log(new Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]]) === 2)
console.log(new Solution().maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]) === 2)
console.log(new Solution().maxEqualRowsAfterFlips([[1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]) === 2)
