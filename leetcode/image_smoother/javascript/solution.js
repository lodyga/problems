class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number[][]} img
    * @return {number[][]}
    */
   imageSmoother(img) {
      const ROWS = img.length;
      const COLS = img[0].length;
      const res = Array.from({ length: ROWS }, () => Array(COLS).fill(0))

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            let cell = 0;
            let divider = 0;

            for (let r = row - 1; r <= row + 1; r++) {
               for (let c = col - 1; c <= col + 1; c++) {
                  if (
                     r == -1 || r == ROWS ||
                     c == -1 || c == COLS
                  )
                     continue
                  cell += img[r][c];
                  divider++
               }
            }
            res[row][col] = Math.floor(cell / divider);
         }
      }
      return res
   };

   /**
    * Time complexity: O(n2)
    * Result space complexity: O(1)
    * Tags:
    *     A: iteration, bit manipulation, in-place method
    * @param {number[][]} img
    * @return {number[][]}
    */
   imageSmoother(img) {
      const ROWS = img.length;
      const COLS = img[0].length;

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            let cell = 0;
            let divider = 0;

            for (let r = row - 1; r <= row + 1; r++) {
               for (let c = col - 1; c <= col + 1; c++) {
                  if (
                     r == -1 || r == ROWS ||
                     c == -1 || c == COLS
                  )
                     continue
                  cell += img[r][c] & 255;
                  divider++
               }
            }
            img[row][col] |= Math.floor(cell / divider) << 8;
         }
      }
      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            img[row][col] >>= 8;
         }
      }

      return img
   };
}


const imageSmoother = new Solution().imageSmoother;
console.log(new Solution().imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]).toString() === [[0, 0, 0], [0, 0, 0], [0, 0, 0]].toString())
console.log(new Solution().imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]).toString() === [[137, 141, 137], [141, 138, 141], [137, 141, 137]].toString())
