import { Queue } from '@datastructures-js/queue'


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: queue
    *     A: greedy
    * @param {string} senate
    * @return {string}
    */
   predictPartyVictory(senate) {
      const votes = new Queue(Array.from(senate));
      let r = 0;

      while (votes.size() > Math.abs(r)) {
         const vote = votes.dequeue();

         if (vote === 'R') {
            if (r >= 0)
               votes.enqueue('R');
            r++;

         } else {
            if (r <= 0)
               votes.enqueue('D');
            r--;
         }
      }

      return votes.front() == "R" ? 'Radiant' : 'Dire';
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: queue
    *     A: greedy
    * @param {string} senate
    * @return {string}
    */
   predictPartyVictory(senate) {
      const radiantVotes = new Queue();
      const direVotes = new Queue();

      for (let index = 0; index < senate.length; index++) {
         const senator = senate[index];
         if (senator === 'R')
            radiantVotes.enqueue(index);
         else
            direVotes.enqueue(index);
      }

      while (
         radiantVotes.size() &&
         direVotes.size()
      ) {
         if (radiantVotes.front() < direVotes.front()) {
            radiantVotes.enqueue(radiantVotes.front() + senate.length);
         } else {
            direVotes.enqueue(direVotes.front() + senate.length);
         }
         radiantVotes.dequeue();
         direVotes.dequeue()
      }

      return radiantVotes.isEmpty() ? 'Dire' : 'Radiant'
   };
}


const predictPartyVictory = new Solution().predictPartyVictory;
console.log(new Solution().predictPartyVictory('RD') === 'Radiant')
console.log(new Solution().predictPartyVictory('DR') === 'Dire')
console.log(new Solution().predictPartyVictory('RDD') === 'Dire')
console.log(new Solution().predictPartyVictory('RDDDRR') === 'Dire')
console.log(new Solution().predictPartyVictory('RDDR') === 'Radiant')
console.log(new Solution().predictPartyVictory('DRRD') === 'Dire')
console.log(new Solution().predictPartyVictory('DDDDRRDDDRDRDRRDDRDDDRDRRRRDRRRRRDRDDRDDRRDDRRRDDRRRDDDDRRRRRRRDDRRRDDRDDDRRRDRDDRDDDRRDRRDRRRDRDRDR') === 'Dire')
