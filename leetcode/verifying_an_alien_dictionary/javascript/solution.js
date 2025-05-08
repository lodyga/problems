class Solution {
   /**
    * Time complexity: O(n*k)
    *     n: word number
    *     k: avg word length
    * Auxiliary space complexity: O(1)
    * @param {string[]} worlList
    * @param {string} order
    * @return {boolean}
    */
   isAlienSorted(worlList, order) {
      function areWordsInOrder(word1, word2) {
         for (let index = 0; index < Math.min(word1.length, word2.length); index++) {
            if (letterOrder.get(word1[index]) < letterOrder.get(word2[index]))
               return true
            else if (letterOrder.get(word1[index]) > letterOrder.get(word2[index]))
               return false
         }
         return word1.length <= word2.length
      }

      const letterOrder = new Map(
         order
            .split('')
            .map((value, index) => [value, index])
         );

      for (let index = 0; index < worlList.length - 1; index++) {
         if (!areWordsInOrder(worlList[index], worlList[index + 1]))
            return false
      }
      return true
   };
}
const isAlienSorted = new Solution().isAlienSorted;


console.log(new Solution().isAlienSorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'), true)
console.log(new Solution().isAlienSorted(['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz'), false)
console.log(new Solution().isAlienSorted(['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz'), false)
console.log(new Solution().isAlienSorted(["ubg", "kwh"], "qcipyamwvdjtesbghlorufnkzx"), true)