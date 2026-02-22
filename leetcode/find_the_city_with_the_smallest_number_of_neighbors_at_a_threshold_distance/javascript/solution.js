import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n3logn)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: heap, hash map, hash set
    *     A: greedy, Dijkstra
    *     Model: graph
    * @param {number} n
    * @param {number[][]} edges
    * @param {number} distanceThreshold
    * @return {number}
    */
   findTheCity(n, edges, distanceThreshold) {
      const adjs = new Map(Array.from({ length: n }, (_, index) => [index, []]));

      for (const [u, v, distance] of edges) {
         adjs.get(u).push([distance, v]);
         adjs.get(v).push([distance, u]);
      }

      const dijkstra = (city) => {
         const visited = Array(n).fill(false);
         const cityHeap = new MinPriorityQueue(x => x[0]);
         cityHeap.enqueue([0, city]);

         while (cityHeap.size()) {
            const [distance, city] = cityHeap.dequeue();

            if (visited[city]) {
               continue
            }

            visited[city] = true;

            for (const [adj_distance, adj_city] of adjs.get(city)) {
               if (distance + adj_distance <= distanceThreshold) {
                  cityHeap.enqueue([distance + adj_distance, adj_city]);
               }
            }
         }

         return visited.filter(val => val).length - 1;
      }

      let resCity = -1;
      let minNeighborsCounter = n;

      for (let city = 0; city < n; city++) {
         const neighborsCounter = dijkstra(city);
         if (neighborsCounter <= minNeighborsCounter) {
            minNeighborsCounter = neighborsCounter;
            resCity = city;
         }
      }

      return resCity
   };
}


const findTheCity = new Solution().findTheCity;
   console.log(new Solution().findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) === 3)
console.log(new Solution().findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) === 0)
console.log(new Solution().findTheCity(6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20) === 5)
