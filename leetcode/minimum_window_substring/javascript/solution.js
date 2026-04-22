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
      const window = new Map();
      let left = 0;
      let resLen = text.length + 1;
      let start = text.length;

      for (const letter of word)
         window.set(letter, (window.get(letter) || 0) - 1);

      let needed = window.size;

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];

         if (!window.has(letter)) {
            continue
         }

         window.set(letter, window.get(letter) + 1);

         if (window.get(letter) === 0) {
            needed--;
         }

         while (needed === 0) {
            if (right - left + 1 < resLen) {
               resLen = right - left + 1;
               start = left;
            }

            const leftLetter = text[left];

            if (window.has(leftLetter)) {
               if (window.get(leftLetter) === 0) {
                  needed++;
               }
               window.set(leftLetter, window.get(leftLetter) - 1);
            }
            left++;
         }
      }

      if (start === text.length) {
         return ''
      } else {
         return text.slice(start, start + resLen)
      }

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
