class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number[]} nums
    * @return {}
    */
   zeroFilledSubarray(nums) {
      let left = 0;
      let counter = 0;
      nums.push(-1);

      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];
         if (num !== 0) {
            counter += (1 + (right - left)) * (right - left) / 2;
            left = right + 1;
         }
      }
      return counter
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number[]} nums
    * @return {}
    */
   zeroFilledSubarray(nums) {
      let zeros = 0;
      let counter = 0;

      for (const num of nums) {
         num === 0 ? zeros += 1 : zeros = 0;
         counter += zeros;
      }
      return counter
   };
}


const zeroFilledSubarray = new Solution().zeroFilledSubarray;
console.log(new Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) === 6)
console.log(new Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]) === 9)
console.log(new Solution().zeroFilledSubarray([2, 10, 2019]) === 0)
