class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} word
    * @param {character} pivot
    * @return {string}
    */
   reversePrefix(word, pivot) {
      const prefixArray = [];
      let hasPrefix = false;
      let index = 0;

      for (index; index < word.length; index++) {
         const letter = word[index];
         prefixArray.push(letter);
         if (letter === pivot) {
            hasPrefix = true;
            break
         }
      }

      if (hasPrefix) {
         const prefix = prefixArray.reverse().join('');
         const base = word.slice(index + 1);
         return prefix + base
      } else
         return word
   };
}


console.log(new Solution().reversePrefix('abcdefd', 'd'), 'dcbaefd')
console.log(new Solution().reversePrefix('xyxzxe', 'z'), 'zxyxxe')
console.log(new Solution().reversePrefix('abcd', 'z'), 'abcd')