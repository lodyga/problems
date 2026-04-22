class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {string} instructions
    * @return {boolean}
    */
   isRobotBounded(instructions) {
      let [x, y] = [0, 0];
      let [dx, dy] = [0, 1];

      for (const ins of instructions) {
         if (ins === 'L') {
            // (0, 1) => (-1, 0) => (0, -1)
            [dx, dy] = [-dy, dx];
         } else if (ins === 'R') {
            // (0, 1) => (1, 0) => (0, -1)
            [dx, dy] = [dy, -dx];
         }
         else {
            x += dx;
            y += dy;
         }
      }

      return (
         x === 0 && y == 0 ||
         dx !== 0 || dy !== 1
      )
   };
}


const isRobotBounded = new Solution().isRobotBounded;
console.log(new Solution().isRobotBounded('GGLLGG') === true)
console.log(new Solution().isRobotBounded('GG') === false)
console.log(new Solution().isRobotBounded('GL') === true)
