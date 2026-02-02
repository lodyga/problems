class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   longestMonotonicSubarray(nums) {
      let prevNum = nums[0];
      let incLen = 1;
      let decLen = 1;
      let maxMonotLen = 1;

      for (let index = 1; index < nums.length; index++) {
         const num = nums[index];

         if (prevNum < num) {
            incLen++;
            maxMonotLen = Math.max(maxMonotLen, incLen);
            decLen = 1;
         } else if (prevNum > num) {
            decLen++;
            maxMonotLen = Math.max(maxMonotLen, decLen);
            incLen = 1;
         } else {
            incLen = 1;
            decLen = 1;
         }
         prevNum = num;
      }
      return maxMonotLen
   };
}


const longestMonotonicSubarray = new Solution().longestMonotonicSubarray;
console.log(new Solution().longestMonotonicSubarray([1, 4, 3, 3, 2]) === 2)
console.log(new Solution().longestMonotonicSubarray([3, 3, 3, 3]) === 1)
console.log(new Solution().longestMonotonicSubarray([3, 2, 1]) === 3)
console.log(new Solution().longestMonotonicSubarray([3]) === 1)
