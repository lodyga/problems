import { PriorityQueue, MinPriorityQueue } from '@datastructures-js/priority-queue';


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[][]} tasks
    * @return {number[]}
    */
   getOrder(tasks) {
      const enqueuedTasks = new PriorityQueue((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]);
      //tasks.forEach((task, index) => enqueuedTasks.push([...task, index]));
      for (let index = 0; index < tasks.length; index++) {
         enqueuedTasks.enqueue([...tasks[index], index]);
      }

      const processingTasks = new PriorityQueue((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]);
      let timeStamp = enqueuedTasks.front()[0];
      const order = [];

      while (
         enqueuedTasks.size() ||
         processingTasks.size()
      ) {
         while (
            enqueuedTasks.size() &&
            enqueuedTasks.front()[0] <= timeStamp
         ) {
            const [_, processing, index] = enqueuedTasks.pop()
            processingTasks.enqueue([processing, index]);
         }
         if (processingTasks.size()) {
            const [processing, index] = processingTasks.pop()
            order.push(index);
            timeStamp += processing;
         } else {
            timeStamp = enqueuedTasks.front()[0];
         }
      }
      return order
   };
}
const getOrder = new Solution().getOrder;


import { Heap, MinHeap } from '@datastructures-js/heap';


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[][]} tasks
    * @return {number[]}
    */
   getOrder(tasks) {
      const enqueuedTasks = new Heap((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0])
      tasks.forEach((task, index) => enqueuedTasks.push([...task, index]));
      const processingTasks = new Heap((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0])
      let timeStamp = enqueuedTasks.top()[0];
      const order = [];

      while (
         enqueuedTasks.size() ||
         processingTasks.size()
      ) {
         while (
            enqueuedTasks.size() &&
            enqueuedTasks.top()[0] <= timeStamp
         ) {
            const [_, processing, index] = enqueuedTasks.pop()
            processingTasks.push([processing, index]);
         }
         if (processingTasks.size()) {
            const [processing, index] = processingTasks.pop()
            order.push(index);
            timeStamp += processing;
         } else {
            timeStamp = enqueuedTasks.top()[0];
         }
      }
      return order
   };
}
const getOrder = new Solution().getOrder;


console.log(new Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]), [0, 2, 3, 1])
console.log(new Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]), [4, 3, 2, 0, 1])
console.log(new Solution().getOrder([[1000000000, 1000000000]]), [0])