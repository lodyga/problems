import { PriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap
    *     A: sorting
    * @param {number[][]} tasks
    * @return {number[]}
    */
   getOrder(tasks) {
      const data = tasks.map(([enqTime, duration], id) => [enqTime, duration, id]);
      const sortBy = (a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]
      data.sort(sortBy);
      let index = 0;
      let time = data[0][0];
      const taskHeap = new PriorityQueue(sortBy);
      const order = [];

      while (
         index < data.length || 
         taskHeap.size()
      ) {
         while (
            index < data.length && 
            data[index][0] <= time
         ) {
            const [, duration, id] = data[index];
            taskHeap.enqueue([duration, id]);
            index++;
         }
         
         if (taskHeap.size()) {
            const [duration, id] = taskHeap.dequeue();
            time += duration;
            order.push(id);
         } else {
            // time fast forward
            time = data[index][0];
         }
      }
      return order
   };
}


const getOrder = new Solution().getOrder;
console.log(new Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]).toString() === [0, 2, 3, 1].toString())
console.log(new Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]).toString() === [4, 3, 2, 0, 1].toString())
console.log(new Solution().getOrder([[1000000000, 1000000000]]).toString() === [0].toString())
console.log(new Solution().getOrder([[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]]).toString() === [6, 1, 2, 9, 4, 10, 0, 11, 5, 13, 3, 8, 12, 7].toString())
