class Solution {
   /**
    * Time complexity: O(k2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: backtracking with pruning, sorting
    * @param {number[]} nums
    * @param {number} k
    * @return {boolean}
    */
   canPartitionKSubsets(nums, k) {
      const TOTAL = nums.reduce((sum, num) => sum + num, 0)
      if (TOTAL % k)
         return false
      const PART_SUM = TOTAL / k;
      nums.sort((a, b) => b - a);
      const partSize = Array(k).fill(0);

      const backtrack = (index) => {
         if (index === nums.length)
            return true

         const num = nums[index];

         for (let partIndex = 0; partIndex < k; partIndex++) {
            if (partSize[partIndex] + num <= PART_SUM) {
               partSize[partIndex] += num;
               if (backtrack(index + 1))
                  return true
               partSize[partIndex] -= num;
            }
            // pruning
            if (partSize[partIndex] === 0)
               break
         }
         return false
      }
      return backtrack(0)
   };
}


const canPartitionKSubsets = new Solution().canPartitionKSubsets;
console.log(new Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) === true)
console.log(new Solution().canPartitionKSubsets([1, 2, 3, 4], 3) === false)
console.log(new Solution().canPartitionKSubsets([3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10) === false)
console.log(new Solution().canPartitionKSubsets([4, 5, 9, 3, 10, 2, 10, 7, 10, 8, 5, 9, 4, 6, 4, 9], 5) === true)
console.log(new Solution().canPartitionKSubsets([10, 1, 10, 9, 6, 1, 9, 5, 9, 10, 7, 8, 5, 2, 10, 8], 11) === false)
