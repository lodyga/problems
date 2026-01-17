class Solution {
   /**
    * Time complexity: O(n2)
    *     O(w * c):
    *     w: word count
    *     c: avg char count
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {string[]} words
    * @param {string} chars
    * @return {number}
    */
   countCharacters(words, chars) {
      let counter = 0;

      const charFreq = Array(26).fill(0);
      for (let index = 0; index < chars.length; index++) {
         const pos = chars.charCodeAt(index) - 'a'.charCodeAt(0);
         charFreq[pos]++;
      }

      for (const word of words) {
         const charFreqCopy = [...charFreq];
         counter += word.length;

         for (let index = 0; index < word.length; index++) {
            const pos = word.charCodeAt(index) - 'a'.charCodeAt(0);
            if (charFreqCopy[pos] === 0) {
               counter -= word.length;
               break
            }
            charFreqCopy[pos]--;
         }
      }
      return counter
   };
}


const countCharacters = new Solution().countCharacters;
console.log(new Solution().countCharacters(['cat', 'bt', 'hat', 'tree'], 'atach') === 6)
console.log(new Solution().countCharacters(['hello', 'world', 'leetcode'], 'welldonehoneyr') === 10)
