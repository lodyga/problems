class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set, hash map
    *     A: iteration
    * @param {string} path
    * @return {boolean}
    */
   isPathCrossing(path) {
      const DIRECTIONS = new Map([['E', [1, 0]], ['W', [-1, 0]], ['N', [0, 1]], ['S', [0, -1]]]);
      let x = 0;
      let y = 0;
      const visited = new Set([`${x},${y}`]);

      for (const direction of path) {
         const [dx, dy] = DIRECTIONS.get(direction);
         x += dx;
         y += dy;

         if (visited.has(`${x},${y}`))
            return true
         else
            visited.add(`${x},${y}`)
      }
      return false
   };
}


const isPathCrossing = new Solution().isPathCrossing;
console.log(new Solution().isPathCrossing('NES') === false)
console.log(new Solution().isPathCrossing('WNSN') === true)
console.log(new Solution().isPathCrossing('NESWW') === true)
