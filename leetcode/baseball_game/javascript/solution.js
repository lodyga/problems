class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {string[]} operations
    * @return {number}
    */
   calPoints(operations) {
      const numberStack = [];

      for (const operation of operations) {
         if (operation === 'C') {
            numberStack.pop();
         } else if (operation === 'D') {
            numberStack.push(numberStack[numberStack.length - 1] * 2);
         } else if (operation === '+') {
            const prevNumber = numberStack.pop();
            const lastNumber = prevNumber + numberStack[numberStack.length - 1];
            numberStack.push(prevNumber, lastNumber);
         } else if (!isNaN(operation)) {
            numberStack.push(Number(operation));
         }
      }
      return numberStack.reduce((sum, number) => sum + number, 0)
   };
}


console.log(new Solution().calPoints(['5', '2', 'C', 'D', '+']), 30)
console.log(new Solution().calPoints(['5', '-2', '4', 'C', 'D', '9', '+', '+']), 27)
console.log(new Solution().calPoints(['1', 'C']), 0)