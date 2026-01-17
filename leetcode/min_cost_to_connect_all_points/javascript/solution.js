import { MinPriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(n2logn)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: heap, hash map, hash set
    *     A: greedy, MST, Prim
    *     Model: graph
    * @param {number[][]} points
    * @return {number}
    */
   minCostConnectPoints(points) {
      const N = points.length;
      // frontier map
      // {vertex: {(adjacent vertex, distance), ...}, ...}
      const adjVertices = new Map();
      for (let vertex = 0; vertex < N; vertex++) {
         adjVertices.set(vertex, [])
      }
      for (let u = 0; u < N; u++) {
         const [x1, y1] = points[u];

         for (let v = 0; v < N; v++) {
            const [x2, y2] = points[v];

            if (u > v) {
               const distance = Math.abs(x1 - x2) + Math.abs(y1 - y2);
               adjVertices.get(u).push([v, distance]);
               adjVertices.get(v).push([u, distance]);
            }
         }
      }

      const visited = Array(N).fill(false);
      let edgeCounter = 0;

      const helper = (vertex) => {
         let totalDistance = 0;
         const vertexHeap = new MinPriorityQueue(x => x[0]);
         vertexHeap.enqueue([0, vertex]);

         while (edgeCounter < N) {
            const [distance, vertex] = vertexHeap.dequeue();

            if (visited[vertex])
               continue
            visited[vertex] = true;
            edgeCounter++;
            totalDistance += distance;

            for (const [adjVertex, adjDistance] of adjVertices.get(vertex)) {
               if (!visited[adjVertex])
                  vertexHeap.enqueue([adjDistance, adjVertex])
            }
         }
         return totalDistance
      }
      return helper(0)
   };

   /**
    * Time complexity: O(V2logV)
    * Auxiliary space complexity: O(V2)
    * Tags:
    *     DS: heap, array
    *     A: DSU, MST, Kruskal
    *     Model: graph
    * @param {number[][]} points
    * @return {number}
    */
   minCostConnectPoints(points) {
      const N = points.length;
      const dsu = new DSU(N);
      // const edges = [];
      const edges = new MinPriorityQueue(x => x[0]);

      for (let u = 0; u < N; u++) {
         const [x1, y1] = points[u];
         for (let v = 0; v < N; v++) {
            const [x2, y2] = points[v];
            if (u > v) {
               const distance = Math.abs(x1 - x2) + Math.abs(y1 - y2)
               // edges.push([distance, u, v]);
               edges.enqueue([distance, u, v]);
            }
         }
      }

      let totalDistance = 0;
      // edges.sort((a, b) => a[0] - b[0]);

      let index = 0;
      while (dsu.components > 1) {
         // const [distance, u, v] = edges[index];
         const [distance, u, v] = edges.dequeue();
         if (dsu.union(u, v))
            totalDistance += distance
         index++;
      }
      return totalDistance
   };
}


class DSU {
   constructor(N) {
      this.size = Array(N).fill(1);
      this.parent = Array.from({ length: N }, (_, index) => index);
      this.components = N
   };

   find(vertex) {
      while (vertex !== this.parent[vertex]) {
         this.parent[vertex] = this.parent[this.parent[vertex]];
         vertex = this.parent[vertex];
      }
      return vertex
   };

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu == pv) {
         return false
      } else if (this.size[pu] >= this.size[pv]) {
         this.size[pu] += this.size[pv];
         this.parent[pv] = this.parent[pu];
         this.parent[v] = this.parent[pu];
      } else {
         this.size[pv] += this.size[pu];
         this.parent[pu] = this.parent[pv];
         this.parent[u] = this.parent[pv];
      }
      this.components--;
      return true
   };
}


const minCostConnectPoints = new Solution().minCostConnectPoints;
console.log(new Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) === 20)
console.log(new Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) === 18)
console.log(new Solution().minCostConnectPoints([[0, 0]]) === 0)
console.log(new Solution().minCostConnectPoints([[11, 12], [-9, 5], [-1, 5], [9, -8], [20, -17], [18, 19], [-1, 14], [16, 19], [2, 16], [14, 3], [1, -12], [19, 4], [5, -17], [-13, 6], [-4, 1], [-7, -16], [13, 7], [-20, -7], [20, -15]]) === 165)
