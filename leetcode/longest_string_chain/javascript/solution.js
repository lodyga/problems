class Solution {
   /**
    * Time complexity: O(n3)
    *     O(word count * avg word length**2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, hash set
    *     A: top-down
    * @param {string[]} words
    * @return {number}
    */
   longestStrChain(words) {
      const wordSet = new Set(words);
      const memo = new Map([["", 0]]);

      const dfs = (word) => {
         if (memo.has(word)) {
            return memo.get(word)
         }
         else if (!wordSet.has(word)) {
            return 0;
         }

         let res = 0;

         for (let idx = 0; idx < word.length; idx++) {
            res = Math.max(res, 1 + dfs(word.slice(0, idx) + word.slice(idx + 1,)));
         }

         memo.set(word, res);
         return res;
      }

      return Math.max(...words.map(word => dfs(word)));
   }
}


class Solution {
   /**
    * Time complexity: O(n3)
    *     O(word count * avg word length**2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: bottom-up
    * @param {string[]} words
    * @return {number}
    */
   longestStrChain(words) {
      words.sort((a, b) => a.length - b.length);
      const cache = new Map();

      for (const word of words) {
         cache.set(word, 1);
         
         for (let idx = 0; idx < word.length; idx++) {
            const predecessor = word.slice(0, idx) + word.slice(idx + 1,);
            
            if (cache.has(predecessor)) {
               cache.set(word, Math.max(cache.get(word), 1 + cache.get(predecessor)));
            }
         }
      }

      return Math.max(...cache.values());
   }
}


class Solution {
   /**
    * Time complexity: O(n3)
    *     O(word count**2 * avg word length)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string[]} words
    * @return {number}
    */
   longestStrChain(words) {
      const isPredecessor = (index1, index2) => {
         const word1 = words[index1];
         const word2 = words[index2];
         if (word1.length + 1 !== word2.length)
            return false

         let skipped = false
         index1 = 0;
         index2 = 0;
         while (index1 < word1.length) {
            if (word1[index1] !== word2[index2]) {
               if (skipped) {
                  return false
               } else {
                  skipped = true;
                  index1--;
               }
            }
            index1++;
            index2++;
         }
         return true
      }

      words.sort((a, b) => a.length - b.length);
      const cache = Array(words.length).fill(1);

      for (let left = words.length - 1; left > -1; left--) {
         for (let right = left + 1; right < words.length; right++) {
            if (isPredecessor(left, right)) {
               cache[left] = Math.max(cache[left], 1 + cache[right]);
            }
         }
      }

      return Math.max(...cache);
   }
}


const longestStrChain = new Solution().longestStrChain;
console.log(new Solution().longestStrChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']) === 4)
console.log(new Solution().longestStrChain(['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc']) === 5)
console.log(new Solution().longestStrChain(['abcd', 'dbqca']) === 1)
console.log(new Solution().longestStrChain(['qyssedya', 'pabouk', 'mjwdrbqwp', 'vylodpmwp', 'nfyqeowa', 'pu', 'paboukc', 'qssedya', 'lopmw', 'nfyqowa', 'vlodpmw', 'mwdrqwp', 'opmw', 'qsda', 'neo', 'qyssedhyac', 'pmw', 'lodpmw', 'mjwdrqwp', 'eo', 'nfqwa', 'pabuk', 'nfyqwa', 'qssdya', 'qsdya', 'qyssedhya', 'pabu', 'nqwa', 'pabqoukc', 'pbu', 'mw', 'vlodpmwp', 'x', 'xr']) === 8)
