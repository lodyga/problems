class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number} number
    * @return {number[]}
    */
   countBits(number) {
      const bitsArray = Array(number + 1).fill(0);

      for (let index = 1; index <= number; index++) {
         bitsArray[index] = countSetBits(index);
      }

      return bitsArray

      function countSetBits(number) {
         let setBitCounter = 0;

         while (number) {
            setBitCounter += number & 1;
            number = number >> 1;
         }
         return setBitCounter
      }
   };
}
const countBits = new Solution().countBits;


console.log(new Solution().countBits(2), [0, 1, 1])
console.log(new Solution().countBits(5), [0, 1, 1, 2, 1, 2])