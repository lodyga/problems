class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dfs, recursion, graph
    * @param {number} n
    * @param {number} headID
    * @param {number[]} managers
    * @param {number[]} directInformTime
    * @return {number}
    */
   numOfMinutes = (n, headID, managers, directInformTime) => {
      const adjs = new Map(managers.map((_, index) => [index, []]));
      for (let employee = 0; employee < managers.length; employee++) {
         const manager = managers[employee];
         if (manager === -1)
            continue
         adjs.get(manager).push(employee);
      }

      const dfs = (manager) => {
         if (indirectInformTime.has(manager))
            return indirectInformTime.get(manager)

         let informTime = 0;
         for (const employee of adjs.get(manager))
            informTime = Math.max(
               informTime,
               dfs(employee) + directInformTime[manager]
            )
         indirectInformTime.set(manager, informTime);
         return informTime
      }

      const indirectInformTime = new Map();
      for (let employee = 0; employee < n; employee++) {
         if (adjs.get(employee).length === 0)
            indirectInformTime.set(employee, 0)
      }
      for (let employee = 0; employee < n; employee++)
         dfs(employee);

      return indirectInformTime.get(headID)
   };
}


import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: bfs, iteration, queue, graph
    * @param {number} n
    * @param {number} headID
    * @param {number[]} managers
    * @param {number[]} directInformTime
    * @return {number}
    */
   numOfMinutes = (n, headID, managers, directInformTime) => {
      const adjs = new Map(managers.map((_, index) => [index, []]));
      for (let employee = 0; employee < managers.length; employee++) {
         const manager = managers[employee];
         if (manager === -1)
            continue
         adjs.get(manager).push(employee);
      }

      const bfs = (manager) => {
         let totalTime = 0;
         const queue = new Queue([[manager, 0]]);

         while (!queue.isEmpty()) {
            const [manager, time] = queue.dequeue();
            totalTime = Math.max(totalTime, time);

            for (const employee of adjs.get(manager))
               queue.enqueue([employee, time + directInformTime[manager]])
         }
         return totalTime
      }
      return bfs(headID)
   };
}

const numOfMinutes = new Solution().numOfMinutes;
console.log(new Solution().numOfMinutes(1, 0, [-1], [0]) === 0)
console.log(new Solution().numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) === 1)