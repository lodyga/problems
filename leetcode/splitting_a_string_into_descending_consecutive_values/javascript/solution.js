class Solution {
   /**
    * Time complexity: O(n^n)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {string} text
    * @return {boolean}
    */
   splitString(text) {
      return dfs(0, 0, 0);

      function dfs(index, prevValue, parts) {
         if (index === text.length) {
            return parts > 1
         }

         let value = 0;
         for (let index2 = index; index2 < text.length; index2++) {
            value = 10 * value + Number(text[index2]);

            if ((
               index === 0 ||
               prevValue - 1 === value
            ) &&
               dfs(index2 + 1, value, parts + 1)
            ) {
               return true
            }
         }
         return false
      }
   };
}
const splitString = new Solution().splitString;


console.log(new Solution().splitString('1') === false)
console.log(new Solution().splitString('21') === true)
console.log(new Solution().splitString('021') === true)
console.log(new Solution().splitString('201') === true)
console.log(new Solution().splitString('050043') === true)
console.log(new Solution().splitString('0090089') === true)
console.log(new Solution().splitString('9080701') === false)
console.log(new Solution().splitString('1234') === false)
console.log(new Solution().splitString('001') === false)