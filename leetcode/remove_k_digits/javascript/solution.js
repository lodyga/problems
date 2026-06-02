class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic increasing stack
    *     A: greedy
    * @param {string} nums
    * @param {number} k
    * @return {string}
    */
   removeKdigits(nums, k) {
      if (nums.length === k) return '0'
      const stack = [];
      let left = 0;

      for (const num of nums) {
         while (
            k &&
            stack.length &&
            stack[stack.length - 1] > num
         ) {
            stack.pop();
            k--;
         }

         stack.push(num);
      }

      const right = stack.length - k;

      while (
         left < nums.length &&
         stack[left] === '0'
      ) {
         left++;
      }

      const result = stack.slice(left, right).join('');
      return result === '' ? '0' : result
   }
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