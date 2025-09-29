import { MinPriorityQueue, PriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(nlogn + mlogm)
    *     n: interval length
    *     m: queries length
    * Auxiliary space complexity: O(n + m)
    * Tags: intervals, heap
    * @param {number[][]} intervals
    * @param {number[]} queries
    * @return {number[]}
    */
   minInterval(intervals, queries) {
      intervals.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      const sortedQueries = [...queries].sort((a, b) => a - b);
      const intervalHeap = new MinPriorityQueue(x => x[0]);
      const minIntervals = new Map();
      let index = 0;

      for (const query of sortedQueries) {
         while (
            index < intervals.length &&
            intervals[index][0] <= query
         ) {
            const [start, end] = intervals[index];
            intervalHeap.enqueue([end - start + 1, end]);
            index++
         }
         while (
            !intervalHeap.isEmpty() &&
            intervalHeap.front()[1] < query
         )
            intervalHeap.dequeue();

         minIntervals.set(query, !intervalHeap.isEmpty() ? intervalHeap.front()[0] : -1)
      }
      return queries.map((query) => minIntervals.get(query))
   };
}
const minInterval = new Solution().minInterval;


console.log(new Solution().minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]), [3, 3, 1, 4])
console.log(new Solution().minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]), [2, -1, 4, 6])