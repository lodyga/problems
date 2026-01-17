class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sliding window, sorting
    * @param {number[]} nums
    * @return {number}
    */
   minOperations(nums) {
      const uniqSortNums = [...new Set(nums)].sort((a, b) => a - b);
      let maxWindow = 0;
      let right = 0;

      for (let left = 0; left < uniqSortNums.length; left++) {
         const num = uniqSortNums[left];
         while (
            right < uniqSortNums.length &&
            num + nums.length - 1 >= uniqSortNums[right]
         ) {
            right++;
         }
         const window = right - left;
         maxWindow = Math.max(maxWindow, window);
      }
      return nums.length - maxWindow
   };
}


const minOperations = new Solution().minOperations;
console.log(new Solution().minOperations([2, 3, 5, 9]) === 1)
console.log(new Solution().minOperations([4, 2, 5, 3]) === 0)
console.log(new Solution().minOperations([1, 2, 3, 5, 6]) === 1)
console.log(new Solution().minOperations([1, 10, 100, 1000]) === 3)
console.log(new Solution().minOperations([1, 9, 10, 11, 19]) === 2)
console.log(new Solution().minOperations([1, 3, 5, 7, 9]) === 2)
console.log(new Solution().minOperations([8, 5, 9, 9, 8, 4]) === 2)
console.log(new Solution().minOperations([8, 10, 16, 18, 10, 10, 16, 13, 13, 16]) === 6)
