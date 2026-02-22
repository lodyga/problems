import { MinPriorityQueue, MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sorting, brute force
    * @param {number[]} nums
    * @return {number}
    */
   minDifference(nums) {
      if (nums.length <= 4) {
         return 0
      }

      nums.sort((a, b) => a - b);
      const N = nums.length;

      return Math.min(
         nums[N - 4] - nums[0],
         nums[N - 3] - nums[1],
         nums[N - 2] - nums[2],
         nums[N - 1] - nums[3]
      )
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap
    * @param {number[]} nums
    * @return {number}
    */
   minDifference(nums) {
      if (nums.length <= 4) {
         return 0
      }

      const minHeap = new MinPriorityQueue();
      const maxHeap = new MaxPriorityQueue();

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         minHeap.enqueue(num);
         maxHeap.enqueue(num);

         if (index >= 4) {
            minHeap.dequeue();
            maxHeap.dequeue();
         }
      }

      const minNums = maxHeap.toArray().sort((a, b) => a - b);
      const maxNums = minHeap.toArray().sort((a, b) => a - b);
      return Math.min(...maxNums.map((val, ind) => val - minNums[ind]))
   };
}


const minDifference = new Solution().minDifference;
console.log(new Solution().minDifference([5, 3, 2, 4]) === 0)
console.log(new Solution().minDifference([3, 100, 20]) === 0)
console.log(new Solution().minDifference([1, 5, 0, 10, 14]) === 1)
console.log(new Solution().minDifference([90, 35, 67, 53, 61]) === 6)
console.log(new Solution().minDifference([6, 6, 0, 1, 1, 4, 6]) === 2)
