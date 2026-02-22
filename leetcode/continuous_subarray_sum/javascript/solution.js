class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: prefix sum, brute-force
    * @param {number[]} nums
    * @param {number} k
    * @return {boolean}
    */
   checkSubarraySum(nums, k) {
      const prefix = [0];

      for (const num of nums) {
         prefix.push(prefix[prefix.length - 1] + num);
      }

      for (let right = 2; right < prefix.length; right++) {
         const numR = prefix[right];

         for (let left = 0; left < right - 1; left++) {
            const numL = prefix[left];

            if ((numR - numL) % k === 0) {
               return true
            }
         }
      }

      return false
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, list
    *     A: prefix sum
    * @param {number[]} nums
    * @param {number} k
    * @return {boolean}
    */
   checkSubarraySum(nums, k) {
      const prefix = [0];
      const diffIndex = new Map([[0, 0]]);

      //for index, num in enumerate(nums, 1):
      for (let index = 1; index <= nums.length; index++) {
         const num = nums[index - 1];
         prefix.push((prefix[prefix.length - 1] + num) % k);
         const diff = prefix[prefix.length - 1];

         if (!diffIndex.has(diff)) {
            diffIndex.set(diff, index);
         } else if (index - diffIndex.get(diff) >= 2) {
            return true
         }
      }

      return false
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash map, list
    *     A: prefix sum
    * @param {number[]} nums
    * @param {number} k
    * @return {boolean}
    */
   checkSubarraySum(nums, k) {
      let diff = 0;
      const diffIndex = new Map([[0, 0]]);

      //for index, num in enumerate(nums, 1):
      for (let index = 1; index <= nums.length; index++) {
         const num = nums[index - 1];
         diff = (diff + num) % k;

         if (!diffIndex.has(diff)) {
            diffIndex.set(diff, index);
         } else if (index - diffIndex.get(diff) >= 2) {
            return true
         }
      }

      return false
   };
}


const checkSubarraySum = new Solution().checkSubarraySum;
console.log(new Solution().checkSubarraySum([23, 2, 6, 4, 7], 6) === true)
console.log(new Solution().checkSubarraySum([23, 2, 6, 4, 7], 13) === false)
console.log(new Solution().checkSubarraySum([0], 1) === false)
console.log(new Solution().checkSubarraySum([23, 2, 4, 6, 6], 7) === true)
console.log(new Solution().checkSubarraySum([24], 6) === false)
