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
      let prev = nums[0];
      // 1: increasing, 0: decreating, -1: donno
      let isIncreasing = -1;
      let size = 1;
      let maxSize = 1;

      for (const num of nums) {
         if (
            prev < num &&
            isIncreasing !== 1
         ) {
            size++
            isIncreasing = 1;
         } else if (
            prev > num &&
            isIncreasing !== 0
         ) {
            size++;
            isIncreasing = 0;
         } else {
            if (prev < num) {
               size = 2;
               isIncreasing = 1;
            } else if (prev > num) {
               size = 2;
               isIncreasing = 0;
            } else {
               size = 1;
               isIncreasing = -1;
            }
         }
         prev = num;
         maxSize = Math.max(maxSize, size);
      }
      return maxSize
   };
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
