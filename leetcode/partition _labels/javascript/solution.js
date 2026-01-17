class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * 
    * @param {string} text
    * @return {number[]}
    */
   partitionLabels(text) {
      const lastIndexes = new Map();
      
      for (let index = 0; index < text.length; index++) {
         const letter = text[index];
         lastIndexes.set(letter, index)
      }
      
      const partLens = [];
      let lastInd = 0;
      let partLen = 0;

      for (let index = 0; index < text.length; index++) {
         const letter = text[index];
         lastInd = Math.max(lastInd, lastIndexes.get(letter));
         partLen++;

         if (index === lastInd) {
            partLens.push(partLen);
            partLen = 0;
         }
      }
      return partLens
   };
}


const partitionLabels = new Solution().partitionLabels;
console.log(new Solution().partitionLabels('ababcc').toString() === [4, 2].toString())
console.log(new Solution().partitionLabels('ababcbacadefegdehijhklij').toString() === [9, 7, 8].toString())
console.log(new Solution().partitionLabels('eccbbbbdec').toString() === [10].toString())
