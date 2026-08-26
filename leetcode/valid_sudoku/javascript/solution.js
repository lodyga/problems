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

      const validateRows = () => {
         for (let row = 0; row < 9; row++) {
            const rowValues = Array(9).fill(false);

            for (let col = 0; col < 9; col++) {
               const cell = board[row][col];

               if (cell === '.') {
                  continue;
               }

               const val = cell.charCodeAt(0) - '1'.charCodeAt(0);

               if (rowValues[val]) {
                  return false;
               }

               rowValues[val] = true;
            }
         }

         return true;
      };

      const validateCols = () => {
         for (let col = 0; col < 9; col++) {
            const colValues = Array(9).fill(false);

            for (let row = 0; row < 9; row++) {
               const cell = board[row][col];

               if (cell === '.') {
                  continue;
               }

               const val = cell.charCodeAt(0) - '1'.charCodeAt(0);

               if (colValues[val]) {
                  return false;
               }

               colValues[val] = true;
            }
         }

         return true;
      };

      const validateSubboxes = () => {

         const validateSubbox = (row, col) => {
            const boxValues = Array(9).fill(false);

            for (let i = row; i < row + 3; i++) {
               for (let j = col; j < col + 3; j++) {
                  const cell = board[i][j];

                  if (cell === '.') {
                     continue;
                  }

                  const val = cell.charCodeAt(0) - '1'.charCodeAt(0);

                  if (boxValues[val]) {
                     return false;
                  }

                  boxValues[val] = true;
               }
            }

            return true;
         };

         for (let row = 0; row < 9; row = row + 3) {
            for (let col = 0; col < 9; col = col + 3) {
               if (validateSubbox(row, col) === false) {
                  return false;
               }
            }
         }

         return true;
      }

      return (
         validateRows()
         && validateCols()
         && validateSubboxes()
      );
   }
}


const isValidSudoku = new Solution().isValidSudoku;
console.log(new Solution().isValidSudoku([['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]) === true)
console.log(new Solution().isValidSudoku([['8', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]) === false)
console.log(new Solution().isValidSudoku([['.', '.', '.', '.', '5', '.', '.', '1', '.'], ['.', '4', '.', '3', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '3', '.', '.', '1'], ['8', '.', '.', '.', '.', '.', '.', '2', '.'], ['.', '.', '2', '.', '7', '.', '.', '.', '.'], ['.', '1', '5', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '2', '.', '.', '.'], ['.', '2', '.', '9', '.', '.', '.', '.', '.'], ['.', '.', '4', '.', '.', '.', '.', '.', '.']]) === false)
