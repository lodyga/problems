import { MinPriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(k)
    * Tags: heap
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   findKthLargest(nums, k) {
      const minHeap = new MinPriorityQueue();

      for (const num of nums) {
         minHeap.enqueue(num);
         if (minHeap.size() > k) {
            minHeap.dequeue();
         }
      }
      return minHeap.front()
   };
}


const findKthLargest = new Solution().findKthLargest;
console.log(new Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) === 5)
console.log(new Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) === 4)
