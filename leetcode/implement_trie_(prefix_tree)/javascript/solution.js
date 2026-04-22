class TrieNode {
   /**
    * Trie node as hash map.
    */
   constructor() {
      this.letters = new Map();
      this.isWord = false;
   }
}


class Trie {
   /**
    * Time complexity:
    *     insert: O(n)
    *     search: O(n)
    *     startsWith: O(n)
    *     n: word length
    * Auxiliary space complexity: O(t)
    *     t: number of Trie nodes
    * Tags:
    *     DS: trie, hash map
    *     A: iteration
    */
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

      node.isWord = true;
   };

   _lookupNode(word) {
      let node = this.root;

      for (const letter of word) {
         if (!node.letters.has(letter)) {
            return null
         }

         node = node.letters.get(letter);
      }
      return node
   }

   search(word) {
      const node = this._lookupNode(word);
      return node ? node.isWord : false
   };

   startsWith(prefix) {
      return Boolean(this._lookupNode(prefix))
   };
}


const trie = new Trie()
trie.insert('apple')
console.log(trie.search('apple') === true)
console.log(trie.search('app') === false)
console.log(trie.startsWith('app') === true)
trie.insert('app')
console.log(trie.search('app') === true)
