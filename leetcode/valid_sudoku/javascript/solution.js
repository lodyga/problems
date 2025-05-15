class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags: hash set
    * @param {string[][]} board
    * @return {}
    */
   isValidSudoku(board) {
      const rows = board.length;
      const cols = board[0].length;

      for (let row = 0; row < rows; row++) {
         if (!isRowValid(row)) {
            return false
         }
      }
      for (let col = 0; col < cols; col++) {
         if (!isColValid(col)) {
            return false
         }
      }
      for (let row = 0; row < rows; row += 3) {
         for (let col = 0; col < cols; col += 3) {
            if (!isSubboxValid(row, col)) {
               return false
            }
         }
      }
      return true

      function isRowValid(row) {
         const uniqueNumbers = new Set();
         for (const char of board[row]) {
            if (char !== '.') {
               if (uniqueNumbers.has(char)) {
                  return false
               } else {
                  uniqueNumbers.add(char);
               }
            }
         }
         return true
      };

      function isColValid(col) {
         const uniqueNumbers = new Set();
         for (let row = 0; row < rows; row++) {
            const char = board[row][col]
            if (char !== '.') {
               if (uniqueNumbers.has(char)) {
                  return false
               } else {
                  uniqueNumbers.add(char);
               }
            }
         }
         return true
      };

      function isSubboxValid(row, col) {
         const uniqueNumbers = new Set();
         for (let r = 0; r < 3; r++) {
            for (let c = 0; c < 3; c++) {
               const char = board[row + r][col + c]
               if (char !== '.') {
                  if (uniqueNumbers.has(char)) {
                     return false
                  } else {
                     uniqueNumbers.add(char);
                  }
               }
            }
         }
         return true
      };

   };
}


console.log(new Solution().isValidSudoku([['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]) === true)
console.log(new Solution().isValidSudoku([['8', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]) === false)
console.log(new Solution().isValidSudoku([['.', '.', '.', '.', '5', '.', '.', '1', '.'], ['.', '4', '.', '3', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '3', '.', '.', '1'], ['8', '.', '.', '.', '.', '.', '.', '2', '.'], ['.', '.', '2', '.', '7', '.', '.', '.', '.'], ['.', '1', '5', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '2', '.', '.', '.'], ['.', '2', '.', '9', '.', '.', '.', '.', '.'], ['.', '.', '4', '.', '.', '.', '.', '.', '.']]) === false)