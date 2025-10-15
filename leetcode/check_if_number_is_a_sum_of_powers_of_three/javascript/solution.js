class Solution {
   /**
    * Time complexity: O(logn)
    *    O(log(3)n)
    * Auxiliary space complexity: O(logn)
    * Tags: greedy
    * @param {number} n
    * @return {boolean}
    */
   checkPowersOfThree(n) {
      const powers = [1];
      let index = 0;
      while (powers[powers.length - 1] <= n) {
         index++;
         powers.push(powers[powers.length - 1] * 3);
      }

      for (const power of powers.reverse()) {
         if (n - power >= 0)
            n -= power;

         if (n === 0)
            return true
      }
      return false
   };
}


const checkPowersOfThree = new Solution().checkPowersOfThree;
console.log(new Solution().checkPowersOfThree(12) === true)  // 12 = 3**1 + 3**2
console.log(new Solution().checkPowersOfThree(91) === true)  // 91 = 3**0 + 3**2 + 3**4
console.log(new Solution().checkPowersOfThree(21) === false)
console.log(new Solution().checkPowersOfThree(27) === true)  // 27 = 3**3