class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: prefix sum
    * @param {number[]} nums
    * @return {number}
    */
   findMaxLength(nums) {
      // Ones over zeros surplus counter.
      let onesSurp = 0;
      let res = 0;
      // Ones over zeros surplus: index of first occurence.
      const prefixIndex = new Map();

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         onesSurp += num ? 1 : -1;

         if (!prefixIndex.has(onesSurp))
            prefixIndex.set(onesSurp, index);

         if (onesSurp === 0) {
            res = Math.max(res, index + 1)
         } else if (prefixIndex.has(onesSurp)) {
            res = Math.max(res, index - prefixIndex.get(onesSurp))
         }
      }

      return res
   };
}


const findMaxLength = new Solution().findMaxLength;
console.log(new Solution().findMaxLength([0, 1]) === 2)
console.log(new Solution().findMaxLength([0, 1, 0]) === 2)
console.log(new Solution().findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]) === 6)
console.log(new Solution().findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0, 0]) === 10)
console.log(new Solution().findMaxLength([0, 1, 1]) === 2)
console.log(new Solution().findMaxLength([1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]) === 94)
console.log(new Solution().findMaxLength([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]) === 94)
