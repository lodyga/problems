class TrieNode {
   constructor() {
      // {(prefix letter, suffix letter): {}}
      this.letters = new Map();
      // this.isWord = false;
      this.counter = 0;
   };
}

class Trie {
   constructor() {
      this.root = new TrieNode();
   }

   add(word) {
      let node = this.root;

      for (let index = 0; index < word.length; index++) {
         const pair = `${word[index]}${word[word.length - 1 - index]}`;

         if (!node.letters.has(pair)) {
            node.letters.set(pair, new TrieNode());
         }

         node = node.letters.get(pair);
         node.counter++;

         // node.isWord = true;
      }
   };

   count(word) {
      let node = this.root;

      for (let index = 0; index < word.length; index++) {
         const pair = `${word[index]}${word[word.length - 1 - index]}`;

         if (!node.letters.has(pair)) {
            return 0
         }

         node = node.letters.get(pair);
      }
      return node.counter
   };
}

class Solution {
   /**
    * Time complexity: O(n2)
    *     O(n * m)
    *     n: word count
    *     m: word length
    * Auxiliary space complexity: O(n * m)
    * Tags:
    *     DS: trie
    * @param {string[]} words
    * @return {number}
    */
   countPrefixSuffixPairs(words) {
      const trie = new Trie();
      let counter = 0;

      for (const word of words.reverse()) {
         counter += trie.count(word);
         trie.add(word);
      }

      return counter
   };
}


const countPrefixSuffixPairs = new Solution().countPrefixSuffixPairs;
console.log(new Solution().countPrefixSuffixPairs(['a', 'aba', 'ababa', 'aa']) === 4)
console.log(new Solution().countPrefixSuffixPairs(['pa', 'papa', 'ma', 'mama']) === 2)
console.log(new Solution().countPrefixSuffixPairs(['abab', 'ab']) === 0)
