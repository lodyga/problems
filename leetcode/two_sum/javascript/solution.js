class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * @param {number[]} nums
    * @param {number} target
    * @return {number[]}
    */
   twoSum(nums, target) {
      const numIdx = new Map();

      for (let idx = 0; idx < nums.length; idx++) {
         const num = nums[idx];
         const diff = target - num;

         if (numIdx.has(diff)) {
            return [numIdx.get(diff), idx]
         } else {
            numIdx.set(num, idx);
         }
      }
   }

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: Plain Object
    * @param {number[]} nums
    * @param {number} target
    * @return {number[]}
   */
   twoSum(nums, target) {
      const numIdx = {};
      
      for (let idx = 0; idx < nums.length; idx++) {
         let num = nums[idx];
         let diff = target - num;
      
         if (diff in numIdx) {
            return [numIdx[diff], idx];
         } else {
            numIdx[num] = idx;
         }
      }
      return null
   }
};


const twoSum = new Solution().twoSum;
console.log(new Solution().twoSum([2, 7, 11, 15], 9).toString() === [0, 1].toString())
console.log(new Solution().twoSum([3, 2, 4], 6).toString() === [1, 2].toString())
console.log(new Solution().twoSum([3, 3], 6).toString() === [0, 1].toString())
