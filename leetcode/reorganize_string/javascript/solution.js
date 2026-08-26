import { MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n)
    *     O(nlogk) -> O(nlog26) -> O(n)
    *     n: text length
    *     k: unique letter count
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: heap, string
    *     A: iteration
    * @param {string} text
    * @return {string}
    */
   reorganizeString(text) {
      const letterFreq = new Map();
      const letterHeap = new MaxPriorityQueue(x => x[0]);
      const res = [];
      let prevLetter;
      let prevFreq = 0;

      for (const letter of text) {
         letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);
      }

      for (const [letter, freq] of letterFreq.entries()) {
         letterHeap.enqueue([freq, letter])
      }


      while (!letterHeap.isEmpty()) {
         const [freq, letter] = letterHeap.pop();
         res.push(letter);

         if (prevFreq) {
            letterHeap.push([prevFreq, prevLetter]);
         }

         prevLetter = letter;
         prevFreq = freq - 1;
      }

      return prevFreq === 0 ? res.join('') : '';
   }
}


const reorganizeString = new Solution().reorganizeString;
console.log(new Solution().reorganizeString('aab') === 'aba')
console.log(new Solution().reorganizeString('aaab') === '')
console.log(new Solution().reorganizeString('kkkkzrkatkwpkkkktrq') === 'ktkrkpktkrkqkzkwkak')
