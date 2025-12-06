class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: hash set
    *     A: iteration
    * @param {string[][]} board
    * @return {boolean}
   */
   isValidSudoku(board) {
      const rows = board.length;
      const cols = board[0].length;

      const areRowsValid = () => {
         for (let row = 0; row < rows; row++) {
            const rowValues = new Set();

            for (let col = 0; col < cols; col++) {
               const cell = board[row][col];
               if (cell === '.') {
                  continue
               } else if (rowValues.has(cell)) {
                  return false
               } else {
                  rowValues.add(cell);
               }
            }
         }
         return true
      };

      const areColsValid = () => {
         for (let col = 0; col < cols; col++) {
            const colValues = new Set();

            for (let row = 0; row < rows; row++) {
               const cell = board[row][col];
               if (cell === '.') {
                  continue
               } else if (colValues.has(cell)) {
                  return false
               } else {
                  colValues.add(cell);
               }
            }
         }
         return true
      };

      const areBoxesValid = () => {
         const isBoxBalid = (row, col) => {
            const boxValues = new Set();
            for (let i = row; i < row + 3; i++) {
               for (let j = col; j < col + 3; j++) {
                  const cell = board[i][j];
                  if (cell === '.')
                     continue
                  else if (boxValues.has(cell)) {
                     return false
                  } else
                     boxValues.add(cell);
               }
            }
            return true
         };

         for (let row = 0; row < rows; row = row + 3) {
            for (let col = 0; col < cols; col = col + 3) {
               if (isBoxBalid(row, col) === false)
                  return false
            }
         }
         return true
      };

      return (
         areRowsValid() &&
         areColsValid() &&
         areBoxesValid()
      )
   }
}


const isValidSudoku = new Solution().isValidSudoku;
console.log(new Solution().isValidSudoku([['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]) === true)
console.log(new Solution().isValidSudoku([['8', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]) === false)
console.log(new Solution().isValidSudoku([['.', '.', '.', '.', '5', '.', '.', '1', '.'], ['.', '4', '.', '3', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '3', '.', '.', '1'], ['8', '.', '.', '.', '.', '.', '.', '2', '.'], ['.', '.', '2', '.', '7', '.', '.', '.', '.'], ['.', '1', '5', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '2', '.', '.', '.'], ['.', '2', '.', '9', '.', '.', '.', '.', '.'], ['.', '.', '4', '.', '.', '.', '.', '.', '.']]) === false)
