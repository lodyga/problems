class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} nums
    * @return {number}
    */
   maxTurbulenceSize(nums) {
      let prevNum = nums[0];
      let subSize = 1;
      let res = 1;
      // increasing: 1, decreasing: 0: donno: -1
      let isIncreasing = -1;

      for (const num of nums) {
         if (num === prevNum) {
            isIncreasing = -1;
            subSize = 1;
         }
         else if (prevNum > num && isIncreasing !== 1) {
            subSize++;
            isIncreasing = 1;
            res = Math.max(res, subSize);
         }
         else if (prevNum < num && isIncreasing !== 0) {
            subSize++;
            isIncreasing = 0;
            res = Math.max(res, subSize);
         }
         // New monotonic pair.
         else {
            subSize = 2;
         }

         prevNum = num;
      }

      return res;
   }
}


const maxTurbulenceSize = new Solution().maxTurbulenceSize;
console.log(new Solution().maxTurbulenceSize([3, 8, 4]) === 3)
console.log(new Solution().maxTurbulenceSize([8, 3, 9]) === 3)
console.log(new Solution().maxTurbulenceSize([1, 3, 8, 4]) === 3)
console.log(new Solution().maxTurbulenceSize([9, 8, 3, 9]) === 3)
console.log(new Solution().maxTurbulenceSize([3, 3]) === 1)
console.log(new Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) === 5)
console.log(new Solution().maxTurbulenceSize([4, 8, 12, 16]) === 2)
console.log(new Solution().maxTurbulenceSize([100]) === 1)
