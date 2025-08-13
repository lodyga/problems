class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: backtracking, hash set
    * @param {number[][]} heights
    * @return {number[][]}
    */
   pacificAtlantic(heights) {
      const rows = heights.length;
      const cols = heights[0].length;
      const pacific = new Set();
      const atlantic = new Set();
      const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      const dfs = (row, col, ocean, prevHeight) => {
         if (
            row < 0 ||
            col < 0 ||
            row == rows ||
            col == cols ||
            heights[row][col] < prevHeight ||
            ocean.has(`${row},${col}`)
         ) return

         ocean.add(`${row},${col}`);
         for (const [r, c] of directions) {
            dfs(row + r, col + c, ocean, heights[row][col]);
         }
      }

      for (let row = 0; row < rows; row++) {
         dfs(row, 0, pacific, heights[row][0]);
         dfs(row, cols - 1, atlantic, heights[row][cols - 1]);
      }

      for (let col = 0; col < cols; col++) {
         dfs(0, col, pacific, heights[0][col]);
         dfs(rows - 1, col, atlantic, heights[rows - 1][col])
      }

      const bothOceans = [];
      for (const coordinates of pacific) {
         if (atlantic.has(coordinates))
         bothOceans.push(coordinates.split(',').map(Number))
      }
      return bothOceans
   };
}
const pacificAtlantic = new Solution().pacificAtlantic;


console.log((new Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]).sort().toString()) === ([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]).sort().toString())
console.log((new Solution().pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]]).sort().toString()) === ([[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]).sort().toString())
console.log((new Solution().pacificAtlantic([[1]]).sort().toString()) === ([[0, 0]]).sort().toString())