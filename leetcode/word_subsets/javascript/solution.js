class Solution {
   /**
    * Time complexity: O((n+m) * l)
    *     n: word1 length
    *     m: word2 length
    *     l: avg word length
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array, string
    *     A: iteration
    * @param {string[]} words1
    * @param {string[]} words2
    * @return {string()}
    */
   wordSubsets(words1, words2) {

      const getLetterFreq = (word) => {
         const letterFreq = Array(26).fill(0);

         for (let i = 0; i < word.length; i++) {
            const letterIndex = word.charCodeAt(i) - 'a'.charCodeAt(0);
            letterFreq[letterIndex] += 1;
         }

         return letterFreq
      }

      const pattren = Array(26).fill(0);
      const res = [];

      for (const word of words2) {
         const letterFreq = getLetterFreq(word);

         for (let index = 0; index < 26; index++) {
            pattren[index] = Math.max(pattren[index], letterFreq[index]);
         }
      }

      for (const word of words1) {
         const letterFreq = getLetterFreq(word);
         res.push(word);

         for (let index = 0; index < 26; index++) {
            if (letterFreq[index] < pattren[index]) {
               res.pop();
               break
            }
         }
      }

      return res
   };
}


const wordSubsets = new Solution().wordSubsets;
console.log(new Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]).sort().toString() === ["facebook", "google", "leetcode"].sort().toString())
console.log(new Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lc", "eo"]).sort().toString() === ["leetcode"].sort().toString())
console.log(new Solution().wordSubsets(["acaac", "cccbb", "aacbb", "caacc", "bcbbb"], ["c", "cc", "b"]).sort().toString() === ["cccbb"].sort().toString())
