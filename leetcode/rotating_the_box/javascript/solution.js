class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string[][]} boxGrid
    * @return {string[][]}
    */
   rotateTheBox(boxGrid) {
      const ROWS = boxGrid.length;
      const COLS = boxGrid[0].length;

      for (let row = 0; row < ROWS; row++) {
         let right = COLS - 1;

         for (let col = COLS - 1; col > -1; col--) {
            const cell = boxGrid[row][col];
            if (cell === '#') {
               [boxGrid[row][col], boxGrid[row][right]] = [boxGrid[row][right], boxGrid[row][col]];
               right--;
            } else if (cell === '*')
               right = col - 1;
         }
      }
      const rotated = Array.from({ length: COLS }, () => Array(ROWS).fill('.'));
      for (let col = 0; col < COLS; col++)
         for (let row = ROWS - 1; row > -1; row--)
            rotated[col][ROWS - 1 - row] = boxGrid[row][col]
      return rotated
   };
}


const rotateTheBox = new Solution().rotateTheBox;
console.log(new Solution().rotateTheBox([['#', '.', '#']]), [['.'], ['#'], ['#']])
console.log(new Solution().rotateTheBox([['#', '.', '#', '.']]), [['.'], ['.'], ['#'], ['#']])
console.log(new Solution().rotateTheBox([['#', '.', '*', '.']]), [['.'], ['#'], ['*'], ['.']])
console.log(new Solution().rotateTheBox([['#', '.', '*', '#', '.']]), [['.'], ['#'], ['*'], ['.'], ['#']])
console.log(new Solution().rotateTheBox([['#', '.', '*', '.'], ['#', '#', '*', '.']]), [['#', '.'], ['#', '#'], ['*', '*'], ['.', '.']])
console.log(new Solution().rotateTheBox([['#', '#', '*', '.', '*', '.'], ['#', '#', '#', '*', '.', '.'], ['#', '#', '#', '.', '#', '.']]), [['.', '#', '#'], ['.', '#', '#'], ['#', '#', '*'], ['#', '*', '.'], ['#', '.', '*'], ['#', '.', '.']])