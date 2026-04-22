class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} nums
    * @return {number}
    */
   rob(nums) {
      if (nums.length <= 3) {
         return Math.max(...nums)
      }

      const oneRob = (nums) => {
         const cache = [0, 0];

         for (let index = nums.length - 1; index > -1; index--) {
            const num = nums[index];
            const skipHouse = cache[0];
            const robHouse = num + cache[1];
            [cache[0], cache[1]] = [Math.max(skipHouse, robHouse), cache[0]];
         }

         return cache[0]
      };

      return Math.max(
         oneRob(nums.slice(0, -1)),
         oneRob(nums.slice(1,))
      )
   };
}


const rob = new Solution().rob;
console.log(new Solution().rob([2, 3, 2]) === 3)
console.log(new Solution().rob([1, 2, 3, 1]) === 4)
console.log(new Solution().rob([1, 2, 3]) === 3)
console.log(new Solution().rob([1]) === 1)
console.log(new Solution().rob([0, 0]) === 0)
console.log(new Solution().rob([1, 3, 1, 3, 100]) === 103)
