class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} num1
    * @param {number} num2
    * @return {num}
    */
   minimizeXor(num1, num2) {
      const countBits = (num) => {
         let setBits = 0;
         while (num) {
            setBits += num & 1;
            num >>= 1;
         }
         return setBits
      }

      let bitCount1 = countBits(num1);
      const bitCount2 = countBits(num2);
      let index = 0;

      // Remove least significant bits.
      while (bitCount1 > bitCount2) {
         if (num1 & (1 << index)) {
            num1 ^= (1 << index);
            bitCount1--;
         }
         index++;
      }

      // Add least significant bits.
      while (bitCount1 < bitCount2) {
         if ((num1 & (1 << index)) == 0) {
            num1 |= (1 << index);
            // num1 ^= (1 << index);
            bitCount1++;
         }
         index++;
      }

      return num1
   };
}


const minimizeXor = new Solution().minimizeXor;
console.log(new Solution().minimizeXor(3, 5) === 3)
console.log(new Solution().minimizeXor(1, 12) === 3)
console.log(new Solution().minimizeXor(65, 84) === 67)
