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
      let idx1 = a.length - 1;
      let idx2 = b.length - 1;
      let carry = false;
      const res = [];

      while (idx1 > -1 || idx2 > -1 || carry) {
         const char1 = idx1 > -1 ? a[idx1] : '0';
         const char2 = idx2 > -1 ? b[idx2] : '0';

         if (char1 === char2) {
            res.push(carry ? '1' : '0');
            carry = char1 === '1';
         } 
         else {
            res.push(carry ? '0': '1');
         }
         
         idx1--;
         idx2--;
      }

      return res.reverse().join('');
   }
}


const addBinary = new Solution().addBinary;
console.log(new Solution().addBinary('11', '1') === '100')
console.log(new Solution().addBinary('1010', '1011') === '10101')
console.log(new Solution().addBinary('11', '11') === '110')
