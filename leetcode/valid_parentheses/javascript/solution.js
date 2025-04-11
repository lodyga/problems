class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {string} bracketList
    * @return {boolean}
   */
   isValid(bracketList) {
      if (bracketList.length % 2 != 0) return false

      const stackedBrackets = [];
      const closingBracket = {
         ")": "(",
         "]": "[",
         "}": "{",
      };
      for (const bracket of bracketList) {
         if (bracket in closingBracket) {
            if (stackedBrackets[stackedBrackets.length - 1] === closingBracket[bracket]) {
               stackedBrackets.pop();
            } else {
               return false
            }
         } else {
            stackedBrackets.push(bracket);
         }
      }
      return !Boolean(stackedBrackets.length)
   }
}


console.log(new Solution().isValid("()") === true)
console.log(new Solution().isValid("({})") === true)
console.log(new Solution().isValid("(})") === false)
console.log(new Solution().isValid("([)") === false)
console.log(new Solution().isValid("(]") === false)
console.log(new Solution().isValid("") === true)
console.log(new Solution().isValid("[") === false)
