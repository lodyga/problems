class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} path
    * @return {boolean}
    */
   isPathCrossing(path) {
      let horizontal = 0;
      let vertical = 0;
      const visited = new Set([`${vertical},${horizontal}`]);

      for (const direction of path) {
         if (direction === 'E') 
            horizontal++;
         else if (direction === 'W') 
            horizontal--;
         else if (direction === 'N') 
            vertical++;
         else if (direction === 'S') 
            vertical--;

         if (visited.has(`${vertical},${horizontal}`))
            return true
         else
            visited.add(`${vertical},${horizontal}`);
      }
      return false
   };
}



class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} path
    * @return {boolean}
    */
   isPathCrossing = function (path) {
      const visited = new Set([`0,0`]);
      let prevVisit = [0, 0];
      let nextVisit = [0, 0];

      const DIRECTIONS = new Map([
         ['E', [1, 0]],
         ['W', [-1, 0]],
         ['N', [0, 1]],
         ['S', [0, -1]]
      ])

      for (const direction of path) {
         nextVisit = [
            prevVisit[0] + DIRECTIONS.get(direction)[0],
            prevVisit[1] + DIRECTIONS.get(direction)[1]
         ]

         if (visited.has(`${nextVisit[0]},${nextVisit[1]}`))
            return true
         else {
            visited.add(`${nextVisit[0]},${nextVisit[1]}`)
            prevVisit = nextVisit;
         }
      }

      return false
   };
}


console.log(new Solution().isPathCrossing('NES'), false)
console.log(new Solution().isPathCrossing('WNSN'), true)
console.log(new Solution().isPathCrossing('NESWW'), true)