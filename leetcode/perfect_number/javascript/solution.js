class Solution {
   /**
    * Time complexity: O(sqrtn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number} target
    * @return {boolean}
    */
   checkPerfectNumber(target) {
      if (target === 1) {
         return false
      }
      let divisorSum = 1;

      for (let number = 2; number < Number(target ** 0.5); number++ ) {
         if (target % number === 0) {
            divisorSum += number;
            divisorSum += Math.floor(target / number);
         }
      }
      return divisorSum === target;
   };
}


const checkPerfectNumber = new Solution().checkPerfectNumber;
console.log(new Solution().checkPerfectNumber(28) === true)
console.log(new Solution().checkPerfectNumber(7) === false)
console.log(new Solution().checkPerfectNumber(6) === true)
console.log(new Solution().checkPerfectNumber(1) === false)
console.log(new Solution().checkPerfectNumber(99999996) === false)
