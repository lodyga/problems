import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap
    * @param {number[]} nums
    * @return {number}
    */
   firstMissingPositive(nums) {
      const N = nums.length;
      const minHeap = new MinPriorityQueue();
      let res = 1;

      for (const num of nums) {
         if (num > 0) {
            minHeap.push(num);
         }
      }

      while (!minHeap.isEmpty()) {
         const num = minHeap.pop();

         if (num < res) {
            continue;
         }
         else if (num === res) {
            res++;
         }
         else {
            return res;
         }
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration, negative marking
    * @param {number[]} nums
    * @return {number}
    */
   firstMissingPositive(nums) {
      const N = nums.length;
      
      for (let idx = 0; idx < N; idx++) {
         if (nums[idx] <= 0) {
            nums[idx] = N + 1;
         }
      }

      for (let idx = 0; idx < N; idx++) {
         const num = Math.abs(nums[idx]);
         
         if (num <= N) {
            nums[num - 1] = -Math.abs(nums[num - 1]);
         }
      }

      for (let idx = 0; idx < N; idx++) {
         const num = nums[idx];
         
         if (num > 0) {
            return idx + 1;
         }
      }

      return N + 1;
   }
}


const firstMissingPositive = new Solution().firstMissingPositive;
console.log(new Solution().firstMissingPositive([1, 2, 0]) === 3)
console.log(new Solution().firstMissingPositive([3, 4, -1, 1]) === 2)
console.log(new Solution().firstMissingPositive([7, 8, 9, 11, 12]) === 1)
