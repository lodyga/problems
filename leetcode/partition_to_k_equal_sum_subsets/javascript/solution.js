class Solution {
   /**
    * Time complexity: O(k^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: backtracking with pruning, sorting
    * @param {number[]} nums
    * @param {number} k
    * @return {boolean}
    */
   canPartitionKSubsets(nums, k) {
      const N = nums.length;
      const TOTAL = nums.reduce((sum, num) => sum + num, 0)
      if (TOTAL % k) {
         return false;
      }
      const UPPER_BOUND = TOTAL / k;
      nums.sort((a, b) => b - a);
      const subsetSum = Array(k).fill(0);

      const backtrack = (idx) => {
         if (idx === N) {
            return true;
         }

         const num = nums[idx];

         for (let partIdx = 0; partIdx < k; partIdx++) {
            if (subsetSum[partIdx] + num <= UPPER_BOUND) {
               subsetSum[partIdx] += num;
               if (backtrack(idx + 1)) {
                  return true;
               }
               subsetSum[partIdx] -= num;
            }
            // pruning
            if (subsetSum[partIdx] === 0) {
               break;
            }
         }

         return false;
      }

      return backtrack(0);
   };
}


const canPartitionKSubsets = new Solution().canPartitionKSubsets;
console.log(new Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) === true)
console.log(new Solution().canPartitionKSubsets([1, 2, 3, 4], 3) === false)
console.log(new Solution().canPartitionKSubsets([3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10) === false)
console.log(new Solution().canPartitionKSubsets([4, 5, 9, 3, 10, 2, 10, 7, 10, 8, 5, 9, 4, 6, 4, 9], 5) === true)
console.log(new Solution().canPartitionKSubsets([10, 1, 10, 9, 6, 1, 9, 5, 9, 10, 7, 8, 5, 2, 10, 8], 11) === false)
