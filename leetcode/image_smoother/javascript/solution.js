class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: iteration
    * @param {number[][]} img
    * @return {number[][]}
    */
   imageSmoother(img) {
      const ROWS = img.length;
      const COLS = img[0].length;
      const smother = Array.from({ length: ROWS }, () => Array(COLS).fill(0))

      const squareMean = (row, col) => {
         let total = 0;
         let divider = 0;

         for (let r = row - 1; r <= row + 1; r++) {
            for (let c = col - 1; c <= col + 1; c++) {
               if (
                  r == -1 ||
                  r == ROWS ||
                  c == -1 ||
                  c == COLS
               )
                  continue
               total += img[r][c];
               divider++
            }
         }
         return parseInt(total / divider)
      };

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            smother[row][col] = squareMean(row, col);
         }
      }
      return smother
   };
}


const imageSmoother = new Solution().imageSmoother;
console.log(new Solution().imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
console.log(new Solution().imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]), [[137, 141, 137], [141, 138, 141], [137, 141, 137]])