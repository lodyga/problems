class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: graph, bucket sort, array
    * @param {number} n
    * @param {number[][]} roads
    * @return {number}
    */
   maximumImportance(n, roads) {
      const vertexDegree = Array(n).fill(0);
      for (const [u, v] of roads) {
         if (u !== v)
            vertexDegree[u]++;
         vertexDegree[v]++;
      }

      const buckets = Array.from({ length: n }, () => []);
      for (let vertex = 0; vertex < n; vertex++) {
         const degree = vertexDegree[vertex];
         buckets[degree].push(vertex);
      }

      const importanceMap = Array(n).fill(0);
      let importanceValue = n;
      for (let index = n - 1; index > -1; index--) {
         const bucket = buckets[index];
         if (bucket.length)
            for (const vertex of bucket) {
               importanceMap[vertex] = importanceValue;
               importanceValue--;
            }
      }

      let totalImportance = 0;
      for (let vertex = 0; vertex < n; vertex++)
         totalImportance += importanceMap[vertex] * vertexDegree[vertex]

      return totalImportance
   };
}


const maximumImportance = new Solution().maximumImportance;
console.log(new Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]) === 43)
console.log(new Solution().maximumImportance(5, [[0, 3], [2, 4], [1, 3]]) === 20)
console.log(new Solution().maximumImportance(5, [[0, 1]]) === 9)