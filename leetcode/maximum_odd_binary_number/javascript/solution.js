class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: string
    *     A: iteration
    * @param {string} num
    * @return {string}
    */
   maximumOddBinaryNumber(num) {
      let odd = 0;
      let even = 0;

      for (const digit of num) {
         digit === '1' ? odd++ : even++;
      }
      return '1'.repeat(odd - 1) + '0'.repeat(even) + '1'
   };
}


const maximumOddBinaryNumber = new Solution().maximumOddBinaryNumber;
console.log(new Solution().maximumOddBinaryNumber('1') === '1')
console.log(new Solution().maximumOddBinaryNumber('10') === '01')
console.log(new Solution().maximumOddBinaryNumber('010') === '001')
console.log(new Solution().maximumOddBinaryNumber('0101') === '1001')
