class Solution {
   /**
    * Time complexity: O(1)
    *     O(32)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} n
    * @return {number}
    */
   reverseBits(n) {
      const mask = Array(32).fill('0');
      let idx = 0;

      for (const char of n.toString(2).split('').reverse().join('')) {
         mask[idx] = char;
         idx++;
      }

      return parseInt(mask.join(''), 2);
   }
}


class Solution {
   /**
    * Time complexity: O(1)
    *     O(32)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} n
    * @return {number}
    */
   reverseBits(n) {
      let res = 0;

      for (let idx = 0; idx < 32; idx++) {
         const bit = (n >> idx) & 1;
         
         if (bit) {
            res += bit << (31 - idx);
         }
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(1)
    *     O(32)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} n
    * @return {number}
    */
   reverseBits(n) {
      let res = 0;

      for (let idx = 0; idx < 32; idx++) {
         res = (res << 1) | (n & 1);
         n >>= 1;
      }

      return res;
   }
}


const reverseBits = new Solution().reverseBits;
console.log(new Solution().reverseBits(43261596) === 964176192)
console.log(new Solution().reverseBits(2147483644) === 1073741822)
