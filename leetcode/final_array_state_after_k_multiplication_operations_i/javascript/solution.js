import { PriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(nlogn + klogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap
    *     A: iteration
    * @param {number[]} nums
    * @param {number} k
    * @param {number} multiplier
    * @return {number[]}
    */
   getFinalState(nums, k, multiplier) {
      const numsCopy = nums.slice();
      const numHeap = new PriorityQueue((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));

      for (let index = 0; index < nums.length; index++) {
         numHeap.enqueue([nums[index], index]);
      }

      for (let _ = 0; _ < k; _++) {
         const [, index] = numHeap.dequeue();
         numsCopy[index] *= multiplier;
         numHeap.enqueue([numsCopy[index], index])
      }

      return numsCopy
   };
}


const getFinalState = new Solution().getFinalState;
console.log(new Solution().getFinalState([2, 1, 3, 5, 6], 5, 2).toString() === [8, 4, 6, 5, 6].toString())
console.log(new Solution().getFinalState([1, 2], 3, 4).toString() === [16, 8].toString())
