import { MinPriorityQueue } from "@datastructures-js/priority-queue";


/**
 * Time complexity: O(nlogn)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: heap
 *     A: iteration
 * @param {number} n 
 * @returns {SeatManager}
 */
class SeatManager {
   /**
    * @param {number} n
    */
   constructor(n) {
      this.seats = new MinPriorityQueue();
      this.nextSeat = 1;
   };

   /**
    * @return {number}
    */
   reserve() {
      if (this.seats.size()) {
         return this.seats.dequeue();
      } else {
         return this.nextSeat++
      }
   };

   /**
    * @param {number} seatNumber
    * @return {void}
    */
   unreserve(seatNumber) {
      this.seats.enqueue(seatNumber)
   };
}


const seatManager = new SeatManager(5);
console.log(seatManager.reserve() === 1)
console.log(seatManager.reserve() === 2)
seatManager.unreserve(2)
console.log(seatManager.reserve() === 2)
console.log(seatManager.reserve() === 3)
console.log(seatManager.reserve() === 4)
console.log(seatManager.reserve() === 5)
seatManager.unreserve(5)
