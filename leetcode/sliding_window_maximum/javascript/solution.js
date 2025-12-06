class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic decreasing queue
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   maxSlidingWindow(nums, k) {
      const window = []  // [(index, num), ...]
      const maxWindowList = [];

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         while (window.length && window[0][0] < index - k + 1)
            window.shift();

         while (window.length && window[window.length - 1][1] <= num)
            window.pop();

         window.push([index, num]);

         if (index >= k - 1)
            maxWindowList.push(window[0][1]);
      }
      return maxWindowList
   };
}


const maxSlidingWindow = new Solution().maxSlidingWindow;
console.log(new Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
console.log(new Solution().maxSlidingWindow([1], 1), [1])
console.log(new Solution().maxSlidingWindow([7, 2, 4], 2), [7, 4])
console.log(new Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3), [3, 3, 2, 5])
console.log(new Solution().maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3), [2, 2, 4, 4, 6])
