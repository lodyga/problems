import { Deque } from "@datastructures-js/deque";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic decreasing queue, deque
    *     A: iteration
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   maxSlidingWindow(nums, k) {
      // Deque([(idx, num), ...])
      const deq = new Deque();
      const res = [];

      for (let idx = 0; idx < nums.length; idx++) {
         const num = nums[idx];

         while (deq.size() && deq.back()[0] <= num) {
            deq.popBack();
         }

         deq.pushBack([num, idx]);

         while (deq.front()[1] <= idx - k) {
            deq.popFront();
         }

         if (idx + 1 >= k) {
            res.push(deq.front()[0]);
         }
      }
      return res
   };
}


const maxSlidingWindow = new Solution().maxSlidingWindow;
console.log(new Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3).toString() === [3, 3, 5, 5, 6, 7].toString())
console.log(new Solution().maxSlidingWindow([1], 1).toString() === [1].toString())
console.log(new Solution().maxSlidingWindow([7, 2, 4], 2).toString() === [7, 4].toString())
console.log(new Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3).toString() === [3, 3, 2, 5].toString())
console.log(new Solution().maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3).toString() === [2, 2, 4, 4, 6].toString())
