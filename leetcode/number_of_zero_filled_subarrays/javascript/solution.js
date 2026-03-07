class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: math, iteration
    *     Arithmetic series.
    * @param {number[]} nums
    * @return {}
    */
   zeroFilledSubarray(nums) {
      nums.push(-1);
      let zeros = 0;
      let res = 0;

      for (const num of nums) {
         if (num === 0) {
            zeros++;
         } else {
            res += (1 + zeros) * zeros / 2;
            zeros = 0;
         }
      }

      nums.pop();
      return res
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: math, iteration
    * @param {number[]} nums
    * @return {}
    */
   zeroFilledSubarray(nums) {
      let zeros = 0;
      let res = 0;

      for (const num of nums) {
         num === 0 ? zeros += 1 : zeros = 0;
         res += zeros;
      }

      return res
   };
}


const zeroFilledSubarray = new Solution().zeroFilledSubarray;
console.log(new Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) === 6)
console.log(new Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]) === 9)
console.log(new Solution().zeroFilledSubarray([2, 10, 2019]) === 0)
