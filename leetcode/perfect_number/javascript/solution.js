class Solution {
   /**
    * Time complexity: O(sqrtn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number} num
    * @return {boolean}
    */
   checkPerfectNumber(num) {
      if (num === 1) {
         return false;
      }
      
      let divisorSum = 1;

      for (let divisor = 2; divisor < Number(num ** 0.5); divisor++ ) {
         if (num % divisor === 0) {
            divisorSum += divisor;
            divisorSum += Math.floor(num / divisor);
         }
      }

      return divisorSum === num;
   }
}


const checkPerfectNumber = new Solution().checkPerfectNumber;
console.log(new Solution().checkPerfectNumber(28) === true)
console.log(new Solution().checkPerfectNumber(7) === false)
console.log(new Solution().checkPerfectNumber(6) === true)
console.log(new Solution().checkPerfectNumber(1) === false)
console.log(new Solution().checkPerfectNumber(99999996) === false)
