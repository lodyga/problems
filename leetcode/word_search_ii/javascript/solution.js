class TrieNode {
   constructor() {
      this.letters = new Map();
      this.isWord = false;
   };
}


class Trie {
   constructor() {
      this.root = new TrieNode();
   };

   /**
    * @param {string} word 
    * @returns {void}
    */
   add(word) {
      let node = this.root;
      for (const letter of word) {
         if (!node.letters.has(letter)) {
            node.letters.set(letter, new TrieNode());
         }
         node = node.letters.get(letter);
      }
      node.isWord = true;
   }
}


class Solution {
   /**
    * Time complexity: O(nm*3^k)
    *     k: word length
    * Auxiliary space complexity: O(nm)
    * Tags: backtracking, trie
    * @param {character[][]} board
    * @param {string[]} words
    * @return {string[]}
    */
   findWords(board, words) {
      const rows = board.length;
      const cols = board[0].length;
      const visitedCells = new Set();
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const wordsFound = new Set();

      const wordTrie = new Trie();
      for (const word of words) {
         wordTrie.add(word);
      }

      const dfs = (row, col, node, word) => {
         if (
            row < 0 ||
            col < 0 ||
            row === rows ||
            col === cols ||
            !node.letters.has(board[row][col]) ||
            visitedCells.has(`${row},${col}`)
         ) {
            return false
         }

         visitedCells.add(`${row},${col}`);
         word += board[row][col];
         if (node.letters.get(board[row][col]).isWord) {
            wordsFound.add(word);
         }

         for (const [r, c] of DIRECTIONS) {
            dfs(row + r, col + c, node.letters.get(board[row][col]), word)
         }

         visitedCells.delete(`${row},${col}`);
         return false
      }

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            dfs(row, col, wordTrie.root, '')
         }
      }
      return [...wordsFound]
   };
}
const findWords = new Solution().findWords;


console.log(new Solution().findWords([['a', 'b'], ['a', 'd']], ['aa', 'ab']), ['aa', 'ab'])
console.log(new Solution().findWords([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']), ['oath', 'eat'])
console.log(new Solution().findWords([['a', 'b'], ['c', 'd']], ['abcd']), [])
console.log(new Solution().findWords([['o', 'a', 'b', 'n'], ['o', 't', 'a', 'e'], ['a', 'h', 'k', 'r'], ['a', 'f', 'l', 'v']], ['oa', 'oaa']), ['oa', 'oaa'])