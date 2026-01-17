class TrieNode {
   constructor() {
      this.letters = new Map();
      this.isWord = false;
   }
}


/**
 * Time complexity:
 *     constructor: O(1)
 *     addWord: O(k)
 *     search: O(min(26^k, 26^w, n*k))
 *     n: word count
 *     k: word length
 *     w: windcard count
 * Auxiliary space complexity: O(n*k)
 * Tags:
 *     DS: trie
 *     A: iteration, recursion
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
      const dfs = (start, node) => {
         for (let index = start; index < word.length; index++) {
            const letter = word[index];

            if (node.letters.has(letter)) {
               node = node.letters.get(letter);
            } else if (letter === '.') {
               for (const wildCard of node.letters.keys()) {
                  if (dfs(index + 1, node.letters.get(wildCard)))
                     return true
               }
               return false
            } else {
               return false
            }
         }
         return node.isWord
      }
      return dfs(0, this.root)
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let wordDictionary;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'WordDictionary') {
         wordDictionary = new WordDictionary(...argument);
         output.push(null);
      } else if (operation === 'addWord') {
         wordDictionary.addWord(...argument);
         output.push(null);
      } else if (operation === 'search') {
         output.push(wordDictionary.search(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
    ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
]

const argumentsList = [
   [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]],
    [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
]

const expectedOutputList = [
   [null,null,null,null,false,true,true,true],
    [null, null, null, true, true, false, true, false, false]
]


// Run tests
/**
 * Run a batch of TimeMap tests and compare outputs with expected results.
 * If show_output is true, returns [(actual, expected), ...] instead of booleans.
 * @param {string[][]} operationsList 
 * @param {number[][][]} argumentsList 
 * @param {number[][]} expectedOutputList 
 * @returns {boolean}
 */
const runTests = (operationsList, argumentsList, expectedOutputList, showOutput) => {
   const output = [];

   for (let index = 0; index < operationsList.length; index++) {
      const operations = operationsList[index];
      const args = argumentsList[index];
      const expectedOutput = expectedOutputList[index];
      if (showOutput) {
         output.push([testInput(operations, args), expectedOutput])
      } else {
         output.push(JSON.stringify(testInput(operations, args)) === JSON.stringify(expectedOutput))
      }
   }
   return output
}
console.log(runTests(operationsList, argumentsList, expectedOutputList))


// Example 1
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