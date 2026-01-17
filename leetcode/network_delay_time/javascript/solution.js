import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(ElogV)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: heap, hash map, hash set, graph
    *     A: BFS, Dijkstra
    * @param {number[][]} times
    * @param {number} n
    * @param {number} k
    * @return {number}
    */
   networkDelayTime(times, n, k) {
      const nextVertices = new Map();

      for (let vertex = 0; vertex < n; vertex++) {
         nextVertices.set(vertex, []);
      }
      for (const [src, dst, time] of times) {
         nextVertices.get(src - 1).push([time, dst - 1]);
      }

      const visited = Array(n).fill(false);
      const minHeap = new MinPriorityQueue(vertex => vertex[0]);
      minHeap.enqueue([0, k - 1]);
      let maxDelay = 0;

      while (minHeap.size()) {
         const [delay, vertex] = minHeap.dequeue();
         if (visited[vertex])
            continue;
         visited[vertex] = true;
         maxDelay = Math.max(maxDelay, delay);

         for (const [nextWeight, nextVertex] of nextVertices.get(vertex)) {
            minHeap.enqueue([delay + nextWeight, nextVertex]);
         }
      }
      return visited.every(v => v === true) ? maxDelay : -1;
   };

   /**
    * Time complexity: O(V * E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: hash map, hash set, graph
    *     A: DFS
    * @param {number[][]} times
    * @param {number} n
    * @param {number} k
    * @return {number}
    */
   networkDelayTime(times, n, k) {
      const nextVertices = new Map();
      const delays = new Map();

      for (let vertex = 0; vertex < n; vertex++) {
         nextVertices.set(vertex, new Set());
         delays.set(vertex, 10 ** 4 + 1);
      }
      
      for (const [src, dst, time] of times) {
         nextVertices.set(src - 1, nextVertices.get(src - 1).add([dst - 1, time]));
      }

      const dfs = (vertex, delay) => {
         if (delays.get(vertex) <= delay)
            return

         delays.set(vertex, delay);

         for (const [nextVertex, nextWeight] of nextVertices.get(vertex)) {
            dfs(nextVertex, delay + nextWeight)
         }
      }

      dfs(k - 1, 0);

      let maxDelay = 0;
      for (const delay of delays.values()) {
         if (delay === 10 ** 4 + 1)
            return -1
         else if (delay > maxDelay)
            maxDelay = delay;
      }
      return maxDelay
   };
}


const networkDelayTime = new Solution().networkDelayTime;
console.log(new Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) === 2)
console.log(new Solution().networkDelayTime([[1, 2, 1]], 2, 1) === 1)
console.log(new Solution().networkDelayTime([[1, 2, 1]], 2, 2) === -1)
console.log(new Solution().networkDelayTime([[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], 4, 1) === 3)
console.log(new Solution().networkDelayTime([[1, 2, 1], [2, 3, 1]], 3, 2) === -1)
