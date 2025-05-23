class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {number} n
    * @return {string}
    */
   generateParenthesis(n) {
      const parenthesis = [];
      const parenthesisList = [];

      dfs(n, n);
      return parenthesisList

      function dfs(open, close) {
         if (
            open === 0 &&
            close === 0
         ) {
            parenthesisList.push(parenthesis.join(''));
            return
         }
         if (open) {
            parenthesis.push('(');
            dfs(open - 1, close);
            parenthesis.pop();
         }
         if (close > open) {
            parenthesis.push(')');
            dfs(open, close - 1);
            parenthesis.pop();
         }
      }
   };
}


console.log(new Solution().generateParenthesis(1), ['()'])
console.log(new Solution().generateParenthesis(2), ['(())', '()()'])
console.log(new Solution().generateParenthesis(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])