class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array (matrix)
    *     A: two pointers
    * @param {string[][]} boxGrid
    * @return {string[][]}
    */
   rotateTheBox(boxGrid) {
      const ROWS = boxGrid.length;
      const COLS = boxGrid[0].length;

      for (let row = 0; row < ROWS; row++) {
         let right = COLS - 1;
         const stoneRow = boxGrid[row];

         for (let left = COLS - 1; left > -1; left--) {
            const cell = stoneRow[left];

            if (cell === '#') {
               [stoneRow[left], stoneRow[right]] = [stoneRow[right], stoneRow[left]];
               right--;
            } else if (cell === '*')
               right = left - 1;
         }
      }
      return Array.from({ length: COLS }, (_, col) => Array.from({length: ROWS}, (_, row) => boxGrid[ROWS - 1 - row][col]));
      
      // const rotated = Array.from({ length: COLS }, () => Array(ROWS));
      // for (let col = 0; col < COLS; col++)
      //    for (let row = ROWS - 1; row > -1; row--)
      //       rotated[col][ROWS - 1 - row] = boxGrid[row][col]
      // return rotated
   };
}


const rotateTheBox = new Solution().rotateTheBox;
console.log(new Solution().rotateTheBox([['#', '.', '#']]).toString() === [['.'], ['#'], ['#']].toString())
console.log(new Solution().rotateTheBox([['#', '.', '#', '.']]).toString() === [['.'], ['.'], ['#'], ['#']].toString())
console.log(new Solution().rotateTheBox([['#', '.', '*', '.']]).toString() === [['.'], ['#'], ['*'], ['.']].toString())
console.log(new Solution().rotateTheBox([['#', '.', '*', '#', '.']]).toString() === [['.'], ['#'], ['*'], ['.'], ['#']].toString())
console.log(new Solution().rotateTheBox([['#', '.', '*', '.'], ['#', '#', '*', '.']]).toString() === [['#', '.'], ['#', '#'], ['*', '*'], ['.', '.']].toString())
console.log(new Solution().rotateTheBox([['#', '#', '*', '.', '*', '.'], ['#', '#', '#', '*', '.', '.'], ['#', '#', '#', '.', '#', '.']]).toString() === [['.', '#', '#'], ['.', '#', '#'], ['#', '#', '*'], ['#', '*', '.'], ['#', '.', '*'], ['#', '.', '.']].toString())
