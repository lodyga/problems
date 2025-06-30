class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[]} numbers
    * @return {boolean}
    */
   canJump(numbers) {
      let step = 1;
      
      for (let index = 0; index < numbers.length - 1; index++) {
         step = Math.max(step - 1, numbers[index]);

         if (step === 0) {
            return false
         }
      }
      return Boolean(step)
   };
}
const canJump = new Solution().canJump;


console.log(new Solution().canJump([2, 3, 1, 1, 4]) === true)
console.log(new Solution().canJump([3, 2, 1, 0, 4]) === false)
console.log(new Solution().canJump([0]) === true)
console.log(new Solution().canJump([2, 0, 0]) === true)
console.log(new Solution().canJump([0, 2, 3]) === false)
console.log(new Solution().canJump([1, 0, 1, 0]) === false)