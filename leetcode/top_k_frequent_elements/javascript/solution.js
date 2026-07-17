import { MinPriorityQueue } from '@datastructures-js/priority-queue';


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
      const numFreq = new Map();

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      const numHeap = new MinPriorityQueue(x => x[0]);
      
      for (const [num, freq] of numFreq) {
         numHeap.enqueue([freq, num]);

         if (numHeap.size() > k) {
            numHeap.pop();
         }
      }
      
      return numHeap.toArray().map(([_, num]) => num);
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, list
    *     A: bucket sort
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent(nums, k) {
      const numFreq = new Map();
      const res = [];
      
      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1)
      }
      
      const numBucket = Array.from({length: Math.max(...numFreq.values())}, () => []);
      
      for (const [num, freq] of numFreq) {
         numBucket[freq - 1].push(num);
      }
      
      for (const nums of numBucket.reverse()) {
         if (nums) {
            for (let num of nums) {
               res.push(num);
               
               if (res.length === k) {
                  return res;
               }
            }
         }
      }
   }
}


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: bucket as Object()
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent(nums, k) {
      const numFreq = {};
      const bucket = Array(nums.length + 1).fill(null);
      const solution = [];

      for (const num of nums) {
         numFreq[num] = (numFreq[num] || 0) + 1
      }

      // bucket as a list of lists
      // [[], [3], [2], [1], [], [], []]
      for (const key of Object.keys(numFreq)) {
         let val = numFreq[key];
         if (!bucket[val]) {
            bucket[val] = [];
         }
         bucket[val].push(Number(key));
      }

      // get top k values
      for (const nums of bucket.reverse()) {
         if (nums) {
            for (let num of nums) {
               solution.push(num);
               if (solution.length === k) {
                  return solution;
               }
            }
         }
      }

      return -1;
   }
}


const topKFrequent = new Solution().topKFrequent;
console.log(new Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2).sort().toString() === [1, 2].toString())
console.log(new Solution().topKFrequent([1], 1).sort().toString() === [1].toString())
console.log(new Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2).sort().toString() === [1, 2].toString())
console.log(new Solution().topKFrequent([5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0, -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8, -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4, 5, -5], 7).sort().toString() === [4, -1, 2, -5, 0, 8, -8].sort().toString())
