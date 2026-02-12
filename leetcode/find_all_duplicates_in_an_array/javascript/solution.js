class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: in-place, negative marking
    * @param {number[]}nums
    * @return {number}
    */
   findDuplicates(nums) {
      const res = [];

      for (const num of nums) {
         const index = Math.abs(num) - 1;

         if (nums[index] < 0) {
            res.push(Math.abs(num));
         } else {
            nums[index] *= -1;
         }
      }

      return res
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: in-place, upper bound marking
    * @param {number[]}nums
    * @return {number}
    */
   findDuplicates(nums) {
      const UPPER_BOUND = nums.length + 1;
      const res = [];

      for (const num of nums) {
         const index = (num % UPPER_BOUND) - 1;

         if (nums[index] > UPPER_BOUND) {
            res.push(num % UPPER_BOUND);
         } else {
            nums[index] += UPPER_BOUND;
         }
      }

      return res
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    * @param {number[]}nums
    * @return {number}
    */
   findDuplicates(nums) {
      const res = [];
      const numSet = new Set();

      for (const num of nums) {
         if (numSet.has(num)) {
            res.push(num);
         } else {
            numSet.add(num);
         }
      }

      return res
   };
}


const findDuplicates = new Solution().findDuplicates;
console.log(new Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]).sort().toString() === [2, 3].sort().toString())
console.log(new Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]).sort().toString() === [2, 3].sort().toString())
console.log(new Solution().findDuplicates([1, 1, 2]).sort().toString() === [1].sort().toString())
console.log(new Solution().findDuplicates([1]).sort().toString() === [].sort().toString())
console.log(new Solution().findDuplicates([10, 2, 5, 10, 9, 1, 1, 4, 3, 7]).sort().toString() === [10, 1].sort().toString())
