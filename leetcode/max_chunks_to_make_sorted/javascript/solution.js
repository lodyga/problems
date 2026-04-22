class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} nums
    * @return {number}
    */
   maxChunksToSorted(nums) {
      let maxNum = 0;
      let counter = 0;

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         maxNum = Math.max(maxNum, num);

         if (maxNum === index) {
            counter += 1;
         }
      }

      return counter
   };
}


const maxChunksToSorted = new Solution().maxChunksToSorted;
console.log(new Solution().maxChunksToSorted([4, 3, 2, 1, 0]) === 1)
console.log(new Solution().maxChunksToSorted([1, 0, 2, 3, 4]) === 4)
console.log(new Solution().maxChunksToSorted([0]) === 1)
