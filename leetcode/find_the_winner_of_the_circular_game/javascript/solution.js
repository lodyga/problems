import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(nk)
    * Auxiliary space complexity: O(n)
    * Tags: queue
    * @param {number} n
    * @param {number} k
    * @return {number}
    */
   findTheWinner(n, k) {
      const queue = new Queue(Array.from({length: n}, (_, index) => index))
      while (queue.size() > 1) {
         for (let index = 1; index < k; index++) 
            queue.push(queue.pop());
         queue.pop();
      }
      return queue.front() + 1
   };
}


const findTheWinner = new Solution().findTheWinner;
console.log(new Solution().findTheWinner(5, 2) === 3)
console.log(new Solution().findTheWinner(6, 5) === 1)
