import { PriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(m*n*logk)
    *     n: nums length
    *     m: avg string num length
    * Auxiliary space complexity: O(k)
    * Tags: heap
    * @param {string[]} nums
    * @param {number} k
    * @return {string}
    */
   kthLargestNumber(nums, k) {
      const minHeap = new PriorityQueue(
         (a, b) => a.length === b.length ? a.localeCompare(b) : a.length - b.length
      );

      for (const num of nums) {
         minHeap.enqueue(num);
         if (minHeap.size() > k)
            minHeap.dequeue();
      }
      return minHeap.front();
   };

   /**
    * Time complexity: O(m*n*logn)
    *     n: nums length
    *     m: avg string num length
    * Auxiliary space complexity: O(n)
    * Tags: sorting
    * @param {string[]} nums
    * @param {number} k
    * @return {string}
    */
   kthLargestNumber(nums, k) {
      nums.sort((a, b) => a.length === b.length ? b.localeCompare(a) : b.length - a.length);
      return nums[k - 1]
   };
}


const kthLargestNumber = new Solution().kthLargestNumber;
console.log(new Solution().kthLargestNumber(['3', '6', '7', '10'], 4) === '3')
console.log(new Solution().kthLargestNumber(['2', '21', '12', '1'], 3) === '2')
console.log(new Solution().kthLargestNumber(['0', '0'], 2) === '0')
