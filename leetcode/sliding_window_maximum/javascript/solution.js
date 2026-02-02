import { Deque } from "@datastructures-js/deque";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic decreasing queue
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   maxSlidingWindow(nums, k) {
      // Deque([(right, num), ...])
      const windowQ = new Deque();
      const res = [];

      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];
         while (windowQ.size() && windowQ.front()[0] <= right - k)
            windowQ.popFront();

         while (windowQ.size() && windowQ.back()[1] <= num)
            windowQ.popBack();

         windowQ.pushBack([right, num]);

         if (right < k - 1)
            continue

         res.push(windowQ.front()[1]);
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
