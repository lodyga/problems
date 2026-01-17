class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: prefix sum
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   subarraySum(nums, target) {
      let counter = 0;
      let prefix = 0;
      const prefixFreq = new Map([[0, 1]]);

      for (const num of nums) {
         prefix += num;
         if (prefixFreq.has(prefix - target)) {
            counter += prefixFreq.get(prefix - target);
         }
         prefixFreq.set(prefix, (prefixFreq.get(prefix) || 0) + 1);
      }
      return counter
   };
}


const subarraySum = new Solution().subarraySum;
console.log(new Solution().subarraySum([1, 1, 1], 2) === 2)
console.log(new Solution().subarraySum([1, 2, 3], 3) === 2)
console.log(new Solution().subarraySum([1], 0) === 0)
console.log(new Solution().subarraySum([-1, -1, 1], 0) === 1)
console.log(new Solution().subarraySum([1, -1, 1, 1, 1], 2) === 4)
