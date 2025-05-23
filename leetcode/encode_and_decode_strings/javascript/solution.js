/**
 * Time complexity: O(n)
 *    n: all chars count
 * Auxiliary space complexity: O(n)
 * Tags: string
 */
class Solution {
   /**
    * @param {string[]} wordList
    * @return {string}
    */
   encode(wordList) {
      return wordList.map(word => word.length + '#' + word).join('')
   };

   /**
    * @param {string} text 
    * @return {string[]}
    */
   decode(text) {
      const wordList = [];
      let index = 0;

      while (index < text.length) {
         let wordLength = 0;

         while (text[index].match(/\d/)) {
            wordLength = Number(10 * wordLength) + Number(text[index]);
            index++;
         }

         if (text[index] === "#") {
            index++;
         }
         wordList.push(text.slice(index, index + wordLength));
         index += wordLength;
      }
      return wordList
   }
}


console.log(new Solution().encode(['code', 'site', 'love', 'you']) === '4#code4#site4#love3#you')
console.log(new Solution().decode(new Solution().encode(['code', 'site', 'love', 'you'])), ['code', 'site', 'love', 'you'])
console.log(new Solution().decode(new Solution().encode([''])), [''])
console.log(new Solution().decode(new Solution().encode(['1,23','45,6','7,8,9'])), ['1,23','45,6','7,8,9'])