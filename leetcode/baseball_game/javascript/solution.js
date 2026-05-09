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
      const stack = [];

      for (const operation of operations) {
         switch (operation) {
            case 'C':
               stack.pop();
               break;
            case 'D':
               stack.push(stack[stack.length - 1] * 2);
               break;
            case '+':
               stack.push(
                  stack[stack.length - 2]
                  + stack[stack.length - 1]
               );
               break;
            default:
               stack.push(Number(operation));
         }
      }

      return stack.reduce((sum, num) => sum + num, 0)
   }
}


const calPoints = new Solution().calPoints;
console.log(new Solution().calPoints(['5', '2', 'C', 'D', '+']), 30)
console.log(new Solution().calPoints(['5', '2', 'C', 'D', '+']) == 30)
console.log(new Solution().calPoints(['5', '-2', '4', 'C', 'D', '9', '+', '+']) == 27)
console.log(new Solution().calPoints(['1', 'C']) == 0)
