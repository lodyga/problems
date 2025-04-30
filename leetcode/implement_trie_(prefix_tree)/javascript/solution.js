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
    * Tags: trie as hash map
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

   _findNode(word) {
      let node = this.root;

      for (const letter of word) {
         if (!node.letters.has(letter)) {
            return false
         }
         node = node.letters.get(letter);
      }
      return node
   }

   search(word) {
      const node = this._findNode(word)
      return node === false ? false : node.isWord
   };

   startsWith(word) {
      const node = this._findNode(word)
      return Boolean(node)
   };
}


class TrieNode {
   /**
    * Trie node as list.
    */
   constructor() {
      this.letters = Array(26);
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
    * Tags: trie as hash map
    */
   constructor() {
      this.root = new TrieNode();
   }

   insert(word) {
      let node = this.root;

      for (const letter of word) {
         const index = letter.charCodeAt(0) - 'a'.charCodeAt(0);

         if (!node.letters[index]) {
            node.letters[index] = new TrieNode();
         }
         node = node.letters[index];
      }
      node.isWord = true;
   };

   _findNode(word) {
      let node = this.root;

      for (const letter of word) {
         const index = letter.charCodeAt(0) - 'a'.charCodeAt(0);

         if (!node.letters[index]) {
            return false
         }
         node = node.letters[index];
      }
      return node
   }

   search(word) {
      const node = this._findNode(word)
      return node === false ? false : node.isWord
   };

   startsWith(word) {
      const node = this._findNode(word)
      return Boolean(node)
   };
}


const trie = new Trie()
trie.insert('apple')
console.log(trie.search('apple'))  // return True
console.log(trie.search('app'))  // return False
console.log(trie.startsWith('app'))  // return True
trie.insert('app')
console.log(trie.search('app'))  // return True