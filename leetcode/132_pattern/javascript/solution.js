class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack, monotonic stack
    * monotonic decreasing stack
    * @param {number[]} numbers
    * @return {boolean}
    */
   find132pattern(numbers) {
      const stack = [];
      let prevMinNumber = numbers[0];

      for (const number of numbers.slice(1,)) {
         while (
            stack.length && 
            stack[stack.length - 1][1] <= number
         ) stack.pop();

         if (
            stack.length && 
            stack[stack.length - 1][0] < number
         ) return true

         stack.push([prevMinNumber, number]);
         prevMinNumber = Math.min(prevMinNumber, number);
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