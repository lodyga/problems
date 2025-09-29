import { PriorityQueue, MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(ElogV)
    * Auxiliary space complexity: O(V + E)
    * Tags: bfs, iteration, graph
    * Dijkstra
    * @param {number[][]} times
    * @param {number} n
    * @param {number} k
    * @return {number}
    */
   networkDelayTime(times, n, k) {
      const nextVertices = new Map();
      const delays = Array(n).fill(0);

      for (let vertex = 1; vertex <= n; vertex++) {
         nextVertices.set(vertex, []);
         // nextVertices.set(vertex, new Set());
      }
      for (const [source, destination, time] of times) {
         nextVertices.get(source).push([destination, time]);
         // nextVertices.get(source).add([destination, time]);
      }

      const visited = new Set();
      const minHeap = new MinPriorityQueue((vertex) => vertex[0]);
      // const minHeap = new PriorityQueue((a, b) => a[0] - b[0]);
      minHeap.enqueue([0, k]);
      let maxDelay = 0;

      while (
         visited.size !== n &&
         !minHeap.isEmpty()
      ) {
         const [weight, vertex] = minHeap.dequeue();
         if (visited.has(vertex)) continue;
         // delays[vertex - 1] = weight;
         maxDelay = Math.max(maxDelay, weight);
         visited.add(vertex);

         for (const [nextVertex, nextWeight] of nextVertices.get(vertex)) {
            minHeap.enqueue([weight + nextWeight, nextVertex]);
         }
      }
      // return visited.size === n ? Math.max(...delays) : -1;
      return visited.size === n ? maxDelay : -1;
   };
}


class Solution2 {
   /**
    * Time complexity: O(V * E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph
    * DFS
    * @param {number[][]} times
    * @param {number} n
    * @param {number} k
    * @return {number}
    */
   networkDelayTime(times, n, k) {
      const delays = new Map();
      const nextVertices = new Map();

      for (let vertex = 1; vertex <= n; vertex++) {
         delays.set(vertex, 10 ** 4 + 1);
         nextVertices.set(vertex, new Set());
      }
      for (const [source, destination, time] of times) {
         nextVertices.set(source, nextVertices.get(source).add([destination, time]));
      }

      const dfs = (vertex, weight) => {
         if (delays.get(vertex) <= weight)
            return

         delays.set(vertex, weight);

         for (const [nextVertex, nextWeight] of nextVertices.get(vertex)) {
            dfs(nextVertex, weight + nextWeight)
         }
      }

      dfs(k, 0);

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