class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack
    *     A: iteration
    * @param {string} brackets
    * @return {boolean}
   */
   static isValid(brackets) {
      if (brackets.length % 2) return false

      const stack = [];
      const BRACKET_MAP = {
         ')': '(',
         ']': '[',
         '}': '{'
      };

      for (const bracket of brackets) {
         if (bracket in BRACKET_MAP) {
            if (stack[stack.length - 1] === BRACKET_MAP[bracket]) {
               stack.pop();
            } else {
               return false
            }
         } else {
            stack.push(bracket);
         }
      }

      return stack.length === 0
   }
}


const isValid = Solution.isValid;
console.log(Solution.isValid('()') === true)
console.log(Solution.isValid('({})') === true)
console.log(Solution.isValid('(})') === false)
console.log(Solution.isValid('([)') === false)
console.log(Solution.isValid('(]') === false)
console.log(Solution.isValid('') === true)
console.log(Solution.isValid('[') === false)
console.log(Solution.isValid(')') === false)
console.log(Solution.isValid(')(') === false)
