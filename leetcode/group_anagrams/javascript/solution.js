class Solution {
   /**
    * Time complexity: O(n*k)
    *     n: list length
    *     k: avg word length
    * Auxiliary space complexity: O(n*k)
    * Tags: hash map
    * @param {string[]} wordList
    * @return {string[][]}
    */
   groupAnagrams(wordList) {
      const groupedAnagrams = new Map();

      for (const word of wordList) {
         const bucket = Array(26).fill(0);
         for (const letter of word) {
            bucket[letter.charCodeAt(0) - 'a'.charCodeAt(0)]++;
         }
         const key = bucket.join(',');

         if (!groupedAnagrams.has(key)) {
            groupedAnagrams.set(key, [])
         }
         groupedAnagrams.get(key).push(word);
      }
      return Array.from(groupedAnagrams.values())
   };
}
const groupAnagrams = new Solution().groupAnagrams;


console.log(new Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
console.log(new Solution().groupAnagrams(['']), [['']])
console.log(new Solution().groupAnagrams(['a']), [['a']])
console.log(new Solution().groupAnagrams(['tin', 'ram', 'zip', 'cry', 'pus', 'jon', 'zip', 'pyx']), [['tin'], ['ram'], ['zip', 'zip'], ['cry'], ['pus'], ['jon'], ['pyx']])
console.log(new Solution().groupAnagrams(['bdddddddddd', 'bbbbbbbbbbc']), [['bdddddddddd'], ['bbbbbbbbbbc']])