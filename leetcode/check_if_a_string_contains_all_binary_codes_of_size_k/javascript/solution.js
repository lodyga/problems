class Solution {
   /**
    * Time complexity: O(n*k)
    * Auxiliary space complexity: O(2^k)
    * Tags:
    *     DS: hash set
    * @param {string} text
    * @param {number} k
    * @return {boolean}
    */
   hasAllCodes(text, k) {
      const codeSet = new Set();

      for (let index = 0; index < text.length - k + 1; index++) {
         codeSet.add(text.slice(index, index + k));
         if (codeSet.size === 1 << k)
            return true
      }
      return false
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(2^k)
    * Tags:
    *     DS: hash set
    *     A: bit manipulation, Rabin-Karp, rolling hash
    * @param {string} text
    * @param {number} k
    * @return {boolean}
    */
   hasAllCodes(text, k) {
      const codeSet = new Set();
      let window = 0;
      let left = 0;

      for (let right = 0; right < text.length; right++) {
         window <<= 1;
         window += text[right] === '1' ? 1 : 0;

         if (right < k - 1) {
            continue
         }

         codeSet.add(window);

         if (codeSet.size === (1 << k)) {
            return true
         }

         const leftNum = text[left] === '1' ? 1 : 0;
         window -= leftNum << k - 1;
         left++;
      }

      return false
   };

   /**
    * Time complexity: O(n*k)
    * Auxiliary space complexity: O(2^k)
    * Tags:
    *     DS: array
    *     A: bit manipulation, Rabin-Karp, rolling hash
    * @param {string} text
    * @param {number} k
    * @return {boolean}
    */
   hasAllCodes(text, k) {
      const codes = Array(1 << k).fill(false);
      let codeCounter = 0
      let window = 0;
      let left = 0;

      for (let right = 0; right < text.length; right++) {
         window <<= 1;
         window += text[right] === '1' ? 1 : 0;

         if (right < k - 1) {
            continue
         }

         if (codes[window] === false) {
            codes[window] = true;
            codeCounter++;
            if (codeCounter === 1 << k) {
               return true
            }
         }

         const leftNum = text[left] === '1' ? 1 : 0;
         window -= leftNum << k - 1;
         left++;
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
console.log(new Solution().hasAllCodes('000011010111011001001111111001000100100100010100101100001101101101110001100100101111100111001001111001001010111010010101101001001110011100110101001001001000000110101001010011101100110110100010000', 7) === false)
