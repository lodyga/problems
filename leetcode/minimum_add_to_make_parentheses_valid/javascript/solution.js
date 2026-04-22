class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {string} s
    * @return {number}
    */
   minAddToMakeValid(s) {
      let opened = 0;
      let openedAdded = 0;

      for (const par of s) {
         if (par === '(') {
            opened++;
         } else if (opened === 0) {
            openedAdded++;
         } else {
            opened--;
         }
      }

      return openedAdded + opened
   };
}


const minAddToMakeValid = new Solution().minAddToMakeValid;
console.log(new Solution().minAddToMakeValid('())') === 1)
console.log(new Solution().minAddToMakeValid('(((') === 3)
console.log(new Solution().minAddToMakeValid('()))((') === 4)
