class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {string[]} directionList
    * @return {string[]}
   */
   dirReduc(directionList) {
      const visitedDirections = [];
      const oppositeDirection = {
         "NORTH": "SOUTH",
         "SOUTH": "NORTH",
         "EAST": "WEST",
         "WEST": "EAST",
      };

      for (const direction of directionList) {
         if (visitedDirections[visitedDirections.length - 1] == oppositeDirection[direction]) {
            visitedDirections.pop();
         } else {
            visitedDirections.push(direction);
         }
      }
      return visitedDirections
   }
}
const solution = new Solution();
console.log(new Solution().dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])
console.log(new Solution().dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]), ["WEST", "WEST"])
console.log(new Solution().dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])
console.log(new Solution().dirReduc([]), [])
