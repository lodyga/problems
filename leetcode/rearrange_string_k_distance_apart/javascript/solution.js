import { MaxPriorityQueue } from '@datastructures-js/priority-queue';
import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap, queue, array
    *     A: iteration
    * @param {string} text
    * @param {number} k
    * @return {string}
    */
   rearrangeString(text, k) {
      const a = 'a'.charCodeAt(0);
      const numFreq = Array(26).fill(0);
      // heap([(freq, letter, avaible), ])
      const topNumHeap = new MaxPriorityQueue(x => x[0]);
      const res = []
      // deque([(freq, letter, avaible), ])
      const coolQueue = new Queue();
      let timeStamp = 1;

      for (const letter of text) {
         const index = letter.charCodeAt(0) - a;
         numFreq[index] += 1;
      }

      for (let index = 0; index < 26; index++) {
         if (numFreq[index]) {
            topNumHeap.enqueue([numFreq[index], String.fromCharCode(index + a), 0]);
         }
      }

      while (timeStamp <= text.length) {
         while (coolQueue.size() && coolQueue.front()[2] <= timeStamp) {
            topNumHeap.enqueue(coolQueue.dequeue());
         }

         if (topNumHeap.isEmpty()) {
            return ''
         }

         const [freq, letter,] = topNumHeap.dequeue();
         res.push(letter);

         if (freq > 1) {
            coolQueue.enqueue([freq - 1, letter, timeStamp + k]);
         }

         timeStamp++;
      }

      return res.join('');
   }
};


const rearrangeString = new Solution().rearrangeString;
console.log(['abcabc', 'acbacb'].includes(new Solution().rearrangeString('aabbcc', 3)))
console.log([''].includes(new Solution().rearrangeString('aaabc', 3)))
console.log(['abacabcd', 'abcabcad'].includes(new Solution().rearrangeString('aaadbbcc', 2)))
