class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number[]} nums
    * @return {number}
    */
   missingNumber(nums) {
      let res = 0;

      for (let num = 0; num < nums.length + 1; num++) {
         res ^= num;
      }
      for (const num of nums) {
         res ^= num;
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   missingNumber(nums) {
      const numSet = new Set(nums);
    
      for (let num = 0; num <= nums.length; num++) {
         if (!numSet.has(num)) {
            return num;
         }
      }
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: math
    * @param {number[]} nums
    * @return {number}
    */
   missingNumber(nums) {
      const rangeSum = nums.length * (nums.length + 1) / 2;
      const numSum = nums.reduce((sum, num) => sum + num);
      return rangeSum - numSum;
   }
}


const missingNumber = new Solution().missingNumber;
console.log(new Solution().missingNumber([3, 0, 1]) === 2)
console.log(new Solution().missingNumber([0, 1]) === 2)
console.log(new Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) === 8)
