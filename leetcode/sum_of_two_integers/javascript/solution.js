class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number} a
    * @param {number} b
    * @return {number}
    */
   getSum(a, b) {
      while (b) {
         const carry = (a & b) << 1;
         a = a ^ b;
         b = carry;
      }
      return a
   };
}
const getSum = new Solution().getSum;


console.log(new Solution().getSum(1, 2) === 3)
console.log(new Solution().getSum(2, 3) === 5)
console.log(new Solution().getSum(-1, 1) === 0)
console.log(new Solution().getSum(-12, -8) === -20)