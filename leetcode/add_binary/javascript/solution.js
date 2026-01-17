class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: string
    *     A: iteration
    * @param {string} a
    * @param {string} b
    * @return {string}
    */
   addBinary(a, b) {
      let index1 = a.length - 1;
      let index2 = b.length - 1;
      const res = [];
      let carry = false;

      while (index1 > -1 || index2 > -1 || carry) {
         const num1 = index1 > -1 ? a[index1] : '0';
         const num2 = index2 > -1 ? b[index2] : '0';

         if (num1 === '0' && num2 === '0') {
            carry ? res.push('1') : res.push('0');
            carry = false;
         } else if (num1 === '1' && num2 === '1') {
            carry ? res.push('1') : res.push('0');
            carry = true;
         } else {
            carry ? res.push('0') : res.push('1');
         }
         index1--;
         index2--;
      }
      return res.reverse().join('');
   };
}


const addBinary = new Solution().addBinary;
console.log(new Solution().addBinary('11', '1') === '100')
console.log(new Solution().addBinary('1010', '1011') === '10101')
console.log(new Solution().addBinary('11', '11') === '110')
