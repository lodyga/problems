class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {bits}
    * @return {boolean}
    */
   isOneBitCharacter(bits) {
      let index = 0
      let oneBit = false;
      while (index < bits.length) {
         const bit = bits[index];
         if (bit) {
            index += 2;
            oneBit = false;
         }
         else {
            index++;
            oneBit = true;
         }
      }
      return oneBit
   };
}


const isOneBitCharacter = new Solution().isOneBitCharacter;
console.log(new Solution().isOneBitCharacter([1, 0, 0]) === true)
console.log(new Solution().isOneBitCharacter([1, 1, 1, 0]) === false)
console.log(new Solution().isOneBitCharacter([0, 0]) === true)
