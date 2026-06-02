class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} goal
    * @return {number}
    */
   numSubarraysWithSum(nums, goal) {
      let left = 0;
      let mid = 0;
      let res = 0;

      for (let right = 0; right < nums.length; right++) {
         goal -= nums[right];

         while (
            mid < right &&
            goal < 0
         ) {
            goal += nums[mid];
            mid++;
            left = mid;
         }

         while (
            mid < right &&
            nums[mid] === 0
         ) mid++;

         if (goal === 0) {
            res += (mid - left + 1);
         }
      }

      return res;
   }
}


const numSubarraysWithSum = new Solution().numSubarraysWithSum;
console.log(new Solution().numSubarraysWithSum([0, 1, 1, 0], 2) === 4)
console.log(new Solution().numSubarraysWithSum([0, 1, 1, 0, 1], 2) === 5)
console.log(new Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2) === 4)
console.log(new Solution().numSubarraysWithSum([0, 0, 1], 0) === 3)
console.log(new Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0) === 15)
console.log(new Solution().numSubarraysWithSum([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 0) === 27)
console.log(new Solution().numSubarraysWithSum([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 0) === 67)
