import { MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n)
    *     O(nlogk) -> O(nlog26) -> O(n)
    *     n: text length
    *     k: unique letter count
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: heap
    *     A: iteration
    * @param {string} text
    * @return {string}
    */
   reorganizeString(text) {
      const letterFreq = new Map();
      const letterHeap = new MaxPriorityQueue(x => x[0]);
      const newString = [];

      for (const letter of text) {
         letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);
      }

      for (const [letter, frequency] of letterFreq.entries()) {
         letterHeap.enqueue([frequency, letter])
      }

      let prevFreq = 0;
      let prevLetter = '';
      while (letterHeap.size()) {
         const [frequency, letter] = letterHeap.dequeue();
         if (prevFreq) {
            letterHeap.enqueue([prevFreq, prevLetter])
         }
         newString.push(letter);
         prevLetter = letter;
         prevFreq = frequency - 1;
      }
      return prevFreq ? '' : newString.join('')
   };
}


const reorganizeString = new Solution().reorganizeString;
console.log(new Solution().reorganizeString('aab') === 'aba')
console.log(new Solution().reorganizeString('aaab') === '')
console.log(new Solution().reorganizeString('kkkkzrkatkwpkkkktrq') === 'ktkrkpktkrkqkzkwkak')
