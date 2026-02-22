import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap
    *     A: sorting
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   maximumBeauty(nums, k) {
      nums.sort((a, b) => a - b);
      let res = 1;
      const beautyHeap = new MinPriorityQueue();

      for (const num of nums) {
         if (beautyHeap.size() && beautyHeap.front() < num - k) {
            beautyHeap.dequeue();
         }

         if (num + k >= 0) {
            beautyHeap.enqueue(num + k);
            res = Math.max(res, beautyHeap.size());
         }
      }

      return res
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   maximumBeauty(nums, k) {
      nums.sort((a, b) => a - b);
      let res = 1;
      let left = 0;

      for (let right = 0; right < nums.length; right++) {
         while (nums[right] - nums[left] > k * 2) {
            left++;
         }

         res = Math.max(res, right - left + 1);
      }

      return res
   };
}


const maximumBeauty = new Solution().maximumBeauty;
console.log(new Solution().maximumBeauty([4, 6, 1, 2], 2) === 3)
console.log(new Solution().maximumBeauty([1, 1, 1, 1], 10) === 4)
console.log(new Solution().maximumBeauty([75, 15, 9], 28) === 2)
console.log(new Solution().maximumBeauty([48, 93, 96, 19], 24) === 3)
