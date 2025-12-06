class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack
    *     A: iteration
    * @param {string[]} directions
    * @return {string[]}
   */
   dirReduc(directions) {
      const directionStack = [];
      const oppositeDirection = new Map([
         ['NORTH', 'SOUTH'],
         ['SOUTH', 'NORTH'],
         ['EAST', 'WEST'],
         ['WEST', 'EAST']
      ]);

      for (const direction of directions) {
         if (directionStack[directionStack.length - 1] === oppositeDirection.get(direction)) {
            directionStack.pop();
         } else {
            directionStack.push(direction);
         }
      }
      return directionStack
   }
};


const dirReduc = new Solution().dirReduc;
console.log(new Solution().dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']), ['WEST'])
console.log(new Solution().dirReduc(['NORTH', 'EAST', 'WEST', 'SOUTH', 'WEST', 'WEST']), ['WEST', 'WEST'])
console.log(new Solution().dirReduc(['NORTH', 'WEST', 'SOUTH', 'EAST']), ['NORTH', 'WEST', 'SOUTH', 'EAST'])
console.log(new Solution().dirReduc([]), [])
