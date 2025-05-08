class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {string} number
    * @return {string}
    */
   maximumOddBinaryNumber(number) {
      let ones = 0;
      let zeros = 0;

      for (const digit of number) {
         if (digit === '1')
            ones++;
         else
            zeros++;
      }
      return '1'.repeat(ones - 1) + '0'.repeat(zeros) + '1'
   };
}
const maximumOddBinaryNumber = new Solution().maximumOddBinaryNumber;


console.log(new Solution().maximumOddBinaryNumber("1"), "1")
console.log(new Solution().maximumOddBinaryNumber("10"), "01")
console.log(new Solution().maximumOddBinaryNumber("010"), "001")
console.log(new Solution().maximumOddBinaryNumber("0101"), "1001")