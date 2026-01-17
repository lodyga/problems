import { MaxPriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(n + klogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[]} gifts
    * @param {number} k
    * @return {number}
    */
   pickGifts(gifts, k) {
      const giftHeap = new MaxPriorityQueue();
      gifts.forEach(gift => giftHeap.enqueue(gift));
      for (let index = 0; index < k; index++) {
         const number = giftHeap.dequeue();
         giftHeap.enqueue(Math.floor(number**0.5));
      }
      return giftHeap.toArray().reduce((total, value) => total + value, 0)
   };
}


const pickGifts = new Solution().pickGifts;
console.log(new Solution().pickGifts([25, 64, 9, 4, 100], 4) === 29)
console.log(new Solution().pickGifts([1, 1, 1, 1], 4) === 4)