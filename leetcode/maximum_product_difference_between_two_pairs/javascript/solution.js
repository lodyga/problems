class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   maxProductDifference(nums) {
      const mins = [10 ** 5, 10 ** 5];
      const maxs = [0, 0];

      for (const num of nums) {
         if (num < mins[0]) {
            mins[1] = mins[0];
            mins[0] = num;
         }
         else if (num < mins[1])
            mins[1] = num;

         if (num > maxs[0]) {
            maxs[1] = maxs[0];
            maxs[0] = num;
         }
         else if (num > maxs[1])
            maxs[1] = num;
      }
      return maxs[0] * maxs[1] - mins[0] * mins[1]
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sorting, build-in function
    * @param {number[]} nums
    * @return {number}
    */
   maxProductDifference(nums) {
      nums.sort((a, b) => b - a);
      return nums[0] * nums[1] - nums[nums.length - 1] * nums[nums.length - 2]
   };
}


const maxProductDifference = new Solution().maxProductDifference;
console.log(new Solution().maxProductDifference([5, 6, 2, 7, 4]) === 34)
console.log(new Solution().maxProductDifference([4, 2, 5, 9, 7, 4, 8]) === 64)
