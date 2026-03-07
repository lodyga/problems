import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n*m)
    *     m: tickets[k]
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: queue
    *     A: iteration
    * @param {number[]} tickets
    * @param {number} k
    * @return {number}
    */
   timeRequiredToBuy(tickets, k) {
      const queue = new Queue(Array.from({ length: tickets.length }, (_, index) => [tickets[index], index]))
      let res = 0;

      while (true) {
         let [ticket, index] = queue.pop();
         res++;
         ticket--;

         if (ticket) {
            queue.push([ticket, index]);
         } else if (index === k) {
            return res
         }
      }
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} tickets
    * @param {number} k
    * @return {number}
    */
   timeRequiredToBuy(tickets, k) {
      let res = 0
      const ticketsToBuy = tickets[k];

      for (let index = 0; index < tickets.length; index++) {
         const ticket = tickets[index];

         if (ticket < ticketsToBuy)
            res += ticket;
         else {
            res += ticketsToBuy;
            res -= index > k ? 1 : 0;
         }
      }
      return res
   };
}


const timeRequiredToBuy = new Solution().timeRequiredToBuy;
console.log(new Solution().timeRequiredToBuy([2, 2], 0) === 3);
console.log(new Solution().timeRequiredToBuy([2, 3, 2], 2) === 6);
console.log(new Solution().timeRequiredToBuy([5, 1, 1, 1], 0) === 8);
