class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic increasing queue, monotonic decreasing queue
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} limit
    * @return {number}
    */
   longestSubarray(nums, limit) {
      // Store min value in monotonic increasing queue.
      // array([(number, index), ...])
      const inc = [];
      let incHead = 0;
      // Store max value in monotonic decreasing queue.
      // array([(number, index), ...])
      const dec = [];
      let decHead = 0;
      let left = 0;
      let res = 0;

      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];

         while (inc.length > incHead && inc[inc.length - 1][0] > num)
            inc.pop();
         inc.push([num, right]);

         while (dec.length > decHead && dec[dec.length - 1][0] < num)
            dec.pop();
         dec.push([num, right]);

         while (dec[decHead][0] - inc[incHead][0] > limit) {
            if (inc[incHead][1] === left)
               incHead++;
            if (dec[decHead][1] === left)
               decHead++;
            left++;
         }

         res = Math.max(res, right - left + 1);
      }

      return res;
   }
}


const longestSubarray = new Solution().longestSubarray;
console.log(new Solution().longestSubarray([8, 2, 4, 7], 4) === 2)
console.log(new Solution().longestSubarray([1, 5, 6, 7, 8, 10, 6, 5, 6], 4) === 5)
console.log(new Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5) === 4)
console.log(new Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0) === 3)
console.log(new Solution().longestSubarray([4, 10, 2, 6, 1], 10) === 5)
console.log(new Solution().longestSubarray([1, 8, 6, 10], 8) === 3)
