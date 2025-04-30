class Solution {
   /**
    * Time complexity: O(n*k)
    *     n: number of words
    *     k: avg word length
    * Auxiliary space complexity: O(k)
    * @param {string[]} wordList
    * @return {string}
    */
   longestCommonPrefix(wordList) {
      let prefix = wordList[0];
      for (const word of wordList.slice(1,)) {
         for (let index = 0; index < word.length; index++) {
            const letter = word[index];
            if (
               index < prefix.length &&
               prefix[index] !== letter
            ) {
               prefix = prefix.slice(0, index);
               break
            }
            prefix = prefix.slice(0, word.length);
         }
      }
      return prefix
   };
}


console.log(new Solution().longestCommonPrefix(['flower', 'flow']) === 'flow')
console.log(new Solution().longestCommonPrefix(['flower', 'flow', 'flight']) === 'fl')
console.log(new Solution().longestCommonPrefix(['dog', 'racecar', 'car']) === '')