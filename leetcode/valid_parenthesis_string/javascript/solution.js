class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down with memoization as hash map
    * Failed
    * @param {string} text
    * @return {boolean}
    */
   checkValidString(text) {
      const memo = new Map();

      const dfs = (index, opened) => {
         if (opened < 0)
            return false
         else if (index === text.length)
            return opened === 0;
         else if (memo.has(`${index},${opened}`))
            return memo.get(`${index},${opened}`)

         const char = text[index];
         let isValid = false;

         if (char === '(')
            isValid = dfs(index + 1, opened + 1);
         else if (char === ')')
            isValid = dfs(index + 1, opened - 1);
         else if (char === '*') {
            // blank char
            isValid = dfs(index + 1, opened);
            // opening parent
            isValid ||= dfs(index + 1, opened + 1);
            // closing parent
            isValid ||= dfs(index + 1, opened - 1);
         }

         memo.set(`${index},${opened}`, isValid);
         return isValid
      };

      return dfs(0, 0)
   };
}


const checkValidString = new Solution().checkValidString;
console.log(new Solution().checkValidString(")") === false)
console.log(new Solution().checkValidString("()") === true)
console.log(new Solution().checkValidString("(*") === true)
console.log(new Solution().checkValidString("(*)") === true)
console.log(new Solution().checkValidString("(*))") === true)
console.log(new Solution().checkValidString("(*)(") === false)
console.log(new Solution().checkValidString("(*)*()") === true)
console.log(new Solution().checkValidString("))(())") === false)
console.log(new Solution().checkValidString("((*)*)*)((*") === false)
console.log(new Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())") === false)