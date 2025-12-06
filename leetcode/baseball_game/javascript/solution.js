class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: stack
    *     A: iteration
    * @param {string[]} operations
    * @return {number}
    */
   calPoints(operations) {
      const numStack = [];

      for (const operation of operations) {
         if (operation === 'C') {
            numStack.pop();
         } else if (operation === 'D') {
            numStack.push(numStack[numStack.length - 1] * 2);
         } else if (operation === '+') {
            numStack.push(numStack[numStack.length - 2] + numStack[numStack.length - 1]);
         } else {
            numStack.push(Number(operation));
         }
      }
      return numStack.reduce((total, num) => total + num, 0)
   };
}


const calPoints = new Solution().calPoints;
console.log(new Solution().calPoints(['5', '2', 'C', 'D', '+']) == 30)
console.log(new Solution().calPoints(['5', '-2', '4', 'C', 'D', '9', '+', '+']) == 27)
console.log(new Solution().calPoints(['1', 'C']) == 0)
