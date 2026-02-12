import { MinPriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(k + E)
    *     O(k + ElogV) -> O(k + E)
    *     k: text length
    *     V: vertex count = 26
    *     E: edges count = 26**2
    * Auxiliary space complexity: O(E)
    *     O(E + 26**2)
    * Tags:
    *     DS: heap, hash map, array
    *     A: greedy, Dijkstra with cache
    *     Model: graph
    * @param {string} source
    * @param {string} target
    * @param {character[]} original
    * @param {character[]} changed
    * @param {number[]} cost
    * @return {number}
    */
   minimumCost(source, target, original, changed, cost) {
      // direct costs only
      // {src: [(dst, cost), ], }
      const adjs = new Map();
      for (let index = 0; index < original.length; index++) {
         const src = original[index];
         const dst = changed[index];
         const c = cost[index];

         if (!adjs.has(src)) {
            adjs.set(src, []);
            adjs.get(src).push([dst, c]);
         }
      }

      const dijkstra = (src, dst) => {
         if (costCache.has(`${src},${dst}`))
            return costCache.get(`${src},${dst}`)

         const baseSrc = src;
         const costHeap = new MinPriorityQueue(x => x[0]);
         costHeap.enqueue([0, src]);
         const path = Array(26).fill(false);

         while (costHeap.size()) {
            const [cost, src] = costHeap.dequeue();

            if (path[src.charCodeAt(0) - 'a'.charCodeAt(0)])
               continue

            path[src.charCodeAt(0) - 'a'.charCodeAt(0)] = true;

            // cache all intermediate paths
            costCache.set(`${baseSrc},${src}`, cost);

            if (src === dst)
               return cost

            if (!adjs.has(src))
               continue

            for (const [adjSrc, adjCost] of adjs.get(src)) {
               if (!(path[adjSrc.charCodeAt(0) - 'a'.charCodeAt(0)])) {
                  costHeap.enqueue([adjCost + cost, adjSrc]);
               }
            }
         }
         return -1
      }


      let totalCost = 0;
      // direct and indirect costs cache
      // {src: [(dst, cost), ], }
      const costCache = new Map();

      for (let index = 0; index < source.length; index++) {
         const src = source[index];
         const dst = target[index];

         if (src === dst)
            continue

         const cost = dijkstra(src, dst);
         totalCost += cost;

         if (cost === -1)
            return -1
      }

      return totalCost
   };
}


const minimumCost = new Solution().minimumCost;
console.log(new Solution().minimumCost('abcd', 'acbe', ['a', 'b', 'c', 'c', 'e', 'd'], ['b', 'c', 'b', 'e', 'b', 'e'], [2, 5, 5, 1, 2, 20]))
console.log(new Solution().minimumCost('abcd', 'acbe', ['a', 'b', 'c', 'c', 'e', 'd'], ['b', 'c', 'b', 'e', 'b', 'e'], [2, 5, 5, 1, 2, 20]) === 28)
console.log(new Solution().minimumCost('aaaa', 'bbbb', ['a', 'c'], ['c', 'b'], [1, 2]) === 12)
console.log(new Solution().minimumCost('abcd', 'abce', ['a'], ['e'], [10000]) === -1)
console.log(new Solution().minimumCost('aadbddcabd', 'bdcdccbada', ['d', 'a', 'a', 'b', 'd', 'b'], ['b', 'c', 'd', 'c', 'a', 'd'], [6, 10, 5, 8, 11, 4]) === -1)
console.log(new Solution().minimumCost('aabbddccbc', 'abbbaabaca', ['a', 'b', 'c', 'b', 'a', 'd'], ['d', 'c', 'b', 'd', 'b', 'b'], [3, 8, 7, 6, 7, 10]) === -1)
console.log(new Solution().minimumCost('bcaabaddac', 'bdccbdaadc', ['c', 'd', 'a', 'a', 'c', 'a', 'd'], ['a', 'a', 'd', 'b', 'd', 'c', 'c'], [4, 3, 6, 3, 11, 6, 4]) === 40)
