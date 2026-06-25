class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: backtracking with pruning
    * @param {string} text
    * @return {boolean}
    */
   splitString(text) {
      const dfs = (startIdx, prevNum, hasSplit) => {
         if (startIdx === text.length) {
            return hasSplit;
         }

         let num = 0;

         for (let idx = startIdx; idx < text.length; idx++) {
            num = num * 10 + Number(text[idx]);

            const isPrevValid = startIdx === 0 || prevNum - 1 === num;

            // pruning
            // if (startIdx !== 0 && num >= prevNum) {
            //    break;
            // }

            if (
               isPrevValid
               && dfs(idx + 1, num, startIdx !== 0)
            ) {
               return true;
            }
         }

         return false;
      }

      return dfs(0, 0, false);
   }
}


const splitString = new Solution().splitString;
console.log(new Solution().splitString('1') === false)
console.log(new Solution().splitString('21') === true)
console.log(new Solution().splitString('021') === true)
console.log(new Solution().splitString('201') === true)
console.log(new Solution().splitString('050043') === true)
console.log(new Solution().splitString('0090089') === true)
console.log(new Solution().splitString('001') === false)
console.log(new Solution().splitString('9080701') === false)
console.log(new Solution().splitString('1234') === false)
console.log(new Solution().splitString('64424509442147483647') === false)
