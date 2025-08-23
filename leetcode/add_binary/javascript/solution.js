class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: bit manipulation
    * @param {string} a
    * @param {string} b
    * @return {string}
    */
   addBinary(a, b) {
      // return (parseInt(a, 2) + parseInt(b, 2)).toString(2)
      a = a.split('').reverse().join('');
      b = b.split('').reverse().join('');
      let carry = '0';
      let binSum = '';
      let binNumber = '';

      for (let index = 0; index < Math.max(a.length, b.length); index++) {
         const charA = index < a.length ? a[index] : '0';
         const charB = index < b.length ? b[index] : '0';

         if (carry === '0') {
            if (charA === '0' && charB === '0') {
               binNumber = '0';
               carry = '0'
            } else if (charA === '0' && charB === '1') {
               binNumber = '1';
               carry = '0'
            } else if (charA === '1' && charB === '0') {
               binNumber = '1';
               carry = '0'
            } else {
               binNumber = '0';
               carry = '1'
            }
         } else {
            if (charA === '0' && charB === '0') {
               binNumber = '1';
               carry = '0'
            } else if (charA === '0' && charB === '1') {
               binNumber = '0';
               carry = '1'
            } else if (charA === '1' && charB === '0') {
               binNumber = '0';
               carry = '1'
            } else {
               binNumber = '1';
               carry = '1'
            }
         }
         binSum += binNumber;
      }
      if (carry === '1') {
         binSum += '1'
      }
      return  binSum.split('').reverse().join('');
   };
}
const addBinary = new Solution().addBinary;


console.log(new Solution().addBinary('11', '1') === '100')
console.log(new Solution().addBinary('1010', '1011') === '10101')
console.log(new Solution().addBinary('11', '11') === '110')