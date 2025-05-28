class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {number[]} pushed
    * @param {number[]} popped
    * @return {boolean}
    */
   validateStackSequences(pushed, popped) {
      const numberStack = [];
      let index = 0;

      for (const number of pushed) {
         numberStack.push(number);

         while (
            numberStack.length && 
            popped[index] === numberStack[numberStack.length - 1]
         ) {
            numberStack.pop();
            index++;
         }
      }
      return (
         numberStack.length === 0 &&
         index === popped.length
      )
   };
}


console.log(new Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) === true)
console.log(new Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) === false)
console.log(new Solution().validateStackSequences([2, 1, 0], [1, 2, 0]) === true)