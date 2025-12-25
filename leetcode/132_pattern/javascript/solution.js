class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic decreasing stack
    *     A: iteration
    * @param {number[]} nums
    * @return {boolean}
    */
   find132pattern(nums) {
      const stack = [];
      let prevMin = nums[0];

      for (const num of nums) {
         while (
            stack.length && 
            stack[stack.length - 1][0] <= num
         ) stack.pop();

         if (
            stack.length && 
            stack[stack.length - 1][1] < num
         ) return true

         stack.push([num, prevMin]);
         prevMin = Math.min(prevMin, num);
      }
      return false
   };
}


const find132pattern = new Solution().find132pattern;
console.log(new Solution().find132pattern([3, 1, 4, 2]) === true)
console.log(new Solution().find132pattern([1, 2, 3, 4]) === false)
console.log(new Solution().find132pattern([-1, 3, 2, 0]) === true)
console.log(new Solution().find132pattern([3, 5, 0, 3, 4]) === true)
console.log(new Solution().find132pattern([1, 0, 1, -4, -3]) === false)
console.log(new Solution().find132pattern([-2, 1, 2, -2, 1, 2]) === true)
console.log(new Solution().find132pattern([1, 2, 3, 4, -4, -3, -5, -1]) === false)
console.log(new Solution().find132pattern([1, 3, -4, 2]) === true)
