class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string} text
    * @return {number[]}
    */
   partitionLabels(text) {
      const letterLastIndex = new Map();
      for (let index = 0; index < text.length; index++) {
         const letter = text[index];
         letterLastIndex.set(letter, index)
      }
      
      let counter = 0;
      let end = 0;
      const partitionLengths = [];

      for (let index = 0; index < text.length; index++) {
         const letter = text[index];
         counter++;
         end = Math.max(end, letterLastIndex.get(letter));

         if (index === end) {
            partitionLengths.push(counter);
            counter = 0;
         }
      }
      return partitionLengths
   };
}
const partitionLabels = new Solution().partitionLabels;


console.log(new Solution().partitionLabels('ababcc'), [4, 2])
console.log(new Solution().partitionLabels('ababcbacadefegdehijhklij'), [9, 7, 8])
console.log(new Solution().partitionLabels('eccbbbbdec'), [10])