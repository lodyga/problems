class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic increasing stack
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   sumSubarrayMins(nums) {
      const MOD = 10 ** 9 + 7;
      let res = 0
      // increasing stack: stack([(num, count), ...])
      const stack = [];
      let stackSum = 0;

      for (const num of nums) {
         let counter = 1;

         while (stack.length && stack[stack.length - 1][0] > num) {
            const [prevNum, prevCounter] = stack.pop();
            stackSum -= prevNum * prevCounter;
            counter += prevCounter;
         }

         stack.push([num, counter]);
         stackSum += num * counter;
         res = (res + stackSum) % MOD;
      }

      return res
   };
}


const sumSubarrayMins = new Solution().sumSubarrayMins;
console.log(new Solution().sumSubarrayMins([5, 4, 3]) === 22)
console.log(new Solution().sumSubarrayMins([3, 1, 2, 4]) === 17)
console.log(new Solution().sumSubarrayMins([11, 81, 94, 43, 3]) === 444)
