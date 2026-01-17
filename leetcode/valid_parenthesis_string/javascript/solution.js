class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {string} text
    * @return {boolean}
    */
   checkValidString(text) {
      const memo = Array.from({ length: text.length }, () => Array(text.length));

      const dfs = (index, opened) => {
         if (opened < 0) {
            return false
         } else if (index === text.length) {
            return opened === 0;
         } else if (memo[index][opened] !== undefined) {
            return memo[index][opened]
         }

         const char = text[index];
         let isValid = false;

         if (char === '(')
            isValid = dfs(index + 1, opened + 1);
         else if (char === ')')
            isValid = dfs(index + 1, opened - 1);
         else if (char === '*') {
            isValid = dfs(index + 1, opened);
            isValid ||= dfs(index + 1, opened + 1);
            isValid ||= dfs(index + 1, opened - 1);
         }

         memo[index][opened] = isValid;
         return isValid
      };

      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {string} text
    * @return {boolean}
    */
   checkValidString(text) {
      let minOpened = 0;
      let maxOpened = 0;

      for (const char of text) {
         if (char === '(') {
            minOpened += 1
            maxOpened += 1
         } else if (char === ')') {
            minOpened -= 1;
            maxOpened -= 1;
         } else { // '*'
            minOpened -= 1;
            maxOpened += 1;
         }

         minOpened = Math.max(minOpened, 0);
         if (maxOpened < 0)
            return false
      }
      return minOpened === 0
   };
}


const checkValidString = new Solution().checkValidString;
console.log(new Solution().checkValidString('*()') === true)
console.log(new Solution().checkValidString(')') === false)
console.log(new Solution().checkValidString('()') === true)
console.log(new Solution().checkValidString('(*') === true)
console.log(new Solution().checkValidString('(*)') === true)
console.log(new Solution().checkValidString('(*))') === true)
console.log(new Solution().checkValidString('(*)(') === false)
console.log(new Solution().checkValidString('(*)*()') === true)
console.log(new Solution().checkValidString('))(())') === false)
console.log(new Solution().checkValidString('((*)*)*)((*') === false)
console.log(new Solution().checkValidString('(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())') === false)
