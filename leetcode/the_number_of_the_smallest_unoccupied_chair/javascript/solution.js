import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: heap, list
    *     A: sorting
    * @param {number[][]} times
    * @param {number} targetFriend
    * @return {number}
    */
   smallestChair(times, targetFriend) {
      const friendData = times.map(([start, end], index) => [start, end, index]);
      friendData.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);

      const avaibleChairs = new MinPriorityQueue();
      times.forEach((_, chairId) => {avaibleChairs.enqueue(chairId)});
      const occupiedChairs = new MinPriorityQueue(x => x[0]);

      for (const [start, end, friendId] of friendData) {
         while (occupiedChairs.size() && occupiedChairs.front()[0] <= start) {
            const [_, chairId] = occupiedChairs.dequeue();
            avaibleChairs.enqueue(chairId);
         }
         
         const chairId = avaibleChairs.dequeue();
         occupiedChairs.enqueue([end, chairId]);

         if (friendId === targetFriend)
            return chairId
      }
   };
}


const smallestChair = new Solution().smallestChair;
console.log(new Solution().smallestChair([[1, 4], [2, 3], [4, 6]], 1) === 1)
console.log(new Solution().smallestChair([[3, 10], [1, 5], [2, 6]], 0) === 2)
