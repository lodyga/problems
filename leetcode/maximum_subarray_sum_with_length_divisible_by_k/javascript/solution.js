class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: prefix sum
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   maxSubarraySum(nums, k) {
      let prefix = 0;
      let subSum = nums.slice(0, k).reduce((sum, num) => sum + num, 0);
      // min prefix for every rest: mod = index % k
      const minPrefix = Array(k).fill(Infinity);
      minPrefix[0] = 0;

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         prefix += num;
         const mod = (index + 1) % k;

         if (minPrefix[mod] !== Infinity) {
            subSum = Math.max(subSum, prefix - minPrefix[mod])
         }

         minPrefix[mod] = Math.min(minPrefix[mod], prefix);
      }

      return subSum
   };
}


const maxSubarraySum = new Solution().maxSubarraySum;
console.log(new Solution().maxSubarraySum([1, 2], 1) === 3)
console.log(new Solution().maxSubarraySum([-1, -2, -3, -4, -5], 4) === -10)
console.log(new Solution().maxSubarraySum([-5, 1, 2, -3, 4], 2) === 4)
console.log(new Solution().maxSubarraySum([9, -11, 15], 2) === 4)
console.log(new Solution().maxSubarraySum([-9653, -7948, -5449, -297, -2536, -2633, -6354, -4335, -5103, -908, -668, -4369, -6986, -328, -3672, -4463, -5360, -5949, -4787, -8946, -7049, -565, -6527, -1386, -1873], 22) === -85094)
