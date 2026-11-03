class Solution {
   /**
    * Time complexity: O(n*k)
    *     n: number of words
    *     k: avg word length
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: list
    *     A: iteration
    * @param {string[]} words
    * @return {string}
    */
   longestCommonPrefix(words) {
      const prefix = Array.from(words[0]);

      for (const word of words) {
         while (prefix.length > word.length) {
            prefix.pop();
         }

         for (let idx = 0; idx < prefix.length; idx++) {
            if (prefix[idx] !== word[idx]) {
               while (prefix.length > idx) {
                  prefix.pop();
               }
               break;
            }
         }

         if (prefix.length === 0) {
            return "";
         }
      }

      return prefix.join("");
   }
}


const longestCommonPrefix = new Solution().longestCommonPrefix;
console.log(new Solution().longestCommonPrefix(["flower", "flow"]) === "flow")
console.log(new Solution().longestCommonPrefix(["flower", "flow", "flight"]) === "fl")
console.log(new Solution().longestCommonPrefix(["dog", "racecar", "car"]) === "")
console.log(new Solution().longestCommonPrefix(["aaa", "aa", "aaa"]) == "aa")
