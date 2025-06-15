import { MaxPriorityQueue } from '@datastructures-js/priority-queue';

class Solution {
   /**
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(k)
    * Tags: heap
    * @param {number[][]} points
    * @param {number} k
    * @return {number[][]}
    */
   kClosest(points, k) {
      const maxHeap = new MaxPriorityQueue(x => x[1])

      for (const [x, y] of points) {
         const distance = (x ** 2 + y ** 2) //** 0.5;
         maxHeap.enqueue([[x, y], distance]);

         if (maxHeap.size() > k) {
            maxHeap.dequeue();
         }
      }
      return maxHeap
         .toArray()
         .map(([point, _]) => point)
   };
}



import { Heap } from '@datastructures-js/heap';

class Solution {
   /**
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(k)
    * Tags: heap
    * @param {number[][]} points
    * @param {number} k
    * @return {number[][]}
    */
   kClosest(points, k) {
      const maxHeap = new Heap((a, b) => b[1] - a[1]);

      for (const [x, y] of points) {
         const distance = (x ** 2 + y ** 2) //** 0.5;
         maxHeap.push([[x, y], distance]);

         if (maxHeap.size() > k) {
            maxHeap.pop();
         }
      }
      return maxHeap.toArray().map(([point, _]) => point)
   };
}
const kClosest = new Solution().kClosest;


console.log(new Solution().kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
console.log(new Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
console.log(new Solution().kClosest([[1, 3], [-2, 2], [2, -2]], 2), [[-2, 2], [2, -2]])