class Solution {
   /**
    * Time complexity: O(n)
    *     O(nlogk) -> O(nlog26) -> O(n)
    *     n: text.length
    *     k: unique_chars.count
    * Auxiliary space complexity: O(1)
    * Tags: heap
    * @param {string} text
    * @return {string}
    */
   reorganizeString(text) {
      const letterFrequency = new Map();  // {letter: frequency}
      const letterHeap = new MaxPriorityQueue(x => x[0]);  // [[frequency, letter], ...]
      const reorganizedString = [];

      for (const letter of text) {
         letterFrequency.set(letter, (letterFrequency.get(letter) || 0) + 1);
      }

      for (const [letter, frequency] of letterFrequency.entries()) {
         letterHeap.enqueue([frequency, letter])
      }

      let prevLetter = '';
      let prevFrequency = 0;
      while (letterHeap.size()) {
         let [frequency, letter] = letterHeap.dequeue();
         if (prevFrequency) {
            letterHeap.enqueue([prevFrequency, prevLetter])
         }
         frequency--;
         reorganizedString.push(letter);
         prevLetter = letter;
         prevFrequency = frequency;
      }
      return prevFrequency ? '' : reorganizedString.join('')
   };
}
const reorganizeString = new Solution().reorganizeString;


console.log(new Solution().reorganizeString('aab') == 'aba')
console.log(new Solution().reorganizeString('aaab') == '')
console.log(new Solution().reorganizeString('kkkkzrkatkwpkkkktrq') == 'ktkrkpktkrkqkzkwkak')