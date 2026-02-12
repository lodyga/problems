class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: hash map
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   maximumSubarraySum(nums, k) {
      const windowNumFreq = new Map();
      let windowSum = 0;
      let left = 0
      let res = 0;

      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];
         windowNumFreq.set(num, (windowNumFreq.get(num) || 0) + 1);
         windowSum += num;

         if (right < k - 1)
            continue

         if (windowNumFreq.size === k)
            res = Math.max(res, windowSum);

         const leftNum = nums[left];
         windowSum -= leftNum;
         windowNumFreq.set(leftNum, windowNumFreq.get(leftNum) - 1);
         if (windowNumFreq.get(leftNum) === 0)
            windowNumFreq.delete(leftNum)
         left += 1;
      }
      return res
   }
}


const maximumSubarraySum = new Solution().maximumSubarraySum;
console.log(new Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) === 15)
console.log(new Solution().maximumSubarraySum([4, 4, 4], 3) === 0)
console.log(new Solution().maximumSubarraySum([9, 9, 9, 1, 2, 3], 3) === 12)
console.log(new Solution().maximumSubarraySum([1, 5, 4, 2, 4, 1, 3], 4) === 12)
