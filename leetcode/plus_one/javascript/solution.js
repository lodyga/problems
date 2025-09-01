class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: iteration
    * @param {number[]} digits
    * @return {number[]}
    */
   plusOne(digits) {
      let carry = true;
      let index = digits.length - 1;

      while (index > -1 && carry) {
         if (digits[index] === 9) {
            digits[index] = 0;
            carry = true;
         } else {
            digits[index] += 1;
            carry = false
         }
         index--;
      }

      if (carry) {
         digits.splice(0, 0, 1)
      }
      
      return digits
   };
}
const plusOne = new Solution().plusOne;


console.log(new Solution().plusOne([1, 2, 3]), [1, 2, 4])
console.log(new Solution().plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
console.log(new Solution().plusOne([9]), [1, 0])
console.log(new Solution().plusOne([9, 9]), [1, 0, 0])