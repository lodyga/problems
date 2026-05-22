class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: two pointers
    * @param {string} text1
    * @param {string} text2
    * @return {boolean}
    */
   backspaceCompare(text1, text2) {
      let idx1 = text1.length - 1;
      let idx2 = text2.length - 1
      let back1 = 0;
      let back2 = 0;

      while (idx1 > -1 || idx2 > -1) {
         while (
            idx1 > -1 &&
            (text1[idx1] == "#" || back1)
         ) {
            back1 += text1[idx1] === "#" ? 1 : -1;
            idx1--;
         }

         while (
            idx2 > -1 &&
            (text2[idx2] === "#" || back2)
         ) {
            back2 += text2[idx2] === "#" ? 1 : -1;
            idx2--;
         }

         if (idx1 === -1 && idx2 === -1)
            return true

         if (text1[idx1] !== text2[idx2])
            return false

         idx1--;
         idx2--;
      }
      
      return (idx1 === -1 && idx2 === -1);
   }
}


const backspaceCompare = new Solution().backspaceCompare;
console.log(new Solution().backspaceCompare('ab#c', 'ad#c') === true)
console.log(new Solution().backspaceCompare('ab##', 'c#d#') === true)
console.log(new Solution().backspaceCompare('a#c', 'b') === false)
console.log(new Solution().backspaceCompare('xywrrmp', 'xywrrmu#p') === true)
console.log(new Solution().backspaceCompare('nzp#o#g', 'b#nzp#o#g') === true)
console.log(new Solution().backspaceCompare('bxj##tw', 'bxo#j##tw') === true)
console.log(new Solution().backspaceCompare('y#fo##f', 'y#f#o##f') === true)
console.log(new Solution().backspaceCompare('bxj##tw', 'bxj###tw') === false)
console.log(new Solution().backspaceCompare('rheyggodcclgstf', '#rheyggodcclgstf') === true)
console.log(new Solution().backspaceCompare('hd#dp#czsp#####', 'hd#dp#czsp#######') === false)
console.log(new Solution().backspaceCompare('a', 'aa#a') === false)
