import { MinPriorityQueue, MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number} projectCount
    * @param {number} currentCapital
    * @param {number[]} profits
    * @param {number[]} capital_list
    * @return {number}
    */
   findMaximizedCapital(projectCount, currentCapital, profits, capital_list) {
      const profCap = Array.from({ length: profits.length }, (_, index) => [profits[index], capital_list[index]]);
      // heap((profit, capital), )
      const entryHeap = new MinPriorityQueue((capital) => capital[1]);
      profCap.forEach((pair) => entryHeap.enqueue(pair));
      // heap((profit), )
      const profitHeap = new MaxPriorityQueue();

      for (let blank = 0; blank < projectCount; blank++) {
         while (
            !entryHeap.isEmpty() &&
            entryHeap.front()[1] <= currentCapital
         ) {
            const [profit, _] = entryHeap.dequeue();
            profitHeap.enqueue(profit);
         }
         if (profitHeap.isEmpty())
            break

         currentCapital += profitHeap.dequeue();
      }
      return currentCapital
   };
}


const findMaximizedCapital = new Solution().findMaximizedCapital;
console.log(new Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) === 4)
console.log(new Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) === 6)
console.log(new Solution().findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) === 0)