class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, array
    *     A: iteration
    * @param {string} s1
    * @param {string} s2
    * @return {string[]}
    */
   uncommonFromSentences(s1, s2) {
      const wordFreq = new Map();
      const res = [];

      for (const word of [...s1.split(' '), ...s2.split(' ')]) {
         wordFreq.set(word, (wordFreq.get(word) || 0) + 1);
      }
      
      for (const [word, freq] of wordFreq.entries()) {
         if (freq === 1) {
            res.push(word);
         }
      }
      
      return res
   };
}


const uncommonFromSentences = new Solution().uncommonFromSentences;
console.log(new Solution().uncommonFromSentences('this apple is sweet', 'this apple is sour').toString() === ['sweet', 'sour'].toString())
console.log(new Solution().uncommonFromSentences('apple apple', 'banana').toString() === ['banana'].toString())
