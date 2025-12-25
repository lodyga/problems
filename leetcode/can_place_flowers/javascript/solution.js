class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy, iteration
    * @param {number[]} plots
    * @param {number} k
    * @return {boolean}
    */
   canPlaceFlowers(plots, k) {
      if (k == 0) {
         return true
      }
      let index = 0;
      while (index < plots.length) {
         if (
            index + 1 < plots.length &&
            plots[index + 1] === 1
         ) {
            index += 1;
         } else if (
            (
               plots[index] == 0 &&
               (index == plots.length - 1 || plots[index + 1] == 0)
            )
         ) {
            k -= 1;
            if (k == 0)
               return true
         }
         index += 2
      }
      return false
   };
}


const canPlaceFlowers = new Solution().canPlaceFlowers;
console.log(new Solution().canPlaceFlowers([0, 0, 0], 2) === true)
console.log(new Solution().canPlaceFlowers([0, 1, 0], 1) === false)
console.log(new Solution().canPlaceFlowers([1, 0, 0, 0], 1) === true)
console.log(new Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1) === true)
console.log(new Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2) === false)
console.log(new Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1) === true)
console.log(new Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) === false)
console.log(new Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0) === true)
console.log(new Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2) === true)
