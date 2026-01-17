class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: backtracking
    * @param {number} n
    * @return {string}
    */
   generateParenthesis(n) {
      const parenthesis = [];
      const parenthesisList = [];

      const dfs = (opened, closed) => {
         if (opened + closed == 2 * n) {
            parenthesisList.push(parenthesis.join(''));
            return
         }
         if (opened < n) {
            parenthesis.push('(');
            dfs(opened + 1, closed);
            parenthesis.pop();
         }
         if (opened !== closed) {
            parenthesis.push(')');
            dfs(opened, closed + 1);
            parenthesis.pop();
         }
      }
      dfs(0, 0);
      return parenthesisList
   };
}


const generateParenthesis = new Solution().generateParenthesis;
console.log(new Solution().generateParenthesis(1), ['()'])
console.log(new Solution().generateParenthesis(2), ['(())', '()()'])
console.log(new Solution().generateParenthesis(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])
