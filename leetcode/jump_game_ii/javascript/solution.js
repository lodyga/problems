class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[]} numbers
    * @return {numbers}
    */
   jump(numbers) {
      let jumpCounter = 0
      let left = 0;
      let right = 0;

      while (right < numbers.length - 1) {
         let nextRight = 0;

         for (let index = left; index <= right; index++) {
            nextRight = Math.max(nextRight, index + numbers[index])
         }

         left = right + 1;
         right = nextRight;
         jumpCounter++;
      }
      return jumpCounter
   };
}
const jump = new Solution().jump;


console.log(new Solution().jump([2, 3, 1, 1, 4]) === 2)
console.log(new Solution().jump([2, 3, 0, 1, 4]) === 2)
console.log(new Solution().jump([0]) === 0)
console.log(new Solution().jump([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]) === 5)