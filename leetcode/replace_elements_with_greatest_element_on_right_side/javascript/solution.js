class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {number[]} nums
    * @return {number[]}
    */
   replaceElements(nums) {
      let prev = -1;
      const res = [];

      for (let idx = nums.length - 1; idx > -1; idx--) {
         res.push(prev);
         prev = Math.max(prev, nums[idx]);
      }

      return res.reverse()
   }
}


const replaceElements = new Solution().replaceElements;
console.log(JSON.stringify(new Solution().replaceElements([17, 18, 5, 4, 6, 1])) === JSON.stringify([18, 6, 6, 6, 1, -1]))
console.log(JSON.stringify(new Solution().replaceElements([400])) === JSON.stringify([-1]))
