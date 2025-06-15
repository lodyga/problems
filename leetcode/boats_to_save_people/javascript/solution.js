class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} people
    * @param {number} limit
    * @return {number}
    */
   numRescueBoats(people, limit) {
      people.sort((a, b) => a - b);
      let left = 0;
      let right = people.length - 1;
      let boatCounter = 0;

      while (left <= right) {
         left += people[left] + people[right] <= limit ? 1 : 0;
         right--;
         boatCounter++;
      }
      return boatCounter
   };
}
const numRescueBoats = new Solution().numRescueBoats;


console.log(new Solution().numRescueBoats([1, 2], 3) === 1)
console.log(new Solution().numRescueBoats([3, 2, 2, 1], 3) === 3)
console.log(new Solution().numRescueBoats([3, 5, 3, 4], 5) === 4)
console.log(new Solution().numRescueBoats([3, 2, 3, 2, 2], 6) === 3)
console.log(new Solution().numRescueBoats([2, 4], 5) === 2)