import { MinPriorityQueue } from '@datastructures-js/priority-queue';

class Solution {
   /**
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(n+k)
    * Tags: priority queue
    * @param {number[]} numbers
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent(numbers, k) {
      const frequencyMap = new Map();

      for (const number of numbers) {
         frequencyMap.set(number, (frequencyMap.get(number) || 0) + 1);
      }

      const minHeap = new MinPriorityQueue(x => x[1]);

      for (const [number, frequency] of frequencyMap) {
         minHeap.enqueue([number, frequency]);
         if (minHeap.size() > k) {
            minHeap.pop();
         }
      }

      const result = [];
      while (minHeap.size()) {
         result.push(minHeap.dequeue()[0]);
      }

      return result;
   }
}
const topKFrequent = new Solution().topKFrequent;



import { Heap } from '@datastructures-js/heap';

class Solution {
   /**
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(n+k)
    * Tags: heap
    * @param {number[]} numbers
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent(numbers, k) {
      const frequencyMap = new Map();

      for (const number of numbers) {
         frequencyMap.set(number, (frequencyMap.get(number) || 0) + 1);
      }

      const minHeap = new Heap((a, b) => a[1] - b[1]);

      for (const [number, frequency] of frequencyMap) {
         minHeap.push([number, frequency]);
         if (minHeap.size() > k) {
            minHeap.pop();
         }
      }

      const result = [];
      while (minHeap.size()) {
         result.push(minHeap.pop()[0]);
      }

      return result;
   }
}
const topKFrequent = new Solution().topKFrequent;


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: bucket as hash map
    * @param {number[]} numbers
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent(numbers, k) {
      const numberFrequency = new Map();
      const bucket = Array(numbers.length + 1).fill(null);
      const solution = [];

      for (const number of numbers) {
         numberFrequency.set(number, (numberFrequency.get(number) ?? 0) + 1)
      }

      // bucket as a list of lists
      // [[], [3], [2], [1], [], [], []]
      for (const [key, val] of numberFrequency) {
         if (!bucket[val]) {
            bucket[val] = [];
         }
         bucket[val].push(key);
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


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: bucket as Object()
    * @param {number[]} numbers
    * @param {number} k
    * @return {number[]}
    */
   topKFrequent(numbers, k) {
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


console.log(new Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
console.log(new Solution().topKFrequent([1], 1), [1])
console.log(new Solution().topKFrequent([5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0, -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8, -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4, 5, -5], 7), [4, -1, 2, -5, 0, 8, -8])