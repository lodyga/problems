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
    * Time complexity: O(w*n2*3^k)
    *     n: board length
    *     k: word length
    *     w: word count
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: backtracking
    * @param {character[][]} board
    * @param {string[]} words
    * @return {string[]}
    */
   findWords(board, words) {
      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      let visited = Array.from(({ length: ROWS }), () => Array(COLS).fill(false));

      const backtrack = (index, row, col, word) => {
         if (index === word.length)
            return true
         else if (
            row == -1 ||
            col == -1 ||
            row === ROWS ||
            col === COLS ||
            board[row][col] !== word[index] ||
            visited[row][col]
         ) {
            return false
         }

         visited[row][col] = true;

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc]
            if (backtrack(index + 1, r, c, word))
               return true
         }

         visited[row][col] = false;
         return false
      }

      const wordFound = [];
      for (const word of words) {
         visited = Array.from(({ length: ROWS }), () => Array(COLS).fill(false));
         let isAdded = false;
         for (let row = 0; row < ROWS; row++) {
            if (isAdded)
               break
            for (let col = 0; col < COLS; col++) {
               if (backtrack(0, row, col, word)) {
                  wordFound.push(word)
                  isAdded = true;
                  break
               }
            }
         }
      }
      return wordFound
   };

   /**
    * Time complexity: O(n2*3^k + w)
    *     n: board length
    *     k: longest word length
    *     w: word count
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: backtracking
    * @param {character[][]} board
    * @param {string[]} words
    * @return {string[]}
    */
   findWords(board, words) {
      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      let visited = Array.from(({ length: ROWS }), () => Array(COLS).fill(false));
      const LONGEST = Math.max(...words.map(word => word.length));

      const trie = new Trie();
      words.forEach(word => trie.add(word));

      const backtrack = (index, row, col, node, word) => {
         if (
            index === LONGEST ||
            row == -1 ||
            col == -1 ||
            row === ROWS ||
            col === COLS ||
            visited[row][col] ||
            !node.letters.has(board[row][col])
         ) {
            return false
         }

         visited[row][col] = true;
         const letter = board[row][col];
         word = word + letter;
         node = node.letters.get(letter);

         if (node.isWord)
            wordFound.add(word);

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            if (backtrack(index + 1, r, c, node, word))
               return true
         }

         visited[row][col] = false;
         return false
      }

      const wordFound = new Set();
      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            (backtrack(0, row, col, trie.root, ''))
         }
      }
      return Array.from(wordFound)
   };
}


const findWords = new Solution().findWords;
console.log(new Solution().findWords([['a', 'b'], ['a', 'd']], ['aa', 'ab']).sort().toString() === ['aa', 'ab'].sort().toString())
console.log(new Solution().findWords([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']).sort().toString() === ['oath', 'eat'].sort().toString())
console.log(new Solution().findWords([['a', 'b'], ['c', 'd']], ['abcd']).sort().toString() === [].sort().toString())
console.log(new Solution().findWords([['o', 'a', 'b', 'n'], ['o', 't', 'a', 'e'], ['a', 'h', 'k', 'r'], ['a', 'f', 'l', 'v']], ['oa', 'oaa']).sort().toString() === ['oa', 'oaa'].sort().toString())
console.log(new Solution().findWords([["a", "b"], ["a", "a"]], ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]).sort().toString() === ["aba", "aaa", "aaab", "baa", "aaba"].sort().toString())
