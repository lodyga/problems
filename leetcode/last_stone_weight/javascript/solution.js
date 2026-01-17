import { MaxPriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *    DS: heap
    *    A: heap
    * @param {number[]} stones
    * @return {number}
    */
   lastStoneWeight(stones) {
      const stoneHeap = new MaxPriorityQueue();
      stones.forEach(stone => stoneHeap.enqueue(stone));

      while (stoneHeap.size() > 1) {
         const diff = stoneHeap.dequeue() - stoneHeap.dequeue();
         if (diff)
            stoneHeap.enqueue(diff);
      }
      return stoneHeap.size() ? stoneHeap.dequeue() : 0
   };
}


const lastStoneWeight = new Solution().lastStoneWeight;
console.log(new Solution().lastStoneWeight([1]) === 1)
console.log(new Solution().lastStoneWeight([1, 1]) === 0)
console.log(new Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) === 1)
