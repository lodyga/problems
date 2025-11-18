import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(nm)
    *    m: position k tickets
    * Auxiliary space complexity: O(n)
    * Tags: queue
    * @param {number[]} tickets
    * @param {number} k
    * @return {number}
    */
   timeRequiredToBuy(tickets, k) {
      const queue = new Queue(Array.from({ length: tickets.length }, (_, person) => [person, tickets[person]]))
      let time = 0;
      while (true) {
         const [person, ticket] = queue.pop();
         time++;
         if (ticket - 1 !== 0)
            queue.push([person, ticket - 1]);
         else if (person === k)
            return time
      }
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[]} tickets
    * @param {number} k
    * @return {number}
    */
   timeRequiredToBuy(tickets, k) {
      let time = 0
      const ticketsToBuy = tickets[k];

      for (let index = 0; index < tickets.length; index++) {
         const ticket = tickets[index];
         if (index <= k)
            time += Math.min(ticket, ticketsToBuy);
         else
            time += Math.min(ticket, ticketsToBuy - 1);
      }
      return time
   };
}


const timeRequiredToBuy = new Solution().timeRequiredToBuy;
console.log(new Solution().timeRequiredToBuy([2, 2], 0) === 3);
console.log(new Solution().timeRequiredToBuy([2, 3, 2], 2) === 6);
console.log(new Solution().timeRequiredToBuy([5, 1, 1, 1], 0) === 8);
