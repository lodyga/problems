class Solution {
   /**
    * Time complexity: O(n*m)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list, array, string
    *     A: iteration
    * @param {string[]} words
    * @return {string[]}
    */
   commonChars(words) {
      const letters = Array(26).fill(100);
      const res = [];

      for (const word of words) {
         const letterFreq = Array(26).fill(0);

         for (const letter of word) {
            const idx = letter.charCodeAt(0) - 'a'.charCodeAt(0);
            letterFreq[idx]++;
         }

         for (let idx = 0; idx < 26; idx++) {
            letters[idx] = Math.min(letters[idx], letterFreq[idx]);
         }
      }

      for (let idx = 0; idx < 26; idx++) {
         if (letters[idx]) {
            for (let i = 0; i < letters[idx]; i++) {
               res.push(String.fromCharCode(idx + 'a'.charCodeAt(0)));
            }
         }
      }

      return res
   };
}


const commonChars = new Solution().commonChars;
console.log(new Solution().commonChars(["bella", "label", "roller"]).toString() === ["e", "l", "l"].toString())
console.log(new Solution().commonChars(["cool", "lock", "cook"]).toString() === ["c", "o"].toString())
