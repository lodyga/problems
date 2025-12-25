class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: stack
    *     A: two pointers
    * @param {number[]} pushed
    * @param {number[]} popped
    * @return {boolean}
    */
   validateStackSequences(pushed, popped) {
      const stack = [];
      let left = 0;
      let right = 0;

      while (left < pushed.length) {
         stack.push(pushed[left]);

         while (
            stack.length &&
            stack[stack.length - 1] === popped[right]
         ) {
            stack.pop();
            right++;
         }
         left++;
      }
      return (
         left === pushed.length &&
         right === popped.length
      )
   };
}


const validateStackSequences = new Solution().validateStackSequences;
console.log(new Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) === true)
console.log(new Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) === false)
console.log(new Solution().validateStackSequences([2, 1, 0], [1, 2, 0]) === true)
