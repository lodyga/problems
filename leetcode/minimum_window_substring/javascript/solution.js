class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: sliding window
    * @param {string} text
    * @param {string} word
    * @return {string}
    */
   minWindow(text, word) {
      const pattern = new Map();
      for (const letter of word) {
         pattern.set(letter, (pattern.get(letter) || 0) + 1);
      }

      const window = new Map();
      let left = 0;
      let start = 0;
      let subsringLength = text.length + 1;
      let neededMatch = pattern.size;

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];

         if (pattern.has(letter)) {
            window.set(letter, (window.get(letter) || 0) + 1);
            if (window.get(letter) === pattern.get(letter)) {
               neededMatch--;
            }
         }

         while (neededMatch === 0) {
            if (right - left + 1 < subsringLength) {
               subsringLength = right - left + 1;
               start = left;
            }
            const leftLetter = text[left];
            if (pattern.has(leftLetter)) {
               if (window.get(leftLetter) === pattern.get(leftLetter)) {
                  neededMatch++;
               }
               window.set(leftLetter, window.get(leftLetter) - 1);
            }
            left++;
         }
      }
      return subsringLength === text.length + 1 ? '' : text.slice(start, start + subsringLength)
   };
}
const minWindow = new Solution().minWindow;


console.log(new Solution().minWindow('accbca', 'ab') === 'bca')
console.log(new Solution().minWindow('ADOBECODEBANC', 'ABC') === 'BANC')
console.log(new Solution().minWindow('a', 'a') === 'a')
console.log(new Solution().minWindow('a', 'aa') === '')
console.log(new Solution().minWindow('a', 'b') === '')
console.log(new Solution().minWindow('ab', 'b') === 'b')
console.log(new Solution().minWindow('bba', 'ab') === 'ba')
console.log(new Solution().minWindow('abc', 'a') === 'a')
console.log(new Solution().minWindow('jwsdrkqzrthzysvqqazpfnulprulwmwhiqlbcdduxktxepnurpmxegktzegxscfbusexvhruumrydhvvyjucpeyrkeodjvgdnkalutfoizoliliguckmikdtpryanedcqgpkzxahwrvgcdoxiylqjolahjawpfbilqunnvwlmtrqxfphgaxroltyuvumavuomodblbnzvequmfbuganwliwidrudoqtcgyeuattxxlrlruhzuwxieuqhnmndciikhoehhaeglxuerbfnafvebnmozbtdjdo', 'qruzywfhkcbovewle') === 'vequmfbuganwliwidrudoqtcgyeuattxxlrlruhzuwxieuqhnmndciik')