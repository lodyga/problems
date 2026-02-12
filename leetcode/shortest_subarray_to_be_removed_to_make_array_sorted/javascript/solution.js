class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {number[]} nums
    * @return {number}
    */
   findLengthOfShortestSubarray(nums) {
      // Find longest non-decreasing prefix.
      let left = 0;
      let right = nums.length - 1;
      
      while (
         left + 1 < nums.length &&
         nums[left] <= nums[left + 1]
      )
         left++;

      if (left === nums.length - 1)
         return 0

      // Find longest non-decreasing suffix.
      while (
         right - 1 > -1 &&
         nums[right - 1] <= nums[right]
      )
         right--;

      let res = Math.min(nums.length - 1 - left, right);

      // Try to merge prefix with suffix;
      let l = 0;
      let r = right;

      while (l <= left && r < nums.length) {
         if (nums[l] <= nums[r]) {
            res = Math.min(res, r - l - 1);
            l++;
         } else {
            r++
         }
      }

      return res
   };
}


const findLengthOfShortestSubarray = new Solution().findLengthOfShortestSubarray;
console.log(new Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]) === 3)
console.log(new Solution().findLengthOfShortestSubarray([5, 4, 3, 2, 1]) === 4)
console.log(new Solution().findLengthOfShortestSubarray([1, 2, 3]) === 0)
console.log(new Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 0, 7, 8, 9]) === 2)
