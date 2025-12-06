class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack
    *     A: iteration
    * @param {string} word
    * @param {character} pivot
    * @return {string}
    */
   reversePrefix(word, pivot) {
      const letterStack = [];
      for (let index = 0; index < word.length; index++) {
         const letter = word[index];
         letterStack.push(letter);
         if (letter === pivot) {
            const prefix = letterStack.reverse().join('');
            const postfix = word.slice(index + 1);
            return prefix + postfix
         }
      }
      return word
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: iteration
    * @param {string} word
    * @param {character} pivot
    * @return {string}
    */
   reversePrefix(word, pivot) {
      for (let index = 0; index < word.length; index++) {
         const letter = word[index];
         if (letter === pivot) {
            const prefix = word.slice(0, index + 1).split('').reverse().join('');
            const postfix = word.slice(index + 1);
            return prefix + postfix
         }
      }
      return word
   };
}


const reversePrefix = new Solution().reversePrefix;
console.log(new Solution().reversePrefix('abcdefd', 'd') === 'dcbaefd')
console.log(new Solution().reversePrefix('xyxzxe', 'z') === 'zxyxxe')
console.log(new Solution().reversePrefix('abcd', 'z') === 'abcd')
