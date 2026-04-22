class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   arraySign(nums) {
      let isPositive = true;

      for (const num of nums) {
         if (num === 0) {
            return 0
         } else if (num < 0) {
            isPositive = !isPositive;
         }
      }

      return isPositive ? 1 : -1
   };
}


const arraySign = new Solution().arraySign;
console.log(new Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]) === 1)
console.log(new Solution().arraySign([1, 5, 0, 2, -3]) === 0)
console.log(new Solution().arraySign([-1, 1, -1, 1, -1]) === -1)
