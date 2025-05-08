class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string} word1
    * @param {string} word2
    * @return {boolean}
    */
   backspaceCompare(word1, word2) {
      function nextValidChar(index, text) {
         let skip = 0;

         while (
            index >= 0 &&
            (text[index] == '#' || skip)
         ) {
            text[index] == '#' ? skip++ : skip--;
            index--;
         }
         return index
      };

      let index1 = word1.length - 1;
      let index2 = word2.length - 1;

      while (index1 >= 0 && index2 >= 0) {
         index1 = nextValidChar(index1, word1);
         index2 = nextValidChar(index2, word2);

         if (word1[index1] !== word2[index2])
            return false

         if (index1 === 0 && index2 === 0)
            return true

         index1--;
         index2--;
      }
      return nextValidChar(index1, word1) === nextValidChar(index2, word2)
   };
}


console.log(new Solution().backspaceCompare('ab#c', 'ad#c'), true)
console.log(new Solution().backspaceCompare('ab##', 'c#d#'), true)
console.log(new Solution().backspaceCompare('a#c', 'b'), false)
console.log(new Solution().backspaceCompare('xywrrmp', 'xywrrmu#p'), true)
console.log(new Solution().backspaceCompare('nzp#o#g', 'b#nzp#o#g'), true)
console.log(new Solution().backspaceCompare('bxj##tw', 'bxo#j##tw'), true)
console.log(new Solution().backspaceCompare('y#fo##f', 'y#f#o##f'), true)
console.log(new Solution().backspaceCompare('bxj##tw', 'bxj###tw'), false)
console.log(new Solution().backspaceCompare('rheyggodcclgstf', '#rheyggodcclgstf'), true)
console.log(new Solution().backspaceCompare('hd#dp#czsp#####', 'hd#dp#czsp#######'), false)