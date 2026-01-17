class Solution {
   /**
    * Time complexity: O(n*k)
    * Auxiliary space complexity: O(2^k)
    * Tags: hash set
    * @param {string} text
    * @param {number} k
    * @return {boolean}
    */
   hasAllCodes(text, k) {
      const seenCode = new Set();

      for (let index = 0; index < text.length - k + 1; index++) {
         seenCode.add(text.slice(index, index + k));
         if (seenCode.size === 2 ** k)
            return true
      }
      return false
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(2^k)
    * Tags: bit manipulation, sliding window
    * @param {string} text
    * @param {number} k
    * @return {boolean}
    */
   hasAllCodes(text, k) {
      if (k > text.length)
         return false

      const numbers = Array.from(text).map(value => Number(value));
      const seenCode = Array(2 ** k).fill(false);

      let left = 0;
      let number = 0;
      let power = 2 ** (k - 1);

      for (let index = 0; index < k - 1; index++) {
         number += numbers[index] * power;
         power = Math.floor(power / 2);
      }

      let found = 0;
      for (let right = k - 1; right < text.length; right++) {
         number += numbers[right];
         if (!seenCode[number]) {
            seenCode[number] = 1;
            found++;
            if (found === 2 ** k)
               return true
         }
         seenCode[number] = true;
         number %= 2 ** (k - 1);
         left += 1;
         number <<= 1;
      }

      // return seenCode.every(bool => bool);
      return false
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(2^k)
    * Tags: bit manipulation, sliding window
    * @param {string} text
    * @param {number} k
    * @return {boolean}
    */
   hasAllCodes(text, k) {
      if (k > text.length)
         return false

      const numbers = Array.from(text).map(value => Number(value));
      const seenCode = new Set();
      let left = 0;
      let number = 0;
      let power = 2 ** (k - 1);

      for (let index = 0; index < k - 1; index++) {
         number += numbers[index] * power;
         power = Math.floor(power / 2);
      }

      for (let right = k - 1; right < text.length; right++) {
         number += numbers[right];
         seenCode.add(number);
         if (seenCode.size === 2 ** k)
            return true
         number %= 2 ** (k - 1);
         left += 1;
         number <<= 1;
      }

      return false
   };
}


const hasAllCodes = new Solution().hasAllCodes;
console.log(new Solution().hasAllCodes('00110110', 2) === true)
console.log(new Solution().hasAllCodes('0110', 1) === true)
console.log(new Solution().hasAllCodes('0110', 2) === false)
console.log(new Solution().hasAllCodes('00110', 2) === true)
console.log(new Solution().hasAllCodes('0', 20) === false)