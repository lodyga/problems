import { MaxPriorityQueue } from '@datastructures-js/priority-queue';
import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(n)
    *     O(nlogn) -> log26 => const ->  O(n)
    * Auxiliary space complexity: O(1)
    *     O(26) -> O(1)
    * Tags: heap, queue
    * @param {string[]} tasks
    * @param {number} cooldown
    * @return {number}
    */
   leastInterval(tasks, cooldown) {
      const taskFrequency = new Map();
      for (const task of tasks) {
         taskFrequency.set(task, (taskFrequency.get(task) || 0) + 1);
      }
      const taskHeap = MaxPriorityQueue.fromArray([...taskFrequency.values()]);
      let taskLength = 0;
      const queue = new Queue();

      while (taskHeap.size() || queue.size()) {
         while (queue.size() && queue.front()[0] === taskLength) {
            const [_, frequency] = queue.pop();
            taskHeap.push(frequency);
         }
         if (taskHeap.size()) {
            const frequency = taskHeap.pop() - 1;
            if (frequency) {
               queue.push([taskLength + cooldown + 1, frequency])
            }
         }
         taskLength++;
      }
      return taskLength
   };
}
const leastInterval = new Solution().leastInterval;


console.log(new Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2), 8)  // A -> B -> idle -> A -> B -> idle -> A -> B
console.log(new Solution().leastInterval(['A', 'C', 'A', 'B', 'D', 'B'], 1), 6)  // A -> B -> C -> D -> A -> B
console.log(new Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 3), 10)  // A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B