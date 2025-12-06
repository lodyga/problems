/**
 * Time complexity: O(n):
 *     n: char count
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: list
 *     A: iteration
 */
class Solution {
   /**
    * @param {string[]} words
    * @return {string}
    */
   encode(words) {
      return words.map(word => word.length + '#' + word).join('')
   };

   /**
    * @param {string} text 
    * @return {string[]}
    */
   decode(text) {
      const words = [];
      let index = 0;

      while (index < text.length) {
         let wordLength = 0;

         while (text[index].match(/\d/)) {
            wordLength = Number(10 * wordLength) + Number(text[index]);
            index++;
         }

         index++;
         words.push(text.slice(index, index + wordLength));
         index += wordLength;
      }
      return words
   };
}


console.log(new Solution().encode(['code', 'site', 'love', 'you']) === '4#code4#site4#love3#you')
console.log(new Solution().decode(new Solution().encode(['code', 'site', 'love', 'you'])), ['code', 'site', 'love', 'you'])
console.log(new Solution().decode(new Solution().encode([''])), [''])
console.log(new Solution().decode(new Solution().encode(['1,23','45,6','7,8,9'])), ['1,23','45,6','7,8,9'])
