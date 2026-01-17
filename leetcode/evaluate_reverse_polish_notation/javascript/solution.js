class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack
    *     A: iteration
    * @param {string[]} tokens
    * @return {number}
    */
   evalRPN(tokens) {
      const numStack = [];

      for (let token of tokens) {
         if (token === '+') {
            numStack.push(numStack.pop() + numStack.pop());
         } else if (token === '*') {
            numStack.push(numStack.pop() * numStack.pop());
         } else if (token === '-') {
            numStack.push(-numStack.pop() + numStack.pop());
         } else if (token === '/') {
            numStack.push(Math.trunc((1 / numStack.pop()) * numStack.pop()));
         } else {
            numStack.push(Number(token));
         }
      }
      return numStack[0]
   };
}


const evalRPN = new Solution().evalRPN;
console.log(new Solution().evalRPN(['2', '1', '+', '3', '*']) === 9)
console.log(new Solution().evalRPN(['4', '13', '5', '/', '+']) === 6)
console.log(new Solution().evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) === 22)
console.log(new Solution().evalRPN(['18']) === 18)
