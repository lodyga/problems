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
         num = Math.abs(num);
         nums[num - 1] = -Math.abs(nums[num - 1]);
      }
      // return nums
      //    .map((value, index) => [value, index])
      //    .filter(([value, _]) => value > 0)
      //    .map(([_, index]) => index + 1)
      const res = [];
      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         if (num > 0)
            res.push(index + 1);
      }
      return res
   };
}


const findDisappearedNumbers = new Solution().findDisappearedNumbers;
console.log(JSON.stringify(new Solution().findDisappearedNumbers([1, 1])) === JSON.stringify([2]))
console.log(JSON.stringify(new Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])) === JSON.stringify([5, 6]))
