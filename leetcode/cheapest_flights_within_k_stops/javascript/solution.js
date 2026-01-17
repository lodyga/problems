import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(Elog(V*k))
    * Auxiliary space complexity: O(V*k)
    * Tags:
    *     DS: heap, array
    *     A: greedy, Dijkstra with cache
    *     Model: graph
    * @param {number} n
    * @param {number[][]} flights
    * @param {number} src
    * @param {number} dst
    * @param {number} k
    * @return {number}
    */
   findCheapestPrice(N, flights, src, dst, k) {
      const UPPER_BOUND = 10 ** 6
      const cache = Array.from({ length: N }, () => Array(k + 2).fill(UPPER_BOUND));
      const adjCities = Array.from({ length: N }, () => []);

      for (const [city, destination, price] of flights) {
         adjCities[city].push([destination, price]);
      }

      const flightHeap = new MinPriorityQueue(vertex => vertex[0]);
      // Heap([price, city, transits])
      flightHeap.enqueue([0, src, 0]);

      while (flightHeap.size()) {
         const [price, city, transits] = flightHeap.dequeue();

         if (city === dst) {
            return price
         } else if (
            transits === k + 1 ||
            price > cache[city][transits]
         ) {
            continue
         }

         for (const [adjCity, adjPrice] of adjCities[city]) {
            const partialPrice = price + adjPrice;
            
            if (partialPrice < cache[adjCity][transits + 1]) {
               cache[adjCity][transits + 1] = partialPrice;
               flightHeap.enqueue([partialPrice, adjCity, transits + 1]);
            }
         }
      }
      return - 1
   };

   /**
    * Time complexity: O(E*k)
    *     O(E*V) => O(E*V)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: BFS, Bellman-Ford
    *     Model: graph
    * @param {number} n
    * @param {number[][]} flights
    * @param {number} src
    * @param {number} dst
    * @param {number} k
    * @return {number}
    */
   findCheapestPrice(n, flights, src, dst, k) {
      const COST_BOUND = 10**6
      let costCache = Array(n).fill(COST_BOUND);
      costCache[src] = 0;

      for (let transits = 0; transits <= k; transits++) {
         const cacheCacheCopy = costCache.slice();

         for (const [source, destination, price] of flights) {
            if (costCache[source] === COST_BOUND) {
               continue
            } else if (costCache[source] + price < cacheCacheCopy[destination]) {
               cacheCacheCopy[destination] = costCache[source] + price;
            }
         }
         costCache = cacheCacheCopy;
      }
      return costCache[dst] !== COST_BOUND ? costCache[dst] : -1
   };
}


const findCheapestPrice = new Solution().findCheapestPrice;
console.log(new Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) === 700)
console.log(new Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) === 200)
console.log(new Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) === 500)
console.log(new Solution().findCheapestPrice(5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1) === -1)
console.log(new Solution().findCheapestPrice(5, [[1, 0, 5], [2, 1, 5], [3, 0, 2], [1, 3, 2], [4, 1, 1], [2, 4, 1]], 2, 0, 2) === 7)
console.log(new Solution().findCheapestPrice(11, [[0, 3, 3], [3, 4, 3], [4, 1, 3], [0, 5, 1], [5, 1, 100], [0, 6, 2], [6, 1, 100], [0, 7, 1], [7, 8, 1], [8, 9, 1], [9, 1, 1], [1, 10, 1], [10, 2, 1], [1, 2, 100]], 0, 2, 4) === 11)
console.log(new Solution().findCheapestPrice(13, [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8], [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64], [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92], [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23], [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98], [8, 10, 61], [2, 12, 38], [5, 7, 58], [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7], [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67], [5, 6, 34], [9, 7, 62], [5, 3, 67]], 10, 1, 10) === -1)
