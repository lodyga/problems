import { Queue } from "@datastructures-js/queue";


class DSU {
   constructor(n) {
      this.size = Array(n).fill(1);
      this.parent = Array.from({ length: n }, (_, node) => node);
      this.components = n;
   }

   find(node) {
      while (node !== this.parent[node]) {
         this.parent[node] = this.parent[this.parent[node]];
         node = this.parent[node];
      }
      return node;
   }

   union(u, v) {
      let pu = this.find(u);
      let pv = this.find(v);

      if (pu === pv) {
         return;
      }
      else if (this.size[pu] > this.size[pv]) {
         [pu, pv] = [pv, pu];
      }

      this.size[pu] += this.size[pv];
      this.parent[pv] = pu;
      this.components--;
   }
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: DSU
    *     Model: graph
    * @param {number} n
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(n, edges) {
      const dsu = new DSU(n);

      for (const [u, v] of edges) {
         dsu.union(u, v);
      }

      return dsu.components;
   }
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: multi-source DFS
    *     Model: graph
    * @param {number} n
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(n, edges) {
      const dfs = (node) => {
         if (visited[node]) {
            return 0;
         }

         visited[node] = true;

         for (const adjNode of adjNodes[node]) {
            dfs(adjNode);
         }

         return 1;
      };

      let components = 0;
      const visited = Array(n).fill(false);
      const adjNodes = Array.from({ length: n }, () => []);

      for (const [u, v] of edges) {
         adjNodes[u].push(v);
         adjNodes[v].push(u);
      }

      for (let node = 0; node < n; node++) {
         components += dfs(node);
      }

      return components;
   }
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: queue, array
    *     A: multi-source BFS
    *     Model: graph
    * @param {number} n
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(n, edges) {
      const bfs = (node) => {
         if (visited[node]) {
            return 0;
         }

         const queue = new Queue([node]);
         visited[node] = true;

         while (queue.size()) {
            const node = queue.pop();

            for (const adjNode of adjNodes[node])
               if (!visited[adjNode]) {
                  queue.push(adjNode);
                  visited[adjNode] = true;
               }
         }

         return 1;
      };

      const visited = Array(n).fill(false);
      const adjNodes = Array.from({ length: n }, () => []);
      let components = 0;

      for (let node = 0; node < n; node++) {
         adjNodes[node] = [];
      }

      for (const [u, v] of edges) {
         adjNodes[u].push(v);
         adjNodes[v].push(u);
      }

      for (let node = 0; node < n; node++) {
         components += bfs(node);
      }

      return components;
   }
}


const countComponents = new Solution().countComponents;
console.log(new Solution().countComponents(3, [[0, 1], [0, 2]]) === 1)
console.log(new Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]) === 2)
console.log(new Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) === 1)
console.log(new Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]) === 2)
