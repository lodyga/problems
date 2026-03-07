class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   numberOfSubarrays(nums, k) {
      let left = 0;
      let mid = 0;
      let oddCounter = 0;
      let res = 0;

      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];

         if (num % 2) {
            oddCounter++;
            if (oddCounter === 1) mid = right

            if (oddCounter > k) {
               left = mid + 1;
               mid = left;
               while (nums[mid] % 2 === 0) mid++;
            }
         }

         if (oddCounter < k) continue
         res += (mid - left + 1);
      }

      return res
   };
}


const numberOfSubarrays = new Solution().numberOfSubarrays;
console.log(new Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3) === 2)
console.log(new Solution().numberOfSubarrays([2, 4, 6], 1) === 0)
console.log(new Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) === 16)
console.log(new Solution().numberOfSubarrays([1, 1, 1, 1, 1], 1) === 5)
console.log(new Solution().numberOfSubarrays([91473, 45388, 24720, 35841, 29648, 77363, 86290, 58032, 53752, 87188, 34428, 85343, 19801, 73201], 4) === 6)
