class Solution {
   /**
    * Time complexity: O(4^n)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking with pruning
    * @param {number[]} matchsticks
    * @return {boolean}
    */
   makesquare(matchsticks) {
      const perimeter = matchsticks.reduce((sum, value) => sum + value, 0);
      if (perimeter % 4) return false
      const sideLength = perimeter >> 2;
      const sides = Array(4).fill(sideLength);
      matchsticks.sort((a, b) => b - a);
      return dfs(0)

      function dfs(index) {
         if (index === matchsticks.length) {
            return true
         }
         for (let sideIndex = 0; sideIndex < 4; sideIndex++) {
            sides[sideIndex] -= matchsticks[index];
            if (
               sides[sideIndex] >= 0 && 
               dfs(index + 1)
            ) {
               return true
            }
            sides[sideIndex] += matchsticks[index];
            
            if (
               sides[sideIndex] === sideLength ||
               sides[sideIndex] - matchsticks[index] === 0
            ) {
               break
            }
         }
         return false
      }
   };
}
const makesquare = new Solution().makesquare;


console.log(new Solution().makesquare([1, 1, 1, 1]) === true)
console.log(new Solution().makesquare([1, 1, 2, 2, 2]) === true)
console.log(new Solution().makesquare([3, 3, 3, 3, 4]) === false)
console.log(new Solution().makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) === true)
console.log(new Solution().makesquare([7215807, 6967211, 5551998, 6632092, 2802439, 821366, 2465584, 9415257, 8663937, 3976802, 2850841, 803069, 2294462, 8242205, 9922998]) === false)
console.log(new Solution().makesquare([10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]) === true)