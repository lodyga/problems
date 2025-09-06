class Solution {
   /**
    * Time complexity: O(n3):
    *     O(n*m*t)
    *     n: text length
    *     m: the number of words
    *     t: max word length
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {string} text
    * @param {string[]} wordList
    * @return {boolean}
    */
   wordBreak(text, wordList) {
      const cache = Array(text.length + 1).fill(false);
      cache[cache.length - 1] = true;

      for (let index = cache.length - 1; index >= 0; index--) {
         for (const word of wordList) {
            if (text.slice(index, index + word.length) === word) {
               cache[index] = cache[index + word.length];
               if (cache[index])
                  break
            }
         }
      }
      return cache[0]
   };
}


class Solution {
   /**
    * Time complexity: O(n3):
    *     O(n*m*t)
    *     n: text length
    *     m: the number of words
    *     t: max word length
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {string} text
    * @param {string[]} wordList
    * @return {boolean}
    */
   wordBreak(text, wordList) {
      const memo = new Map([[text.length, true]]);
      return dfs(0)

      function dfs(index) {
         if (memo.has(index)) {
            return memo.get(index)
         }

         for (const word of wordList) {
            if (
               text.slice(index, index + word.length) === word &&
               dfs(index + word.length)
            ) {
               memo.set(index, true);
               return true
            }
         }

         memo.set(index, false);
         return false
      }
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

   insert(word) {
      let node = this.root;

      for (const letter of word) {
         if (!node.letters.has(letter)) {
            node.letters.set(letter, new TrieNode());
         }
         node = node.letters.get(letter);
      }
      node.isWord = true
   }

   search(word, left, right) {
      let node = this.root;

      for (let index = left; index <= right; index++) {
         const letter = word[index];

         if (node.letters.has(letter)) {
            node = node.letters.get(letter);
         } else {
            return false
         }
      }
      return node.isWord
   }
}


class Solution {
   /**
    * Time complexity: O(n3):
    *     O(n*t^2)
    *     n: text length
    *     m: the number of words
    *     t: max word length
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up, trie
    * @param {string} text
    * @param {string[]} wordList
    * @return {boolean}
    */
   wordBreak(text, wordList) {
      const cache = Array(text.length + 1).fill(false);
      cache[cache.length - 1] = true;
      const longestWord = Math.max(...wordList.map((word) => word.length));

      const trie = new Trie();
      for (const word of wordList) {
         trie.insert(word);
      }

      for (let left = text.length - 1; left >= 0; left--) {
         for (let right = left; right < Math.min(text.length, left + longestWord); right++) {
            if (trie.search(text, left, right)) {
               cache[left] = cache[right + 1];
               if (cache[left])
                  break
            }
         }
      }
      return cache[0]
   };
}


console.log(new Solution().wordBreak('leetcode', ['leet', 'code']) === true)
console.log(new Solution().wordBreak('applepenapple', ['apple', 'pen']) === true)
console.log(new Solution().wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) === false)
console.log(new Solution().wordBreak('cars', ['car', 'ca', 'rs']) === true)
console.log(new Solution().wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) === false)