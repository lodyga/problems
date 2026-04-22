import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n + klogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap
    *     A: iteration
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   findLeastNumOfUniqueInts(nums, k) {
      const numFreq = new Map();
      // heap([freq, ...])
      const minFreq = new MinPriorityQueue();

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      for (const freq of numFreq.values()) {
         minFreq.enqueue(freq);
      }

      while (k > 0) {
         const freq = minFreq.dequeue();

         if (freq > k) {
            minFreq.enqueue(freq - k);
         }

         k -= freq;
      }

      return minFreq.size()
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: bucket sort
    *     A: iteration
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   findLeastNumOfUniqueInts(nums, k) {
      const numFreq = new Map();
      const bucket = Array(nums.length).fill(0);
      let res = 0;

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      for (const freq of numFreq.values()) {
         bucket[freq - 1] += 1;
      }

      for (let index = 0; index < bucket.length; index++) {
         const freq = bucket[index]

         if (k <= 0) {
            res += freq;
         } else {
            k -= freq * (index + 1);

            if (k < 0) {
               while (k < 0) {
                  k += (index + 1);
                  res++;
               }

               k = 0;
            }
         }
      }

      return res
   };
}


const findLeastNumOfUniqueInts = new Solution().findLeastNumOfUniqueInts;
console.log(new Solution().findLeastNumOfUniqueInts([5, 5, 4], 1) === 1)
console.log(new Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3) === 2)
