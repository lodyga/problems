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
      const backtrack = (idx, row, col, word) => {
         if (idx === word.length) {
            return true;
         }
         else if (
            row === -1 || row === ROWS
            || col === -1 || col === COLS
            || board[row][col] !== word[idx]
            || visited[row][col]
         ) {
            return false;
         }

         visited[row][col] = true;
         let isFound = false;

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc]
            if (backtrack(idx + 1, r, c, word)) {
               isFound = true;
               break;
            }
         };

         visited[row][col] = false;
         return isFound;
      };

      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      let visited = Array.from(({ length: ROWS }), () => Array(COLS).fill(false));
      const res = [];

      for (const word of words) {
         let isWordAdded = false;

         for (let row = 0; row < ROWS; row++) {
            if (isWordAdded) {
               break;
            }

            for (let col = 0; col < COLS; col++) {
               if (backtrack(0, row, col, word)) {
                  res.push(word);
                  isWordAdded = true;
                  break;
               }
            }
         }
      }

      return res;
   }
}


class TrieNode {
   constructor() {
      this.letters = new Map();
      this.wordIdx = -1;
   }
}


class Trie {
   constructor() {
      this.root = new TrieNode();
   };

   /**
    * @param {string} word 
    * @param {number} wordIdx
    * @returns {void}
    */
   add(word, wordIdx) {
      let node = this.root;

      for (const letter of word) {
         if (!node.letters.has(letter)) {
            node.letters.set(letter, new TrieNode());
         }

         node = node.letters.get(letter);
      }

      node.wordIdx = wordIdx;
   }
}


class Solution {
   /**
    * Time complexity: O(n2*3^k + w)
    *     n: board length
    *     k: longest word length
    *     c: letter count
    *     w: word count
    * Auxiliary space complexity: O(n2 + w)
    * Tags:
    *     DS: array (matrix)
    *     A: backtracking
    * @param {character[][]} board
    * @param {string[]} words
    * @return {string[]}
    */
   findWords(board, words) {
      const backtrack = (row, col, node) => {
         if (
            row === -1 || row === ROWS
            || col === -1 || col === COLS
            || !node.letters.has(board[row][col])
            || visited[row][col]
         ) {
            return;
         }

         visited[row][col] = true;
         const letter = board[row][col];
         const nextNode = node.letters.get(letter);

         // Remove dead branches from the Trie.
         if (nextNode.letters.length === 0 && nextNode.wordIdx === -1) {
            node.letters.delete(letter);
         }

         if (nextNode.wordIdx != -1) {
            resIdx.push(nextNode.wordIdx);
            nextNode.wordIdx = -1;
         }

         for (const [dr, dc] of DIRECTIONS) {
            backtrack(row + dr, col + dc, nextNode);
         }

         visited[row][col] = false;
      };

      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      let visited = Array.from(({ length: ROWS }), () => Array(COLS).fill(false));
      const resIdx = [];
      const trie = new Trie();

      words.forEach((word, idx) => trie.add(word, idx));

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (trie.root.letters.has(board[row][col])) {
               backtrack(row, col, trie.root);
            }
         }
      }

      return resIdx.map(idx => words[idx]);
   }
}


class TrieNode {
   constructor() {
      this.letters = new Map();
      this.wordIdx = -1;
   };

   /**
    * @param {string} word 
    * @param {number} wordIdx
    * @returns {void}
    */
   add(word, wordIdx) {
      let node = this;

      for (const letter of word) {
         if (!node.letters.has(letter)) {
            node.letters.set(letter, new TrieNode());
         }

         node = node.letters.get(letter);
      }

      node.wordIdx = wordIdx;
   }
}


class Solution {
   /**
    * Time complexity: O(n2*3^k + w)
    *     n: board length
    *     k: longest word length
    *     c: letter count
    *     w: word count
    * Auxiliary space complexity: O(n2 + w)
    * Tags:
    *     DS: array (matrix)
    *     A: backtracking
    * @param {character[][]} board
    * @param {string[]} words
    * @return {string[]}
    */
   findWords(board, words) {
      const backtrack = (row, col, node) => {
         if (
            row === -1 || row === ROWS
            || col === -1 || col === COLS
            || !node.letters.has(board[row][col])
            || visited[row][col]
         ) {
            return;
         }

         visited[row][col] = true;
         const letter = board[row][col];
         const nextNode = node.letters.get(letter);

         // Remove dead branches from the Trie.
         if (nextNode.letters.length === 0 && nextNode.wordIdx === -1) {
            node.letters.delete(letter);
         }

         if (nextNode.wordIdx != -1) {
            resIdx.push(nextNode.wordIdx);
            nextNode.wordIdx = -1;
         }

         for (const [dr, dc] of DIRECTIONS) {
            backtrack(row + dr, col + dc, nextNode);
         }

         visited[row][col] = false;
      };

      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      let visited = Array.from(({ length: ROWS }), () => Array(COLS).fill(false));
      const resIdx = [];
      const trie = new TrieNode();

      words.forEach((word, idx) => trie.add(word, idx));

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (trie.letters.has(board[row][col])) {
               backtrack(row, col, trie);
            }
         }
      }

      return resIdx.map(idx => words[idx]);
   }
}


const findWords = new Solution().findWords;
console.log(new Solution().findWords([['a', 'b'], ['a', 'd']], ['aa', 'ab']).sort().toString() === ['aa', 'ab'].sort().toString())
console.log(new Solution().findWords([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']).sort().toString() === ['oath', 'eat'].sort().toString())
console.log(new Solution().findWords([['a', 'b'], ['c', 'd']], ['abcd']).sort().toString() === [].sort().toString())
console.log(new Solution().findWords([['o', 'a', 'b', 'n'], ['o', 't', 'a', 'e'], ['a', 'h', 'k', 'r'], ['a', 'f', 'l', 'v']], ['oa', 'oaa']).sort().toString() === ['oa', 'oaa'].sort().toString())
console.log(new Solution().findWords([["a", "b"], ["a", "a"]], ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]).sort().toString() === ["aba", "aaa", "aaab", "baa", "aaba"].sort().toString())
