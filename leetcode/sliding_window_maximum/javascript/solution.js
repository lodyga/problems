class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: sliding window, deque, monotonic queue
    * monotonically decreasing queue
    * @param {number[]} numbers
    * @param {number} windowSize
    * @return {number[]}
    */
   maxSlidingWindow(numbers, windowSize) {
      let left = 0;
      const window = [];  // [[number, index], ...]
      const maxArray = Array(numbers.length - windowSize + 1).fill(0);

      for (let right = 0; right < numbers.length; right++) {
         const number = numbers[right];

         while (window.length && window[0][1] < left) {
            window.shift();
         }

         while (window.length && window[window.length - 1][0] <= number) {
            window.pop();
         }

         window.push([number, right]);

         if (right - left + 1 == windowSize) {
            maxArray[left] = window[0][0];
            left++;
         }
      }
      return maxArray
   };
}
const maxSlidingWindow = new Solution().maxSlidingWindow;


console.log(new Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
console.log(new Solution().maxSlidingWindow([1], 1), [1])
console.log(new Solution().maxSlidingWindow([7, 2, 4], 2), [7, 4])
console.log(new Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3), [3, 3, 2, 5])
console.log(new Solution().maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3), [2, 2, 4, 4, 6])