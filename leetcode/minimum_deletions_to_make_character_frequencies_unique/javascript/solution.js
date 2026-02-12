import { MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap, array
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   minDeletions(text) {
      const letterFreq = Array(26).fill(0);
      let res = 0;
      const freqHeap = new MaxPriorityQueue();

      for (let index = 0; index < text.length; index++) {
         const letterInd = text.charCodeAt(index) - 'a'.charCodeAt(0);
         letterFreq[letterInd] += 1;
      }

      for (const freq of letterFreq) {
         if (freq) {
            freqHeap.enqueue(freq);
         }
      }

      let prevFreq = freqHeap.front() + 1;

      while (freqHeap.size()) {
         const freq = freqHeap.dequeue();

         if (prevFreq === freq) {
            freqHeap.enqueue(prevFreq - 1);
            res++;
         } else {
            prevFreq = freq;
         }

         if (prevFreq === 1) {
            res += freqHeap.size();
            break
         }
      }

      return res
   };
}


const minDeletions = new Solution().minDeletions;
console.log(new Solution().minDeletions('aab') === 0)
console.log(new Solution().minDeletions('aaabbbcc') === 2)
console.log(new Solution().minDeletions('ceabaacb') === 2)
console.log(new Solution().minDeletions('abcabc') === 3)
console.log(new Solution().minDeletions('bbcebab') === 2)
