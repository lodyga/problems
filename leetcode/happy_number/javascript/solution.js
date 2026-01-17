class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(logn)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number} num
    * @return {boolean}
    */
   isHappy(num) {
      const sumOfSquares = (num) => {
         let nextNumber = 0;
         while (num) {
            nextNumber += (num % 10) ** 2;
            num = Math.floor(num / 10);
         }
         return nextNumber
      };

      const prevNumbers = new Set();
      while (!prevNumbers.has(num)) {
         prevNumbers.add(num);
         num = sumOfSquares(num);

         if (num === 1)
            return true
      }
      return false
   };

   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash set
    *     A: two pointers, Floyd
    * @param {number} num
    * @return {boolean}
    */
   isHappy(num) {
      const sumOfSquares = (num) => {
         let nextNumber = 0;
         while (num) {
            nextNumber += (num % 10) ** 2;
            num = Math.floor(num / 10);
         }
         return nextNumber
      };
      let slow = num;
      let fast = sumOfSquares(num);

      while (slow !== 1 && fast !== 1) {
         if (slow === fast)
            return false

         slow = sumOfSquares(slow);
         fast = sumOfSquares(fast);
         fast = sumOfSquares(fast);
      }
      return true
   };
}


const isHappy = new Solution().isHappy;
console.log(new Solution().isHappy(19) === true)
console.log(new Solution().isHappy(2) === false)
console.log(new Solution().isHappy(7) === true)
console.log(new Solution().isHappy(100) === true)
console.log(new Solution().isHappy(101) === false)
console.log(new Solution().isHappy(1) === true)
