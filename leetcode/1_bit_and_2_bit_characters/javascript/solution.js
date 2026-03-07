class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {bits}
    * @return {boolean}
    */
   isOneBitCharacter(bits) {
      let index = 0
      let isOneBit = false;

      while (index < bits.length) {
         if (bits[index]) {
            isOneBit = false;
            index += 2;
         }
         else {
            isOneBit = true;
            index++;
         }
      }

      return isOneBit
   };
}


const isOneBitCharacter = new Solution().isOneBitCharacter;
console.log(new Solution().isOneBitCharacter([1, 0, 0]) === true)
console.log(new Solution().isOneBitCharacter([1, 1, 1, 0]) === false)
console.log(new Solution().isOneBitCharacter([0, 0]) === true)
