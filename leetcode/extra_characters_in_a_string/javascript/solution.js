class Solution {
   /**
    * Time complexity: O(n3)
    *     O(text length * word count * word lenght)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string} text
    * @param {string[]} words
    * @return {number}
    */
   minExtraChar(text, words) {
      const cache = Array(text.length + 1).fill(0);

      for (let idx = text.length - 1; idx > -1; idx--) {
         cache[idx] = cache[idx + 1] + 1;

         for (const word of words) {
            if (
               idx + word.length <= text.length &&
               text.slice(idx, idx + word.length) === word
            ) {
               cache[idx] = Math.min(
                  cache[idx],
                  cache[idx + word.length]
               );
            }

            if (cache[idx] === 0) {
               break;
            }
         }
      }

      return cache[0];
   }
}


class Solution {
   /**
    * Time complexity: O(n3)
    *     O(text length * distinct word count * word lenght)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: bottom-up
    *     check every distinct word length
    * @param {string} text
    * @param {string[]} words
    * @return {number}
    */
   minExtraChar(text, words) {
      const cache = Array(text.length + 1).fill(0);
      const wordLengths = new Set(words.map((word) => word.length));
      const wordSet = new Set(words);

      for (let idx = text.length - 1; idx > -1; idx--) {
         cache[idx] = cache[idx + 1] + 1;

         for (const wordLength of wordLengths) {
            if (
               idx + wordLength <= text.length &&
               wordSet.has(text.slice(idx, idx + wordLength))
            ) {
               cache[idx] = Math.min(
                  cache[idx],
                  cache[idx + wordLength]
               );
            }

            if (cache[idx] === 0) {
               break;
            }
         }
      }

      return cache[0];
   }
}


class TrieNode {
   constructor() {
      this.letters = new Map();
      this.isWord = false;
   }
}


class Trie {
   constructor() {
      this.root = new TrieNode();
   }

   add(word) {
      let node = this.root;
      for (const letter of word) {
         if (!node.letters.has(letter)) {
            node.letters.set(letter, new TrieNode())
         }
         node = node.letters.get(letter);
      }
      node.isWord = true;
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    *     O(text length * word lenght)
    * Auxiliary space complexity: O(n2)
    *     O(word count * word length) + O(text lenght)
    * Tags:
    *     DS: trie
    *     A: bottom-up
    * @param {string} text
    * @param {string[]} words
    * @return {number}
    */
   minExtraChar(text, words) {
      const LONGEST_WORD_LENGTH = Math.max(...words.map((word) => word.length));
      const trie = new Trie();
      
      for (const word of words) {
         trie.add(word);
      }
      
      const cache = Array(text.length + 1).fill(0);

      for (let left = text.length - 1; left > -1; left--) {
         cache[left] = cache[left + 1] + 1;
         let node = trie.root;

         for (let right = left; right < Math.min(text.length, left + LONGEST_WORD_LENGTH); right++) {
            const letter = text[right];

            if (!node.letters.has(letter)) {
               break;
            }

            node = node.letters.get(letter);

            if (node.isWord) {
               cache[left] = Math.min(cache[left], cache[right + 1]);
            }

            if (cache[left] === 0) {
               break;
            }
         }
      }

      return cache[0];
   }
}


const minExtraChar = new Solution().minExtraChar;
console.log(new Solution().minExtraChar('ab', ['a', 'b']) === 0)
console.log(new Solution().minExtraChar('leetcode', ['leet', 'code', 'leetcode']) === 0)
console.log(new Solution().minExtraChar('leetscode', ['leet', 'code', 'leetcode']) === 1)
console.log(new Solution().minExtraChar('sayhelloworld', ['hello', 'world']) === 3)
console.log(new Solution().minExtraChar('ecolloycollotkvzqpdaumuqgs', ['flbri', 'uaaz', 'numy', 'laper', 'ioqyt', 'tkvz', 'ndjb', 'gmg', 'gdpbo', 'x', 'collo', 'vuh', 'qhozp', 'iwk', 'paqgn', 'm', 'mhx', 'jgren', 'qqshd', 'qr', 'qpdau', 'oeeuq', 'c', 'qkot', 'uxqvx', 'lhgid', 'vchsk', 'drqx', 'keaua', 'yaru', 'mla', 'shz', 'lby', 'vdxlv', 'xyai', 'lxtgl', 'inz', 'brhi', 'iukt', 'f', 'lbjou', 'vb', 'sz', 'ilkra', 'izwk', 'muqgs', 'gom', 'je']) === 2)
