class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(logn)
    * Tags: hash set
    * @param {number} number
    * @return {boolean}
    */
   isHappy(number) {
      const sumOfSquares = (numebr) => {
         let newNumber = 0;
         while (number) {
            newNumber += (number % 10) ** 2;
            number = number / 10 | 0;
         }
         return newNumber
      };

      const prevNumbers = new Set();
      while (!prevNumbers.has(number)) {
         prevNumbers.add(number);
         number = sumOfSquares(number);

         if (number === 1)
            return true
      }
      return false
   };
}
const isHappy = new Solution().isHappy;


console.log(new Solution().isHappy(19) === true)
console.log(new Solution().isHappy(2) === false)
console.log(new Solution().isHappy(7) === true)
console.log(new Solution().isHappy(100) === true)
console.log(new Solution().isHappy(101) === false)