class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   findMaxConsecutiveOnes(nums) {
      let counter = 0;
      let maxCounter = 0;

      for (const number of nums) {
         if (number) {
            counter++;
            maxCounter = Math.max(maxCounter, counter);
         } else {
            counter = 0;
         }
      }
      return maxCounter
   };
}


const findMaxConsecutiveOnes = new Solution().findMaxConsecutiveOnes;
console.log(new Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) === 3)
console.log(new Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) === 2)
console.log(new Solution().findMaxConsecutiveOnes([1]) === 1)
console.log(new Solution().findMaxConsecutiveOnes([0]) === 0)
