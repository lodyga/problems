import { MaxPriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(n + klogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap
    *     A: iteration
    * @param {number[]} gifts
    * @param {number} k
    * @return {number}
    */
   pickGifts(gifts, k) {
      const giftHeap = new MaxPriorityQueue();
      gifts.forEach(gift => giftHeap.enqueue(gift));
      
      for (let index = 0; index < k; index++) {
         const gift = giftHeap.dequeue();
         giftHeap.enqueue(Math.floor(gift ** 0.5));
      }
      return giftHeap.toArray().reduce((sum, num) => sum + num, 0)
   };
}


const pickGifts = new Solution().pickGifts;
console.log(new Solution().pickGifts([25, 64, 9, 4, 100], 4) === 29)
console.log(new Solution().pickGifts([1, 1, 1, 1], 4) === 4)
