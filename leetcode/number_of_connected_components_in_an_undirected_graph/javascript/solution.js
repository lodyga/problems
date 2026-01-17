import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array (graph)
    *     A: multi-source DFS
    * @param {number} N
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(N, edges) {
      let components = 0;
      const visited = Array(N).fill(false);
      const adjs = new Map();

      for (let node = 0; node < N; node++) {
         adjs.set(node, []);
      }

      for (const [u, v] of edges) {
         adjs.get(u).push(v);
         adjs.get(v).push(u);
      }

      const dfs = (node) => {
         if (visited[node])
            return 0

         visited[node] = true;

         for (const adjNode of adjs.get(node))
            dfs(adjNode);

         return 1
      };

      for (let node = 0; node < N; node++) {
         components += dfs(node);
      }
      return components
   };

   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array (graph)
    *     A: multi-source BFS
    * @param {number} N
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(N, edges) {
      let components = 0;
      const visited = Array(N).fill(false);
      const adjs = new Map();

      for (let node = 0; node < N; node++) {
         adjs.set(node, []);
      }

      for (const [u, v] of edges) {
         adjs.get(u).push(v);
         adjs.get(v).push(u);
      }

      const bfs = (node) => {
         if (visited[node])
            return 0
         const queue = new Queue([node]);

         while (queue.size()) {
            const node = queue.dequeue();
            visited[node] = true;

            for (const adjNode of adjs.get(node))
               if (!visited[adjNode])
                  queue.enqueue(adjNode);
         }
         return 1
      };

      for (let node = 0; node < N; node++) {
         components += bfs(node);
      }
      return components
   };

   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array (graph)
    *     A: DSU
    * @param {number} N
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(N, edges) {
      const dsu = new DSU(N);
      for (const [u, v] of edges) {
         dsu.union(u, v);
      }
      return dsu.components
   };
}


class DSU {
   constructor(N) {
      this.size = Array(N).fill(1);
      this.parent = Array.from({ length: N }, (_, node) => node);
      this.components = N;
   }

   find(node) {
      while (node !== this.parent[node]) {
         this.parent[node] = this.parent[this.parent[node]];
         node = this.parent[node];
      }
      return node
   }

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu === pv) {
         return
      } else if (this.size[pu] >= this.size[pv]) {
         this.size[pu] += this.size[pv];
         this.parent[pv] = pu;
         this.components -= 1;
      } else {
         this.size[pv] += this.size[pu];
         this.parent[pu] = pv;
         this.components -= 1;
      }
   }
}


const countComponents = new Solution().countComponents;
console.log(new Solution().countComponents(3, [[0, 1], [0, 2]]) === 1)
console.log(new Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]) === 2)
console.log(new Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) === 1)
console.log(new Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]) === 2)
