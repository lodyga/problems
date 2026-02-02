import { MinPriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[][]} trips
    * @param {number} cap
    * @return {number}
    */
   carPooling(trips, cap) {
      trips.sort((a, b) => a[1] - b[1]);
      // heap([end stop, passanger count], )
      const exitHeap = new MinPriorityQueue(p => p[0]);

      for (const [passangers, start, end] of trips) {
         while (
            exitHeap.size() &&
            exitHeap.front()[0] <= start
         ) {
            const [, exitPassangers] = exitHeap.dequeue();
            cap += exitPassangers;
         }

         cap -= passangers;
         if (cap < 0)
            return false

         exitHeap.enqueue([end, passangers]);
      }
      return true
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: line sweep, prefix sum, sorting, iteration
    * @param {number[][]} trips
    * @param {number} cap
    * @return {number}
    */
   carPooling(trips, cap) {
      const events = [];

      for (const [passengers, start, end] of trips) {
         events.push([start, passengers]);
         events.push([end, -passengers]);
      }

      events.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);

      let total = 0;
      for (const [, passangers] of events) {
         total += passangers;
         if (total > cap)
            return false
      }
      return true
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: line sweep, iteration
    * @param {number[][]} trips
    * @param {number} cap
    * @return {number}
    */
   carPooling(trips, cap) {
      const UPPER_BOUND = 1001
      const timeLine = Array(UPPER_BOUND).fill(0);

      for (const [passengers, start, end] of trips) {
         timeLine[start] += passengers;
         timeLine[end] -= passengers;
      }

      for (let index = 0; index < UPPER_BOUND; index++) {
         cap -= timeLine[index];
         if (cap < 0)
            return false
      }
      return true
   };
}


const carPooling = new Solution().carPooling;
console.log(new Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4) === false)
console.log(new Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5) === true)
console.log(new Solution().carPooling([[4, 5, 6], [6, 4, 7], [4, 3, 5], [2, 3, 5]], 13) === true)
console.log(new Solution().carPooling([[2, 1, 5], [1, 2, 3], [3, 3, 7]], 4) === false)
console.log(new Solution().carPooling([[9, 3, 6], [8, 1, 7], [6, 6, 8], [8, 4, 9], [4, 2, 9]], 28) === false)
