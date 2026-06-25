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
      const taskFreq = Array(26).fill(0);
      const taskHeap = new MaxPriorityQueue();
      const idleTasks = new Queue();
      let timestamp = 0;

      for (const task of tasks) {
         const idx = task.charCodeAt(0) - 'A'.charCodeAt(0);
         taskFreq[idx]++;
      }

      for (const val of taskFreq) {
         if (val) {
            taskHeap.push(val);
         }
      }

      while (!taskHeap.isEmpty() || !idleTasks.isEmpty()) {
         if (
            !idleTasks.isEmpty()
            && idleTasks.front()[0] <= timestamp
         ) {
            const [, task] = idleTasks.pop();
            taskHeap.push(task);
         }

         if (!taskHeap.isEmpty()) {
            const task = taskHeap.pop() - 1;

            if (task) {
               idleTasks.push([timestamp + cooldown + 1, task])
            }
         }

         timestamp++;
      }

      return timestamp;
   }
}


const leastInterval = new Solution().leastInterval;
console.log(new Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2) === 8)
console.log(new Solution().leastInterval(['A', 'C', 'A', 'B', 'D', 'B'], 1) === 6)
console.log(new Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 3) === 10)
console.log(new Solution().leastInterval(['B', 'C', 'D', 'A', 'A', 'A', 'A', 'G'], 1) === 8)
