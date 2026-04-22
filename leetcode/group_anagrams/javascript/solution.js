class Solution {
   /**
    * Time complexity: O(n*k)
    *     n: words length
    *     k: avg word length
    * Auxiliary space complexity: O(n*k)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * @param {string[]} words
    * @return {string[][]}
    */
   groupAnagrams(words) {
      const anagramGroups = new Map();

      for (const word of words) {
         const letterFreq = Array(26).fill(0);

         for (const letter of word) {
            const idx = letter.charCodeAt(0) - 'a'.charCodeAt(0);
            letterFreq[idx]++;
         }

         const key = letterFreq.join(',')

         if (!anagramGroups.has(key)) {
            anagramGroups.set(key, [])
         }

         anagramGroups.get(key).push(word);
      }

      return Array.from(anagramGroups.values())
   };

   /**
    * Time complexity: O(n*klogk)
    *     n: words length
    *     k: avg word length
    * Auxiliary space complexity: O(n*k)
    * Tags:
    *     DS: hash map
    *     A: sorting
    * @param {string[]} words
    * @return {string[][]}
    */
   groupAnagrams(words) {
      const anagramGroups = new Map();

      for (const word of words) {
         const key = word.split('').sort().join(',');

         if (!anagramGroups.has(key)) {
            anagramGroups.set(key, []);
         }

         anagramGroups.get(key).push(word);
      }
      return Array.from(anagramGroups.values())
   };
}


const groupAnagrams = new Solution().groupAnagrams;
console.log(new Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']).toString() === [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']].toString())
console.log(new Solution().groupAnagrams(['']).toString() === [['']].toString())
console.log(new Solution().groupAnagrams(['a']).toString() === [['a']].toString())
console.log(new Solution().groupAnagrams(['tin', 'ram', 'zip', 'cry', 'pus', 'jon', 'zip', 'pyx']).toString() === [['tin'], ['ram'], ['zip', 'zip'], ['cry'], ['pus'], ['jon'], ['pyx']].toString())
console.log(new Solution().groupAnagrams(['bdddddddddd', 'bbbbbbbbbbc']).toString() === [['bdddddddddd'], ['bbbbbbbbbbc']].toString())
