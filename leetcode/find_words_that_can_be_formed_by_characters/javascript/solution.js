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
      let res = 0;

      const charFreq = Array(26).fill(0);
      for (let idx = 0; idx < chars.length; idx++) {
         const pos = chars.charCodeAt(idx) - 'a'.charCodeAt(0);
         charFreq[pos]++;
      }

      for (const word of words) {
         const charFreqCopy = [...charFreq];
         res += word.length;

         for (let idx = 0; idx < word.length; idx++) {
            const pos = word.charCodeAt(idx) - 'a'.charCodeAt(0);
            
            if (charFreqCopy[pos] === 0) {
               res -= word.length;
               break;
            }

            charFreqCopy[pos]--;
         }
      }
      
      return res;
   }
}


const countCharacters = new Solution().countCharacters;
console.log(new Solution().countCharacters(['cat', 'bt', 'hat', 'tree'], 'atach') === 6)
console.log(new Solution().countCharacters(['hello', 'world', 'leetcode'], 'welldonehoneyr') === 10)
