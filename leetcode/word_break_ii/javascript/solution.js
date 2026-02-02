class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: backtracking
    * @param {string} text
    * @param {string[]} words
    * @return {string[]}
    */
   wordBreak(text, words) {
      const sentence = [];
      const sentences = [];

      const backtrack = (index) => {
         if (index === text.length) {
            sentences.push(sentence.join(' '));
            return
         } else if (index > text.length) {
            return
         }

         for (const word of words) {
            if (word === text.slice(index, index + word.length)) {
               sentence.push(word);
               backtrack(index + word.length);
               sentence.pop();
            }
         }
      }

      backtrack(0);
      return sentences
   };

   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: backtracking
    * @param {string} text
    * @param {string[]} words
    * @return {string[]}
    */
   wordBreak(text, words) {
      const sentence = [];
      const sentences = [];
      const wordSet = new Set(words)

      const backtrack = (start) => {
         if (start === text.length) {
            sentences.push(sentence.join(' '));
            return
         } else if (start > text.length) {
            return
         }

         for (let end = start + 1; end < text.length + 1; end++) {
            const word = text.slice(start, end);
            
            if (wordSet.has(word)) {
               sentence.push(word);
               backtrack(end);
               sentence.pop();
            }
         }
      }

      backtrack(0);
      return sentences
   };

   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {string} text
    * @param {string[]} wordList
    * @return {string[]}
    */
   wordBreak(text, wordList) {
      const words = new Set(wordList);
      const sentence = [];
      const sentences = [];
      let wordLength = 0;

      const wordTrie = new Trie();
      for (const word of words) {
         wordTrie.add(word);
         wordLength = Math.max(wordLength, word.length);
      }

      const dfs = (index) => {
         if (index === text.length) {
            sentences.push(sentence.join(' '));
            return
         }
         for (let right = index; right < Math.min(text.length, index + wordLength); right++) {
            const word = text.slice(index, right + 1);

            if (wordTrie.has(word)) {
               sentence.push(word);
               dfs(index + word.length);
               sentence.pop();
            }
         }
      }

      dfs(0);
      return sentences
   };
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

   /**
    * Add word to trie.
    * @param {string} word 
    * @returns {void}
    */
   add(word) {
      let node = this.root;  //const
      for (const letter of word) {
         if (!node.letters.has(letter)) {
            node.letters.set(letter, new TrieNode());
         }
         node = node.letters.get(letter);
      }
      node.isWord = true;
   }

   /**
    * Look up word in trie;
    * @param {string} word 
    * @returns {boolean}
    */
   has(word) {
      let node = this.root;
      for (const letter of word) {
         if (node.letters.has(letter)) {
            node = node.letters.get(letter);
         } else {
            return false
         }
      }
      return node.isWord
   }
}


const wordBreak = new Solution().wordBreak;
console.log(new Solution().wordBreak('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']).sort().toString() === ['cats and dog', 'cat sand dog'].sort().toString())
console.log(new Solution().wordBreak('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']).sort().toString() === ['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple'].sort().toString())
console.log(new Solution().wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']).sort().toString() === [].sort().toString())
