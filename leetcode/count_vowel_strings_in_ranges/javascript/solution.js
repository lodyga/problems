class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: prefix sum
    * @param {string[]} words
    * @param {number[]=} queries
    * @return {number[]}
    */
   vowelStrings(words, queries) {
      const vowels = 'aeoiu';
      const prefix = [0];
      
      for (let index = 0; index < words.length; index++) {
         const word = words[index];
         const areVowelEnds = vowels.includes(word[0]) && vowels.includes(word[word.length - 1]);
         prefix.push(prefix[prefix.length - 1] + areVowelEnds);
      }

      const res = [];
      
      for (const [start, end] of queries) {
         res.push(prefix[end + 1] - prefix[start]);
      }
      
      return res
   };
}


const vowelStrings = new Solution().vowelStrings;
console.log(new Solution().vowelStrings(['a', 'e', 'i'], [[0, 2], [0, 1], [2, 2]]).toString() === [3, 2, 1].toString())
console.log(new Solution().vowelStrings(['aba', 'bcb', 'ece', 'aa', 'e'], [[0, 2], [1, 4], [1, 1]]).toString() === [2, 3, 0].toString())
