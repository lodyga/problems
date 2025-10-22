import { PriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O((k+n)logn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[]} numbers
    * @param {number} k
    * @param {number} multiplier
    * @return {number[]}
    */
   getFinalState(numbers, k, multiplier) {
      const numberHeap = new PriorityQueue((a, b) => (a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]));
      
      for (let index = 0; index < numbers.length; index++) {
         const number = numbers[index];
         numberHeap.enqueue([number, index]);
      }

      for (let index = 0; index < k; index++) {
         const [_, index] = numberHeap.dequeue();
         numbers[index] *= multiplier;
         numberHeap.enqueue([numbers[index], index])
      }

      return numbers
   };
}


const getFinalState = new Solution().getFinalState;
console.log(new Solution().getFinalState([2, 1, 3, 5, 6], 5, 2), [8, 4, 6, 5, 6])
console.log(new Solution().getFinalState([1, 2], 3, 4), [16, 8])