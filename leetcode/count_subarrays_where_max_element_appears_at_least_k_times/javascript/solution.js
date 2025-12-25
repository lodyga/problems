class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *    A: sliding window
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   countSubarrays(nums, k) {
      let window = 0;
      let left = 0;
      let maxNum = Math.max(...nums);
      let counter = 0;

      for (const number of nums) {
         if (number === maxNum) {
            window++;
         }
         while (window === k) {
            if (nums[left] === maxNum) {
               window--;
            }
            left++;
         }
         counter += left;
      }
      return counter
   };
}


const countSubarrays = new Solution().countSubarrays;
console.log(new Solution().countSubarrays([1, 3, 2, 3, 3], 2) === 6)
console.log(new Solution().countSubarrays([1, 3, 2, 3, 3, 1], 2) === 10)
console.log(new Solution().countSubarrays([1, 3, 2, 3, 1], 2) === 4)
console.log(new Solution().countSubarrays([1, 3, 2, 3, 1, 1], 2) === 6)
console.log(new Solution().countSubarrays([1, 3, 2, 3, 1, 1, 3], 2) === 10)
console.log(new Solution().countSubarrays([1, 4, 2, 1], 3) === 0)
console.log(new Solution().countSubarrays([3, 2, 3, 4, 4], 2) === 4)
console.log(new Solution().countSubarrays([37, 20, 38, 66, 34, 38, 9, 41, 1, 14, 25, 63, 8, 12, 66, 66, 60, 12, 35, 27, 16, 38, 12, 66, 38, 36, 59, 54, 66, 54, 66, 48, 59, 66, 34, 11, 50, 66, 42, 51, 53, 66, 31, 24, 66, 44, 66, 1, 66, 66, 29, 54], 5) === 594)
