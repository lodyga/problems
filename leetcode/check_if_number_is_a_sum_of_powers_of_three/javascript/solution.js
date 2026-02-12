class Solution {
   /**
    * Time complexity: O(logn)
    *     O(log(3)n)
    * Auxiliary space complexity: O(logn)
    * Tags:
    *     DS: list
    *     A: iteration
    * @param {number} n
    * @return {boolean}
    */
   checkPowersOfThree(n) {
      const powers = [];
      let power = 1;

      while (power <= n) {
         powers.push(power);
         power *= 3;
      }

      for (const power of powers.reverse()) {
         if (n - power >= 0) {
            n -= power;
            if (n === 0) {
               return true
            }
         }
      }
      return false
   };
}


const checkPowersOfThree = new Solution().checkPowersOfThree;
console.log(new Solution().checkPowersOfThree(12) === true)
console.log(new Solution().checkPowersOfThree(91) === true)
console.log(new Solution().checkPowersOfThree(21) === false)
console.log(new Solution().checkPowersOfThree(27) === true)
