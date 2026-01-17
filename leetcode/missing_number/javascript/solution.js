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
      let xor = 0;

      for (let number = 0; number <= nums.length; number++) {
         xor ^= number;
      }
      for (const number of nums) {
         xor ^= number
      }
      return xor
   };

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
            return num
         }
      }
   };
   
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: math
    * @param {number[]} nums
    * @return {number}
    */
   amissingNumber(nums) {
      const total = nums.length * (nums.length + 1) / 2
      const numSum = nums.reduce((sum, num) => sum + num);
      return total - numSum
   };
}


const missingNumber = new Solution().missingNumber;
console.log(new Solution().missingNumber([3, 0, 1]) === 2)
console.log(new Solution().missingNumber([0, 1]) === 2)
console.log(new Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) === 8)
