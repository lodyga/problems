import { Deque } from "@datastructures-js/deque";


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: DFS with memoization (DP on DAG)
    *     Model: graph
    * @param {number} n
    * @param {number} headID
    * @param {number[]} managers
    * @param {number[]} directInformTime
    * @return {number}
    */
   numOfMinutes = (n, headId, managers, directInformTime) => {
      // Total indirect information time.
      const memo = Array(n).fill(-1);
      memo[headId] = directInformTime[headId];

      const dfs = (id) => {
         if (memo[id] !== -1) {
            return memo[id]
         }

         memo[id] = directInformTime[id] + dfs(managers[id]);
         return memo[id]
      }

      for (let id = 0; id < n; id++) {
         dfs(id);
      }

      return Math.max(...memo)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: BFS
    *     Model: graph
    * @param {number} n
    * @param {number} headID
    * @param {number[]} managers
    * @param {number[]} directInformTime
    * @return {number}
    */
   numOfMinutes = (n, headID, managers, directInformTime) => {
      const adjs = new Map(managers.map((_, index) => [index, []]));

      for (let emp = 0; emp < managers.length; emp++) {
         const manager = managers[emp];
         if (manager === -1)
            continue
         adjs.get(manager).push(emp);
      }

      const bfs = (managerId) => {
         let res = 0;
         const deque = new Deque([[managerId, directInformTime[managerId]]]);

         while (deque.size()) {
            const [managerId, time] = deque.popFront();
            res = Math.max(res, time);

            for (const empId of adjs.get(managerId))
               deque.pushBack([empId, time + directInformTime[empId]])
         }
         return res
      }
      return bfs(headID)
   };
}

const numOfMinutes = new Solution().numOfMinutes;
console.log(new Solution().numOfMinutes(1, 0, [-1], [0]) === 0)
console.log(new Solution().numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) === 1)
