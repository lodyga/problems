class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list, string
    *     A: backtracking
    * @param {number} n
    * @return {string}
    */
   generateParenthesis(n) {
      const parenthesis = [];
      const res = [];

      const dfs = (opened, closed) => {
         if (opened + closed == 2 * n) {
            res.push(parenthesis.join(''));
            return
         }

         if (opened < n) {
            parenthesis.push('(');
            dfs(opened + 1, closed);
            parenthesis.pop();
         }

         if (closed < opened) {
            parenthesis.push(')');
            dfs(opened, closed + 1);
            parenthesis.pop();
         }
      }
      dfs(0, 0);
      return res
   }
}
const generateParenthesis = new Solution().generateParenthesis;


console.log(new Solution().generateParenthesis(1).toString() === ['()'].toString())
console.log(new Solution().generateParenthesis(2).toString() === ['(())', '()()'].toString())
console.log(new Solution().generateParenthesis(3).toString() === ['((()))', '(()())', '(())()', '()(())', '()()()'].toString())
