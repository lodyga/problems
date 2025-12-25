import { MaxPriorityQueue } from '@datastructures-js/priority-queue';
import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(n)
    *     O(nlogk) -> O(nlog26) -> O(n)
    *     n: task count
    *     k: letter count
    * Auxiliary space complexity: O(1)
    *     O(k)
    * Tags: 
    *     DS: heap, queue
    *     A: iteration
    * @param {string[]} tasks
    * @param {number} cooldown
    * @return {number}
    */
   leastInterval(tasks, cooldown) {
      const taskHeap = MaxPriorityQueue.fromArray();
      const taskFreq = new Map();
      for (const task of tasks) {
         taskFreq.set(task, (taskFreq.get(task) || 0) + 1);
      }

      const taskQueue = new Queue([...taskFreq.values()].map(freq => [0, freq]));
      let time = 0;
      while (
         taskQueue.size() ||
         taskHeap.size()
      ) {
         time++;

         while (
            taskQueue.size() &&
            taskQueue.front()[0] < time
         ) {
            const [_, freq] = taskQueue.pop();
            taskHeap.push(freq);
         }
         if (taskHeap.size() === 0)
            continue

         const freq = taskHeap.pop() - 1;
         if (freq) {
            taskQueue.push([time + cooldown, freq])
         }
      }
      return time
   };
}


const leastInterval = new Solution().leastInterval;
console.log(new Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2) === 8)
console.log(new Solution().leastInterval(['A', 'C', 'A', 'B', 'D', 'B'], 1) === 6)
console.log(new Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 3) === 10)
console.log(new Solution().leastInterval(['B', 'C', 'D', 'A', 'A', 'A', 'A', 'G'], 1) === 8)
