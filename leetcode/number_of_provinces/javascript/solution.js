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
    * Time complexity: O(n2)
    *     n: adjacency matrix side
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: DSU
    *     Model: graph
    * @param {number[][]} isConnected
    * @return {number}
    */
   findCircleNum(isConnected) {
      const n = isConnected.length;
      const dsu = new DSU(n);

      for (let row = 0; row < n; row++) {
         for (let col = 0; col < n; col++) {
            if (row > col && isConnected[row][col]) {
               dsu.union(row, col);
            }
         }
      }

      return dsu.components;
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    *     n: adjacency matrix side
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: multi-source DFS
    *     Model: graph
    * @param {number[][]} isConnected
    * @return {number}
    */
   findCircleNum(isConnected) {
      const dfs = (node) => {
         if (visited[node]) {
            return 0;
         }

         visited[node] = true;

         for (let adjNode = 0; adjNode < n; adjNode++) {
            if (adjNode !== node && isConnected[node][adjNode]) {
               dfs(adjNode);
            }
         }

         return 1;
      };

      const n = isConnected.length;
      let components = 0;
      const visited = Array(n).fill(false);

      for (let node = 0; node < n; node++) {
         components += dfs(node);
      }

      return components;
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    *     n: adjacency matrix side
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: queue, array
    *     A: multi-source BFS
    *     Model: graph
    * @param {number[][]} isConnected
    * @return {number}
    */
   findCircleNum(isConnected) {
      const bfs = (node) => {
         if (visited[node]) {
            return 0;
         }

         const queue = new Queue([node]);
         visited[node] = true;

         while (queue.size()) {
            const node = queue.pop();

            for (let adjNode = 0; adjNode < n; adjNode++) {
               if (
                  adjNode !== node
                  && isConnected[node][adjNode]
                  && !visited[adjNode]
               ) {
                  queue.push(adjNode);
                  visited[adjNode] = true;
               }
            }
         }

         return 1;
      };

      const n = isConnected.length;
      const visited = Array(n).fill(false);
      let components = 0;

      for (let node = 0; node < n; node++) {
         components += bfs(node);
      }

      return components;
   }
}


const findCircleNum = new Solution().findCircleNum;
console.log(new Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) === 2)
console.log(new Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) === 3)
console.log(new Solution().findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) === 1)
