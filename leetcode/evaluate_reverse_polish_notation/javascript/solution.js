class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {string[]} tokens
    * @return {number}
    */
   evalRPN(tokens) {
      const digitStack = [];

      for (let token of tokens) {
         if (token === '+') {
            digitStack.push(digitStack.pop() + digitStack.pop());
         } else if (token === '*') {
            digitStack.push(digitStack.pop() * digitStack.pop());
         } else if (token === '-') {
            digitStack.push(-digitStack.pop() + digitStack.pop());
         } else if (token === '/') {
            digitStack.push(Math.trunc((1/digitStack.pop()) * digitStack.pop()));
         } else {
            digitStack.push(Number(token));
         }
      }
      return digitStack[0]
   };
}
const evalRPN = new Solution().evalRPN;


console.log(new Solution().evalRPN(['2', '1', '+', '3', '*']), 9)
console.log(new Solution().evalRPN(['4', '13', '5', '/', '+']), 6)
console.log(new Solution().evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']), 22)
console.log(new Solution().evalRPN(['18']), 18)