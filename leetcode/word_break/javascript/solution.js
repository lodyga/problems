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
      const memo = Array(text.length).fill(-1);
      memo.push(1);

      const dfs = (idx) => {
         if (memo[idx] !== -1) {
            return memo[idx]
         }

         memo[idx] = 0;

         for (const word of words) {
            if (
               text.slice(idx, idx + word.length) === word &&
               dfs(idx + word.length)
            ) {
               memo[idx] = 1
               break
            }
         }

         return memo[idx]
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
      const cache = Array(text.length).fill(false);
      cache.push(true);

      for (let idx = cache.length - 1; idx > -1; idx--) {
         for (const word of words) {
            if (
               text.slice(idx, idx + word.length) === word &&
               cache[idx + word.length]
            ) {
               cache[idx] = true;
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
            if (trie.has(left, right, text)) {
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
      const bfs = (idx) => {
         const queue = new Queue([idx]);
         const visited = Array(text.length + 1).fill(false);
         visited[0] = true;

         while (!queue.isEmpty()) {
            const idx = queue.pop();
            if (idx === text.length)
               return true

            for (const word of words) {
               if (
                  text.slice(idx, idx + word.length) === word &&
                  visited[idx + word.length] === false
               ) {
                  queue.push(idx + word.length);
                  visited[idx + word.length] = true;
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

   has(left, right, text) {
      let node = this.root;

      for (let idx = left; idx <= right; idx++) {
         const letter = text[idx];

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
