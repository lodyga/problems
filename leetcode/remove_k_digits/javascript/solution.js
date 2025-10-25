class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack, monotonic stack
    * monotonic increasing stack
    * @param {string} numbers
    * @param {number} k
    * @return {string}
    */
   removeKdigits(numbers, k) {
      if (numbers.length === k) return '0'
      const stack = [];

      for (const number of numbers) {
         while (
            k &&
            stack.length &&
            stack[stack.length - 1] > number
         ) {
            stack.pop();
            k--;
         }
         stack.push(number);
      }
      const right = stack.length - k;

      let left = 0;
      while (
         left < numbers.length &&
         stack[left] === '0'
      ) left++;
      
      const result = stack.slice(left, right).join('');
      return result === '' ? '0' : result
   };
}
const removeKdigits = new Solution().removeKdigits;


console.log(new Solution().removeKdigits('12345', 2) === '123')
console.log(new Solution().removeKdigits('54321', 2) === '321')
console.log(new Solution().removeKdigits('1432219', 3) === '1219')
console.log(new Solution().removeKdigits('10200', 1) === '200')
console.log(new Solution().removeKdigits('10', 2) === '0')
console.log(new Solution().removeKdigits('9', 1) === '0')
console.log(new Solution().removeKdigits('112', 1) === '11')
console.log(new Solution().removeKdigits('1173', 2) === '11')
console.log(new Solution().removeKdigits('10', 1) === '0')
console.log(new Solution().removeKdigits('33526221184202197273', 19) === '0')