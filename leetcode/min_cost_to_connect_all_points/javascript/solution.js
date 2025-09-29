import { PriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(n2logn)
    * Auxiliary space complexity: O(n2)
    * Tags: bfs, iteration, graph, msp
    * Minimum Spanning Tree, Prim's alg
    * @param {number[][]} points
    * @return {number}
    */
   minCostConnectPoints(points) {
      const vertex_size = points.length
      // frontier map
      // {vertex: {(adjacent vertex, distance), ...}, ...}
      const adjs = new Map();
      for (let vertex = 0; vertex < vertex_size; vertex++) {
         adjs.set(vertex, [])
      }
      for (let index = 0; index < vertex_size; index++) {
         const [xa, ya] = points[index];
         for (let index2 = 0; index2 < vertex_size; index2++) {
            const [xb, yb] = points[index2];
            if (index > index2) {
               const distance = Math.abs(xa - xb) + Math.abs(ya - yb);
               adjs.get(index).push([index2, distance]);
               adjs.get(index2).push([index, distance]);
            }
         }
      }
      
      const closestVertex = new PriorityQueue((a, b) => a[0] - b[0]);
      closestVertex.enqueue([0, 0]);
      let totalDistance = 0;
      const visited = new Set();

      while (visited.size < vertex_size) {
         const [distance, vertex] = closestVertex.dequeue();
         if (visited.has(vertex))
            continue
         visited.add(vertex);
         totalDistance += distance;

         for (const [adjVertex, adjDistance] of adjs.get(vertex)) {
            if (!visited.has(adjVertex))
               closestVertex.enqueue([adjDistance, adjVertex])
         }
      }
      return totalDistance
   };
}


const minCostConnectPoints = new Solution().minCostConnectPoints;
console.log(new Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20)
console.log(new Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18)