class Solution {
   /**
    * Time complexity: O(n2*3^k)
    *     n: board length
    *     k: word length
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: backtracking
    * @param {string[][]} board
    * @param {string} word
    * @return {boolean}
    */
   exist(board, word) {
      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const backtrack = (index, row, col) => {
         if (index === word.length) {
            return true
         } else if (
            row < 0 ||
            col < 0 ||
            row === ROWS ||
            col === COLS ||
            board[row][col] !== word[index] ||
            visited[row][col]
         )
            return false

         visited[row][col] = true;

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            if (backtrack(index + 1, r, c)) {
               return true
            }
         }
         visited[row][col] = false;
         return false
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (backtrack(0, row, col))
               return true
         }
      }
      return false
   };
}


const exist = new Solution().exist;
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
