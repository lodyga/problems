import { Deque } from "@datastructures-js/deque";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: deque, array (matrix)
    *     A: BFS
    * @param {number[][]} board
    * @return {number}
    */
   snakesAndLadders(board) {
      const getBoradVal = (index) => {
         index--;
         const row = Math.floor(index / COLS);
         let col = index % COLS;
         col = row % 2 ? COLS - 1 - col : col
         const val = board[row][col];
         return val == -1 ? index + 1 : val
      }

      const ROWS = board.length;
      const COLS = board[0].length;
      const N = ROWS * COLS;
      const visited = Array(N + 1).fill(false);
      board.reverse();

      const bfs = (moves, boardVal) => {
         const rollQueue = new Deque([[moves, boardVal]]);
         visited[boardVal] = true;

         while (rollQueue.size()) {

            const [moves, cellIndex] = rollQueue.popFront();

            for (let dieRoll = 1; dieRoll < 7; dieRoll++) {
               const nextCell = cellIndex + dieRoll;
               const boardVal = getBoradVal(nextCell);

               if (visited[boardVal]) {
                  continue
               } else if (boardVal === N) {
                  return moves + 1
               }

               rollQueue.pushBack([moves + 1, boardVal]);
               visited[boardVal] = true;
            }
         }

         return -1
      }
      return bfs(0, 1)
   };
}


const snakesAndLadders = new Solution().snakesAndLadders;
console.log(new Solution().snakesAndLadders([[-1, -1], [-1, 3]]) === 1)
console.log(new Solution().snakesAndLadders([[2, -1, -1], [-1, -1, -1], [-1, -1, -1]]) === 2)
console.log(new Solution().snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]) === 4)
console.log(new Solution().snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]) === -1)
console.log(new Solution().snakesAndLadders([[2, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) === 4)
