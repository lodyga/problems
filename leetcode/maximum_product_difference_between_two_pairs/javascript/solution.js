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
      let [a, b] = [nums[0], nums[1]];

      if (a > b) {
         [a, b] = [b, a];
      }

      let [min1, min2] = [a, b];
      let [max1, max2] = [b, a];

      for (let idx = 2; idx < nums.length; idx++) {
         const num = nums[idx];

         if (num < min1) {
            min2 = min1;
            min1 = num;
         } 
         else if (num < min2) {
            min2 = num;
         }

         if (num > max1) {
            max2 = max1;
            max1 = num;
         }
         else if (num > max2) {
            max2 = num;
         }
      }

      return max1 * max2 - min1 * min2;
   }
}


class Solution {
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
      return nums[0] * nums[1] - nums[nums.length - 1] * nums[nums.length - 2];
   }
}


const maxProductDifference = Solution().maxProductDifference;
console.log(new Solution().maxProductDifference([5, 6, 2, 7, 4]) === 34)
console.log(new Solution().maxProductDifference([4, 2, 5, 9, 7, 4, 8]) === 64)
console.log(new Solution().maxProductDifference([1, 6, 7, 5, 2, 4, 10, 6, 4]) === 68)
console.log(new Solution().maxProductDifference([7, 3, 6, 2, 5]) === 36)
