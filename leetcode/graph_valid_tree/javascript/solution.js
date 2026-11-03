import { Queue } from "@datastructures-js/queue";


class Solution2 {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: Single-source DFS, cycle detection
    * @param {number} vertexCount
    * @param {number[][]} edges
    * @returns {boolean}
    */
   validTree(vertexCount, edges) {
      const dfs = (vertex, prevVertex) => {
         if (visited[vertex]) {
            return false;
         }

         visited[vertex] = true;

         for (const adjVertex of adjVertices.get(vertex)) {
            if (
               adjVertex !== prevVertex
               && !dfs(adjVertex, vertex)
            ) {
               return false;
            }
         }

         return true;
      };

      // Tree property: E == V - 1
      if (edges.length !== vertexCount - 1) {
         return false;
      }

      const adjVertices = new Map();
      for (let vertex = 0; vertex < vertexCount; vertex++) {
         adjVertices.set(vertex, new Set());
      }

      for (const [u, v] of edges) {
         if (u === v) {
            return false;
         }

         adjVertices.set(u, adjVertices.get(u).add(v));
         adjVertices.set(v, adjVertices.get(v).add(u));
      }

      const visited = Array(vertexCount).fill(false);

      // No cycles and connected.
      return dfs(0, -1) && visited.every(v => v == true);
   }
}


class Solution5 {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: Single-source BFS, cycle detection
    * @param {number} vertexCount
    * @param {number[][]} edges
    * @returns {boolean}
    */
   validTree(vertexCount, edges) {
      // Tree property: E == V - 1
      if (edges.length !== vertexCount - 1) {
         return false;
      }

      const adjVertices = new Map();
      for (let vertex = 0; vertex < vertexCount; vertex++) {
         adjVertices.set(vertex, new Set());
      }

      for (const [u, v] of edges) {
         if (u === v) {
            return false;
         }

         adjVertices.set(u, adjVertices.get(u).add(v));
         adjVertices.set(v, adjVertices.get(v).add(u));
      }

      const visited = Array(vertexCount).fill(false);
      const queue = new Queue([[0, -1]]);
      visited[0] = true;

      while (!queue.isEmpty()) {
         const [vertex, prev] = queue.pop();

         
         for (const adjVertex of adjVertices.get(vertex)) {
            if (adjVertex !== prev) {
               if (visited[adjVertex]) {
                  return false;
               }

               queue.push([adjVertex, vertex]);
               visited[adjVertex] = true;
            }
         }
      }

      return visited.every(v => v == true);
   }
}


class DSU {
   constructor(N) {
      this.size = Array(N).fill(1);
      this.parent = Array.from({ length: N }, (_, idx) => idx);
   };

   find(u) {
      while (u !== this.parent[u]) {
         this.parent[u] = this.parent[this.parent[u]];
         u = this.parent[u];
      }
      return u;
   };

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu == pv) {
         return false;
      } 
      else if (this.size[pu] >= this.size[pv]) {
         this.size[pu] += this.size[pv];
         this.parent[pv] = this.parent[pu];
      } 
      else {
         this.size[pv] += this.size[pu];
         this.parent[pu] = this.parent[pv];
      }

      return true;
   }
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: DSU, cycle detection
    * @param {number} vertexCount
    * @param {number[][]} edges
    * @returns {boolean}
    */
   validTree(vertexCount, edges) {
      // Tree property: E == V - 1
      if (edges.length !== vertexCount - 1) {
         return false;
      }

      const dsu = new DSU(vertexCount);
      
      for (const [u, v] of edges)
         if (dsu.union(u, v) === false) {
            return false
         }

      return true;
   }
}




const validTree = new Solution().validTree;
console.log(new Solution().validTree(3, [[0, 1], [1, 2], [2, 0]]) === false)
console.log(new Solution().validTree(1, [[0, 0]]) === false)
console.log(new Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) === true)
console.log(new Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) === false)
console.log(new Solution().validTree(4, [[0, 1], [2, 3]]) === false)
console.log(new Solution().validTree(5, [[0, 1], [2, 0], [3, 0], [1, 4]]) === true)
console.log(new Solution().validTree(5, [[0, 1], [1, 3], [3, 2], [1, 4]]) === true)
console.log(new Solution().validTree(1, []) === true)
console.log(new Solution().validTree(3, [[0, 1], [1, 2], [2, 0]]) === false)
console.log(new Solution().validTree(5, [[0, 1], [1, 3], [3, 0], [2, 4]]) == false)
