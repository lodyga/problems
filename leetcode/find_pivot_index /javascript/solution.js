class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    DS: prefix sum
    * @param {number[]} nums
    * @return {number}
    */
   pivotIndex(nums) {
      let suffixSum = nums.reduce((sum, num) => sum + num, 0);
      let prefixSum = 0;

      for (let idx = 0; idx < nums.length; idx++) {
         const num = nums[idx];
         suffixSum -= num;
         
         if (prefixSum === suffixSum) {
            return idx
         }

         prefixSum += num;
      }

      return -1;
   }
}


const pivotIndex = new Solution().pivotIndex;
console.log(new Solution().pivotIndex([1, 7, 3, 6, 5, 6]) === 3)
console.log(new Solution().pivotIndex([1, 2, 3]) === -1)
console.log(new Solution().pivotIndex([2, 1, -1]) === 0)
