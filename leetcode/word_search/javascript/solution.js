class Solution {
   /**
    * Time complexity: O(nm*3^k)
    *     k: word length
    * Auxiliary space complexity: O(nm)
    * Tags: backtracking
    * @param {string[][]} board
    * @param {string} word
    * @return {boolean}
    */
   exist(board, word) {
      const rows = board.length;
      const cols = board[0].length;
      const directoins = [[-1, 0], [1, 0], [0, -1], [0, 1]]

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            if (dfs(0, row, col))
               return true
         }
      }
      return false

      function dfs(index, row, col) {
         if (index === word.length)
            return true
         else if (
            row < 0 ||
            col < 0 ||
            row === rows ||
            col === cols ||
            board[row][col] !== word[index]
         )
            return

         board[row][col] = '#';
         let isPathRight = directoins.some(([r, c]) => dfs(index + 1, row + r, col + c))

         board[row][col] = word[index];
         return isPathRight
      }
   };
}


console.log(new Solution().exist([['C', 'A', 'A']], 'AA') === true)
console.log(new Solution().exist([['C', 'A', 'A'], ['C', 'C', 'B']], 'AAB') === true)
console.log(new Solution().exist([['C', 'A', 'A'], ['A', 'A', 'A'], ['B', 'C', 'D']], 'AAB') === true)
console.log(new Solution().exist([['C', 'A', 'A'], ['A', 'A', 'A'], ['B', 'C', 'D']], 'AACA') === true)
console.log(new Solution().exist([['A', 'A']], 'AAA') === false)
console.log(new Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']], 'ABCEFSADEESE') === true)
console.log(new Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'AB') === true)
console.log(new Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'AZ') === false)
console.log(new Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABFS') === true)
console.log(new Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED') === true)
console.log(new Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE') === true)
console.log(new Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB') === false)