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
      const getHash = (word) => {
         const hash = Array(26).fill(0);
         for (let index = 0; index < word.length; index++) {
            hash[word.charCodeAt(index) - 'a'.charCodeAt(0)]++;
         }
         return hash.join(',')
      }

      const anagramGroups = new Map();
      for (const word of words) {
         const key = getHash(word);
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
         if (!anagramGroups.has(key))
            anagramGroups.set(key, []);
         anagramGroups.get(key).push(word);
      }
      return Array.from(anagramGroups.values())
   };
}


const groupAnagrams = new Solution().groupAnagrams;
console.log(new Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
console.log(new Solution().groupAnagrams(['']), [['']])
console.log(new Solution().groupAnagrams(['a']), [['a']])
console.log(new Solution().groupAnagrams(['tin', 'ram', 'zip', 'cry', 'pus', 'jon', 'zip', 'pyx']), [['tin'], ['ram'], ['zip', 'zip'], ['cry'], ['pus'], ['jon'], ['pyx']])
console.log(new Solution().groupAnagrams(['bdddddddddd', 'bbbbbbbbbbc']), [['bdddddddddd'], ['bbbbbbbbbbc']])
