import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: heap
    * @param {number[][]} times
    * @param {number} targetFriend
    * @return {number}
    */
   smallestChair(times, targetFriend) {
      const friendsOrder = Array.from({ length: times.length }, (_, index) => index);
      friendsOrder.sort((a, b) => times[a][0] - times[b][0]);
      const occupiedChairs = new MinPriorityQueue(x => x[0]);
      const avaibleChairs = new MinPriorityQueue();
      let minChair = 0;

      for (const friendId of friendsOrder) {
         const [start, end] = times[friendId];

         while (!occupiedChairs.isEmpty() && occupiedChairs.front()[0] <= start) {
            const [_, chair] = occupiedChairs.dequeue();
            avaibleChairs.enqueue(chair);
         }
         if (avaibleChairs.isEmpty()) {
            avaibleChairs.enqueue(minChair);
            minChair++;
         }
         const chair = avaibleChairs.dequeue();
         occupiedChairs.enqueue([end, chair]);

         if (friendId === targetFriend)
            return chair
      }
   };
}


const smallestChair = new Solution().smallestChair;
console.log(new Solution().smallestChair([[1, 4], [2, 3], [4, 6]], 1) === 1)
console.log(new Solution().smallestChair([[3, 10], [1, 5], [2, 6]], 0) === 2)