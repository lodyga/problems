import { Queue } from "@datastructures-js/queue"

class Solution {
   /**
    * Time complexity: O(n3):
    *     O(n*m*t)
    *     n: text length
    *     m: word count
    *     t: avg word length
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: array
    *     A: top-down
    * @param {string} text
    * @param {string[]} words
    * @return {boolean}
    */
   wordBreak(text, words) {
      /**
       * 
       * @param {number} left 
       * @param {string} word 
       * @returns {boolean}
       * text.slice(index, index + word.length) === word
       */
      const isWordInSegment = (left, word) => {
         if (left + word.length > text.length)
            return false
         for (let index = 0; index < word.length; index++)
            if (text[left + index] !== word[index])
               return false
         return true
      }
      const memo = Array(text.length + 1).fill(null);
      memo[memo.length - 1] = true;

      const dfs = (index) => {
         if (memo[index] !== null) {
            return memo[index]
         }

         let isSegmented = false;
         for (const word of words) {
            if (
               // text.slice(index, index + word.length) === word &&
               isWordInSegment(index, word) &&
               dfs(index + word.length)
            ) {
               isSegmented = true;
               break
            }
         }
         memo[index] = isSegmented;
         return isSegmented
      }
      return dfs(0)
   };

   /**
    * Time complexity: O(n3):
    *     O(n*m*t)
    *     n: text length
    *     m: word count
    *     t: avg word length
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: array
    *     A: bottom-up
    * @param {string} text
    * @param {string[]} words
    * @return {boolean}
    */
   wordBreak(text, words) {
      const cache = Array(text.length + 1).fill(false);
      cache[cache.length - 1] = true;

      for (let index = cache.length - 1; index > -1; index--) {
         for (const word of words) {
            if (
               text.slice(index, index + word.length) === word &&
               cache[index + word.length]
            ) {
               cache[index] = true;
               break
            }
         }
      }
      return cache[0]
   };

   /**
    * Time complexity: O(n3):
    *     O(n*t^2 + m)
    *     n: text length
    *     m: word count
    *     t: longest word length
    * Auxiliary space complexity: O(n+m*t)
    * Tags: 
    *     DS: tire, array
    *     A: bottom-up
    * @param {string} text
    * @param {string[]} words
    * @return {boolean}
    */
   wordBreak(text, words) {
      const cache = Array(text.length + 1).fill(false);
      cache[cache.length - 1] = true;
      const longestWord = Math.max(...words.map((word) => word.length));

      const trie = new Trie();
      for (const word of words) {
         trie.add(word);
      }

      for (let left = text.length - 1; left >= 0; left--) {
         for (let right = left; right < Math.min(text.length, left + longestWord); right++) {
            if (trie.lookup(left, right, text)) {
               cache[left] = cache[right + 1];
               if (cache[left])
                  break
            }
         }
      }
      return cache[0]
   };

   /**
    * Time complexity: O(n3):
    *     O(n*m*t)
    *     n: text length
    *     m: word count
    *     t: avg word length
    * Auxiliary space complexity: O(n+m*t)
    * Tags: 
    *     DS: queue
    *     A: bottom-up
    * @param {string} text
    * @param {string[]} words
    * @return {boolean}
    */
   wordBreak(text, words) {
      const bfs = (index) => {
         const queue = new Queue([index]);
         const visited = Array(text.length + 1).fill(false);
         visited[0] = true;

         while (!queue.isEmpty()) {
            const index = queue.pop();
            if (index === text.length)
               return true

            for (const word of words) {
               if (
                  text.slice(index, index + word.length) === word &&
                  visited[index + word.length] === false
               ) {
                  queue.push(index + word.length);
                  visited[index + word.length] = true;
               }
            }
         }
         return false
      }
      return bfs(0)
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
            node.letters.set(letter, new TrieNode());
         }
         node = node.letters.get(letter);
      }
      node.isWord = true
   }

   lookup(left, right, text) {
      let node = this.root;

      for (let index = left; index <= right; index++) {
         const letter = text[index];

         if (!node.letters.has(letter))
            return false
         node = node.letters.get(letter);
      }
      return node.isWord
   }
}



const wordBreak = new Solution().wordBreak;
console.log(new Solution().wordBreak('leetcode', ['leet', 'code']) === true)
console.log(new Solution().wordBreak('applepenapple', ['apple', 'pen']) === true)
console.log(new Solution().wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) === false)
console.log(new Solution().wordBreak('cars', ['car', 'ca', 'rs']) === true)
console.log(new Solution().wordBreak('aaaaaaa', ['aaaa', 'aa']) === false)
console.log(new Solution().wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) === false)
