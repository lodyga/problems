class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {string} text
    * @param {string} locked
    * @return {boolean}
    */
   canBeValid(text, locked) {
      if (text.length % 2 === 1) {
         return false
      }

        let minOpened = 0;
        let maxOpened = 0;

        for (let i = 0; i < text.length; i++) {
           const [p, b] = [text[i], locked[i]];
           
           if (b === '0') {
              minOpened--;
              maxOpened++;
            } else if (p === '(') {
               minOpened++;
               maxOpened++;
            } else if (p === ')') {
               minOpened--;
               maxOpened--;
            }

            if (maxOpened < 0) {
               return false
            }
            
            minOpened = Math.max(minOpened, 0);
         }

        return minOpened === 0
   };
}


const canBeValid = new Solution().canBeValid;
console.log(new Solution().canBeValid('()', '11') === true)
console.log(new Solution().canBeValid('))()))', '010100') === true)
console.log(new Solution().canBeValid('()()', '0000') === true)
console.log(new Solution().canBeValid(')', '0') === false)
console.log(new Solution().canBeValid('(((())', '111111') === false)
console.log(new Solution().canBeValid('(((())(((())', '111111010111') === true)
console.log(new Solution().canBeValid('()()((()))((', '111111101101') === false)
