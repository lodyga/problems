class Solution {
   /**
    * Time complexity: O(1)
         O(32)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number} num
    * @return {number}
    */
   hammingWeight(num) {
      let setBitCounter = 0;

      while (num) {
         setBitCounter += num % 2;
         num = num >> 1;
      }

      return setBitCounter
   };

   /**
    * Time complexity: O(1)
         O(32)
    * Auxiliary space complexity: O(n)
    * Tags: bit manipulation
    * @param {number} num
    * @return {number}
    */
   hammingWeight(num) {
      return (
         num
            .toString(2)
            .split('')
            .filter(digit => digit === '1')
            .length
      )
   };

   /**
    * Time complexity: O(1)
         O(32)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number} num
    * @return {number}
    */
   hammingWeight(num) {
      let setBitCounter = 0;

      while (num) {
         setBitCounter += num & 1;
         num = num >> 1;
      }
      return setBitCounter
   };
}


const hammingWeight = new Solution().hammingWeight;
console.log(new Solution().hammingWeight(0) === 0)
console.log(new Solution().hammingWeight(1) === 1)
console.log(new Solution().hammingWeight(2) === 1)
console.log(new Solution().hammingWeight(3) === 2)
console.log(new Solution().hammingWeight(4) === 1)
console.log(new Solution().hammingWeight(11) === 3)
console.log(new Solution().hammingWeight(128) === 1)
console.log(new Solution().hammingWeight(2147483645) === 30)
