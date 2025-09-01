class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[][]} triplets
    * @param {number[]} target
    * @return {boolean}
    */
   mergeTriplets(triplets, target) {
      const [targetA, targetB, targetC] = target;
      let aFound = false;
      let bFound = false;
      let cFound = false;

      for (const [a, b, c] of triplets) {
         if (
            a > targetA ||
            b > targetB ||
            c > targetC
         )
            continue

         if (a === targetA)
            aFound = true
         if (b === targetB)
            bFound = true
         if (c === targetC)
            cFound = true
         
         if (aFound && bFound && cFound)
            return true
      }
      return false
   };
}
const mergeTriplets = new Solution().mergeTriplets;


console.log(new Solution().mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) === true)
console.log(new Solution().mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) === false)
console.log(new Solution().mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]) === true)