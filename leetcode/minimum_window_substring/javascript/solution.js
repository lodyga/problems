class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: hash map
    *     A: sliding window
    * @param {string} text
    * @param {string} word
    * @return {string}
    */
   minWindow(text, word) {
      const pattern = new Map();
      for (const letter of word)
         pattern.set(letter, (pattern.get(letter) || 0) + 1);

      let left = 0;
      const window = new Map();
      let start = -1;
      let shortest = text.length;
      let needed = pattern.size;

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];
         window.set(letter, (window.get(letter) || 0) + 1);

         if (window.get(letter) === pattern.get(letter))
            needed--;

         if (needed)
            continue

         while (needed === 0) {
            const windowLength = right - left + 1;
            if (windowLength <= shortest) {
               shortest = windowLength;
               start = left;
            }
            const leftLetter = text[left];
            if (window.get(leftLetter) === pattern.get(leftLetter)) {
               needed++;
            }
            window.set(leftLetter, window.get(leftLetter) - 1);
            left++;
         }
      }
      return text.slice(start, start + shortest)
   };
}


const minWindow = new Solution().minWindow;
console.log(new Solution().minWindow('a', 'a') === 'a')
console.log(new Solution().minWindow('a', 'aa') === '')
console.log(new Solution().minWindow('ab', 'ab') === 'ab')
console.log(new Solution().minWindow('a', 'b') === '')
console.log(new Solution().minWindow('ab', 'b') === 'b')
console.log(new Solution().minWindow('bba', 'ab') === 'ba')
console.log(new Solution().minWindow('abc', 'a') === 'a')
console.log(new Solution().minWindow('accbca', 'ab') === 'bca')
console.log(new Solution().minWindow('ADOBECODEBANC', 'ABC') === 'BANC')
console.log(new Solution().minWindow('jwsdrkqzrthzysvqqazpfnulprulwmwhiqlbcdduxktxepnurpmxegktzegxscfbusexvhruumrydhvvyjucpeyrkeodjvgdnkalutfoizoliliguckmikdtpryanedcqgpkzxahwrvgcdoxiylqjolahjawpfbilqunnvwlmtrqxfphgaxroltyuvumavuomodblbnzvequmfbuganwliwidrudoqtcgyeuattxxlrlruhzuwxieuqhnmndciikhoehhaeglxuerbfnafvebnmozbtdjdo', 'qruzywfhkcbovewle') === 'vequmfbuganwliwidrudoqtcgyeuattxxlrlruhzuwxieuqhnmndciik')
