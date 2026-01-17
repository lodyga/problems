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
      const dfs = (index, prevNum, isValid) => {
         if (index === text.length) {
            return isValid
         }

         let num = 0;
         for (let end = index; end < text.length; end++) {
            num = num * 10 + Number(text[end]);

            if (index === 0 || prevNum - 1 === num)
               if (dfs(end + 1, num, index !== 0))
                  return true
         }
         return false
      };
      return dfs(0, 0, 0);
   };
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
