class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: iteration
    * @param {number[]} digits
    * @return {number[]}
    */
   plusOne(digits) {
      digits.reverse();
      let carry = 1;

      for (let index = 0; index < digits.length; index++) {
         let digit = digits[index] + carry;
         carry = 0;
         if (digit === 10) {
            carry = 1;
            digit = 0;
         }
         digits[index] = digit;
      }

      if (carry) {
         digits.push(1);
      }

      return digits.reverse()
   };
}


const plusOne = new Solution().plusOne;
console.log(new Solution().plusOne([1, 2, 3]).toString() === [1, 2, 4].toString())
console.log(new Solution().plusOne([4, 3, 2, 1]).toString() === [4, 3, 2, 2].toString())
console.log(new Solution().plusOne([9]).toString() === [1, 0].toString())
console.log(new Solution().plusOne([9, 9]).toString() === [1, 0, 0].toString())
