class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack
    *     A: iteration
    * @param {string} bracketList
    * @return {boolean}
   */
   isValid(bracketList) {
      if (bracketList.length % 2 != 0) return false

      const bracketStack = [];
      const closingBracket = {
         ')': '(',
         ']': '[',
         '}': '{'
      };
      for (const bracket of bracketList) {
         if (bracket in closingBracket) {
            if (bracketStack[bracketStack.length - 1] === closingBracket[bracket]) {
               bracketStack.pop();
            } else {
               return false
            }
         } else {
            bracketStack.push(bracket);
         }
      }
      return bracketStack.length === 0
   }
}


const isValid = new Solution().isValid;
console.log(new Solution().isValid('()') === true)
console.log(new Solution().isValid('({})') === true)
console.log(new Solution().isValid('(})') === false)
console.log(new Solution().isValid('([)') === false)
console.log(new Solution().isValid('(]') === false)
console.log(new Solution().isValid('') === true)
console.log(new Solution().isValid('[') === false)
