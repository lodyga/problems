import { MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: heap
    *     A: heap
    * @param {number[][]} points
    * @param {number} k
    * @return {number[][]}
    */
   kClosest(points, k) {
      const pointHeap = new MaxPriorityQueue(x => x[0]);
      for (const [x, y] of points) {
         const dist = x ** 2 + y ** 2;
         pointHeap.enqueue([dist, x, y]);
         if (pointHeap.size() > k)
            pointHeap.dequeue();
      }
      return pointHeap.toArray().map(([_, x, y]) => [x, y])
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(k)
    * Tags:
    *     A: sorting, build-in function
    * @param {number[][]} points
    * @param {number} k
    * @return {number[][]}
    */
   kClosest(points, k) {
      points.sort((a, b) => a[0] ** 2 + a[1] ** 2 - b[0] ** 2 - b[1] ** 2);
      return points.slice(0, k)
   };
}


const kClosest = new Solution().kClosest;
console.log(new Solution().kClosest([[1, 3], [-2, 2]], 1).sort().toString() === [[-2, 2]].sort().toString())
console.log(new Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2).sort().toString() === [[3, 3], [-2, 4]].sort().toString())
console.log(new Solution().kClosest([[1, 3], [-2, 2], [2, -2]], 2).sort().toString() === [[-2, 2], [2, -2]].sort().toString())
