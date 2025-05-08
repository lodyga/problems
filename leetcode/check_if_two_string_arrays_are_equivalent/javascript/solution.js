class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string[]} word1List
    * @param {string[]} word2List
    * @return {boolean}
    */
   arrayStringsAreEqual(word1List, word2List) {
      function getLetterOrEnd(letter, word, wordList, isEnd) {
         if (letter === wordList[word].length) {
            word++;
            letter = 0;
            if (word == wordList.length)
               return [null, null, true]
         }
         return [letter, word, isEnd]
      };
      
      let [letter1, letter2] = [0, 0];
      let [word1, word2] = [0, 0];
      let [isEnd1, isEnd2] = [false, false];

      while (true) {
         if (word1List[word1][letter1] != word2List[word2][letter2])
            return false

         letter1++;
         letter2++;
         [letter1, word1, isEnd1] = getLetterOrEnd(letter1, word1, word1List, isEnd1);
         [letter2, word2, isEnd2] = getLetterOrEnd(letter2, word2, word2List, isEnd2);
         
         if (isEnd1 || isEnd2)
            return isEnd1 === isEnd2
      }
   };
}
const arrayStringsAreEqual = new Solution().arrayStringsAreEqual;


class Solution {
   /**
    * Time complexity: O(m+n)
    * Auxiliary space complexity: O(m+n)
    * Tags: build-in function
    * @param {string[]} word1List
    * @param {string[]} word2List
    * @return {boolean}
    */
   arrayStringsAreEqual(word1List, word2List) {
      return word1List.join('') === word2List.join('')
   };
}
const arrayStringsAreEqual = new Solution().arrayStringsAreEqual;


console.log(new Solution().arrayStringsAreEqual(['ab', 'c'], ['a', 'bc']), true)
console.log(new Solution().arrayStringsAreEqual(['a', 'cb'], ['ab', 'c']), false)
console.log(new Solution().arrayStringsAreEqual(['abc', 'd', 'defg'], ['abcddefg']), true)
console.log(new Solution().arrayStringsAreEqual(['abc', 'd', 'defg'], ['abcddef']), false)