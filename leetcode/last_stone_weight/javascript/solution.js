import { MaxPriorityQueue } from '@datastructures-js/priority-queue';

class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[]} stones
    * @return {number}
    */
   lastStoneWeight(stones) {
      const stoneHeap = new MaxPriorityQueue();
      stones.forEach(stone => stoneHeap.enqueue(stone));

      while (stoneHeap.size()) {
         const smashedStone = stoneHeap.dequeue() - stoneHeap.dequeue();
         if (smashedStone)
            stoneHeap.enqueue(smashedStone);
      }
      return stoneHeap.isEmpty() ? 0 : stoneHeap.dequeue()
   };
}
const lastStoneWeight = new Solution().lastStoneWeight;


import { MaxHeap } from '@datastructures-js/heap';

class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[]} stones
    * @return {number}
    */
   lastStoneWeight(stones) {
      const stoneHeap = MaxHeap.heapify(stones);

      while (stoneHeap.size()) {
         const smashedStone = stoneHeap.pop() - stoneHeap.pop();
         if (smashedStone)
            stoneHeap.push(smashedStone);
      }
      return stoneHeap.isEmpty() ? 0 : stoneHeap.pop()
   };
}


console.log(new Solution().lastStoneWeight([1]) === 1)
console.log(new Solution().lastStoneWeight([1, 1]) === 0)
console.log(new Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) === 1)