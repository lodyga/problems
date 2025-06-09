class TrieNode {
   constructor() {
      this.letters = new Map();
      this.isWord = false;
   }
}


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: trie
 * @return {TrieNode}
 */
class WordDictionary {
   constructor() {
      this.root = new TrieNode();
   };

   /**
    * @param {string} word
    * @return {void}
    */
   addWord(word) {
      let node = this.root;
      for (const letter of word) {
         if (!node.letters.has(letter))
            node.letters.set(letter, new TrieNode());
         node = node.letters.get(letter);
      }
      node.isWord = true;
   };

   /**
   * @param {string} word
   * @return {boolean}
   */
   search(word) {
      return dfs(0, this.root)

      function dfs(left, node) {
         for (let right = left; right < word.length; right++) {
            const letter = word[right];

            if (letter === '.') {
               // return [...node.letters.values()].some((valueNode) => dfs(right + 1, valueNode))
               for (const valueNode of node.letters.values()) {
                  if (dfs(right + 1, valueNode))
                     return true
               }
               return false
            }
            else if (node.letters.has(letter))
               node = node.letters.get(letter);
            else
               return false
         }
         return node.isWord
      }

   };
}


const word_dictionary = new WordDictionary()
word_dictionary.addWord('a')
console.log(word_dictionary.search('a')) // true
console.log(word_dictionary.search('b')) // false
console.log(word_dictionary.search('.')) // true

const word_dictionary2 = new WordDictionary()
word_dictionary2.addWord('bad')
word_dictionary2.addWord('dad')
word_dictionary2.addWord('mad')
console.log(word_dictionary2.search('pad')) // false
console.log(word_dictionary2.search('bad')) // true
console.log(word_dictionary2.search('.ad')) // true
console.log(word_dictionary2.search('b..')) // true