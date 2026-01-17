// import { MinPriorityQueue } from '@datastructures-js/priority-queue';

class Solution {
   /**
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap, hash map
    *     A: iteration
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent(nums, k) {
      const numFrequency = new Map();
      for (const num of nums) {
         numFrequency.set(num, (numFrequency.get(num) || 0) + 1);
      }
      const numHeap = new MinPriorityQueue(x => x[0]);
      for (const [num, frequency] of numFrequency) {
         numHeap.enqueue([frequency, num]);
         if (numHeap.size() > k) {
            numHeap.pop();
         }
      }
      return numHeap.toArray().map(([_, num]) => num)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: bucket as list, hash map
    *     A: iteration
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent(nums, k) {
      const numFrequency = new Map();
      for (const number of nums) {
         numFrequency.set(number, (numFrequency.get(number) ?? 0) + 1)
      }
      
      const numBucket = Array(Math.max(...numFrequency.values()) + 1);
      for (const [num, frequency] of numFrequency) {
         if (numBucket[frequency] === undefined) {
            numBucket[frequency] = [];
         }
         numBucket[frequency].push(num);
      }
      
      const result = [];
      for (const numbers of numBucket.reverse()) {
         if (numbers) {
            for (let number of numbers) {
               result.push(number);
               if (result.length === k) {
                  return result
               }
            }
         }
      }
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: bucket as Object()
    * @param {number[]} numbers
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent2(numbers, k) {
      const numberFrequency = {};
      const bucket = Array(numbers.length + 1).fill(null);
      const solution = [];

      for (const number of numbers) {
         numberFrequency[number] = (numberFrequency[number] ?? 0) + 1
      }

      // bucket as a list of lists
      // [[], [3], [2], [1], [], [], []]
      for (const key of Object.keys(numberFrequency)) {
         let val = numberFrequency[key];
         if (!bucket[val]) {
            bucket[val] = [];
         }
         bucket[val].push(Number(key));
      }

      // get top k values
      for (const numbers of bucket.reverse()) {
         if (numbers) {
            for (let number of numbers) {
               solution.push(number);
               if (solution.length === k) {
                  return solution
               }
            }
         }
      }

      return -1
   };
}


const topKFrequent = new Solution().topKFrequent;
console.log(new Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
console.log(new Solution().topKFrequent([1], 1), [1])
console.log(new Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2), [1, 2])
console.log(new Solution().topKFrequent([5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0, -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8, -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4, 5, -5], 7), [4, -1, 2, -5, 0, 8, -8])
