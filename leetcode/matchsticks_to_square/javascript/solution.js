class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: backtracking with pruning, sorting
    * @param {number[]} sticks
    * @return {boolean}
    */
   makesquare(sticks) {
      const perimeter = sticks.reduce((sum, val) => sum + val, 0);

      if (perimeter % 4) {
         return false
      }

      const sideLength = perimeter / 4;
      sticks.sort((a, b) => b - a);
      const sides = [0, 0, 0, 0];

      const backtrack = (idx) => {
         if (idx === sticks.length) {
            return true
         }

         const stick = sticks[idx];

         for (let sideIdx = 0; sideIdx < 4; sideIdx++) {
            if (sides[sideIdx] + stick <= sideLength) {
               sides[sideIdx] += stick;
               if (backtrack(idx + 1)) {
                  return true;
               }
               sides[sideIdx] -= stick;
            }

            // pruning
            if (sides[sideIdx] === 0) {
               break;
            }
         }

         return false;
      }

      return backtrack(0);
   }
}


const makesquare = new Solution().makesquare;
console.log(new Solution().makesquare([1, 1, 1, 1]) === true)
console.log(new Solution().makesquare([1, 1, 2, 2, 2]) === true)
console.log(new Solution().makesquare([3, 3, 3, 3, 4]) === false)
console.log(new Solution().makesquare([3, 3, 2, 2, 2]) === false)
console.log(new Solution().makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) === true)
console.log(new Solution().makesquare([10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]) === true)
console.log(new Solution().makesquare([7215807, 6967211, 5551998, 6632092, 2802439, 821366, 2465584, 9415257, 8663937, 3976802, 2850841, 803069, 2294462, 8242205, 9922998]) === false)
