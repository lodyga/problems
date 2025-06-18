import { MinPriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(k)
    * Tags: heap
    * @param {number[]} numbers
    * @param {number} k
    * @return {number}
    */
   findKthLargest(numbers, k) {
      const minHeap = new MinPriorityQueue();

      for (const number of numbers) {
         minHeap.enqueue(number)
         if (minHeap.size() > k) {
            minHeap.dequeue()
         }
      }
      return minHeap.dequeue()
   };
}


console.log(new Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) === 5)
console.log(new Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) === 4)