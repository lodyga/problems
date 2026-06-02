class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: negative marking, in-place method
    * @param {number[]} nums
    * @return {number[]}
    */
   findDisappearedNumbers(nums) {
      for (let num of nums) {
         const idx = Math.abs(num) - 1;
         nums[idx] = -Math.abs(nums[idx]);
      }
      // return nums
      //    .map((val, idx) => [val, idx])
      //    .filter(([val, _]) => val > 0)
      //    .map(([_, idx]) => idx + 1)

      const res = [];
      for (let idx = 0; idx < nums.length; idx++) {
         const num = nums[idx];

         if (num > 0) {
            res.push(idx + 1);
         }
      }

      return res;
   }
}


const findDisappearedNumbers = new Solution().findDisappearedNumbers;
console.log(JSON.stringify(new Solution().findDisappearedNumbers([1, 1])) === JSON.stringify([2]))
console.log(JSON.stringify(new Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])) === JSON.stringify([5, 6]))
