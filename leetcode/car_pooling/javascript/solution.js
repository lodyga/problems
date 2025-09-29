import { MinPriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[][]} trips
    * @param {number} capacity
    * @return {number}
    */
   carPooling(trips, capacity) {
      trips.sort((a, b) => a[1] - b[1]);
      const passangerHeap = new MinPriorityQueue((passangers) => passangers[0]);
      
      for (const [passangers, start, end] of trips) {
         while (
            !passangerHeap.isEmpty() && 
            passangerHeap.front()[0] <= start
         ) {
            const [_, ejectPassangers] = passangerHeap.dequeue();
            capacity += ejectPassangers;
         }

         passangerHeap.enqueue([end, passangers]);  // heap([end, passangers], )
         capacity -= passangers;
         if (capacity < 0)
            return false
      }
      return true
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: iteration, brute-force
    * @param {number[][]} trips
    * @param {number} capacity
    * @return {number}
    */
   carPooling(trips, capacity) {
      const timeLine = Array(1001).fill(0);

      for (const [passengers, start, end] of trips) {
         timeLine[start] += passengers;
         timeLine[end] -= passengers;
      }

      for (let index = 0; index <= 1000; index++) {
         capacity -= timeLine[index];
         if (capacity < 0)
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
console.log(new Solution().carPooling([[9, 3, 6], [8, 1, 7],[6, 6, 8], [8, 4, 9], [4, 2, 9]], 28) === false)