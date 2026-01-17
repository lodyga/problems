import { MaxPriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap
    *     A: iteration
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
      const change = money - twoChocks;
      return change >= 0 ? change : money
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap
    *     A: greedy
    * @param {number[]} prices
    * @param {number} money
    * @return {number}
    */
   buyChoco(prices, money) {
      const chocks = [101, 101];
      for (const price of prices) {
         if (price < chocks[0]) {
            chocks[1] = chocks[0];
            chocks[0] = price;
         }
         else if (price < chocks[1])
            chocks[1] = price;
      }

      const change = money - chocks[0] - chocks[1]
      return change >= 0 ? change : money
   };
}


const buyChoco = new Solution().buyChoco;
console.log(new Solution().buyChoco([1, 2, 2], 3) === 0)
console.log(new Solution().buyChoco([3, 2, 3], 3) === 3)
