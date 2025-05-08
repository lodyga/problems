import { MaxPriorityQueue } from '@datastructures-js/priority-queue';

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: priority queue
    * @param {number[]} prices
    * @param {number} money
    * @return {number}
    */
   buyChoco(prices, money) {
      const maxHeap = new MaxPriorityQueue();
      for (const price of prices) {
         maxHeap.enqueue(price);
         if (maxHeap.size() > 2) {
            maxHeap.dequeue()
         }
      }
      const twoChocks = maxHeap.dequeue() + maxHeap.dequeue();
      const leftover = money - twoChocks;

      return leftover >= 0 ? leftover : money
   };
}
const buyChoco = new Solution().buyChoco;



import { MinHeap } from '@datastructures-js/heap';


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: heap
    * @param {number[]} prices
    * @param {number} money
    * @return {number}
    */
   buyChoco(prices, money) {
      const priceHeap = MinHeap.heapify(prices);
      const twoChocks = priceHeap.pop() + priceHeap.pop();
      const leftover = money - twoChocks;

      return leftover >= 0 ? leftover : money
   };
}
const buyChoco = new Solution().buyChoco;


console.log(new Solution().buyChoco([1, 2, 2], 3), 0)
console.log(new Solution().buyChoco([3, 2, 3], 3), 3)