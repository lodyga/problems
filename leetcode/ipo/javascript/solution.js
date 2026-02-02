import { MinPriorityQueue, MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap
    *     A: greedy
    * @param {number} projectCount
    * @param {number} capital
    * @param {number[]} profits
    * @param {number[]} capital_list
    * @return {number}
    */
   findMaximizedCapital(projectCount, capital, profits, capital_list) {
      // min-heap((capital, profit), )
      const projectHeap = new MinPriorityQueue(project => project[0]);
      for (let index = 0; index < profits.length; index++) {
         projectHeap.enqueue([capital_list[index], profits[index]]);
      }

      // max-heap((profit), )
      const profitHeap = new MaxPriorityQueue();

      for (let i = 0; i < projectCount; i++) {
         while (
            projectHeap.size() &&
            projectHeap.front()[0] <= capital
         ) {
            const [, profit] = projectHeap.dequeue();
            profitHeap.enqueue(profit);
         }
         if (profitHeap.isEmpty())
            break

         capital += profitHeap.dequeue();
      }
      return capital
   };
}


const findMaximizedCapital = new Solution().findMaximizedCapital;
console.log(new Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) === 4)
console.log(new Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) === 6)
console.log(new Solution().findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) === 0)
