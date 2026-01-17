class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[][]} triplets
    * @param {number[]} target
    * @return {boolean}
    */
   mergeTriplets(triplets, target) {
      const [tA, tB, tC] = target;
      let [isA, isB, isC] = [false, false, false];

      for (const [a, b, c] of triplets) {
         if (a > tA || b > tB || c > tC)
            continue

         isA = isA || a === tA;
         isB = isB || b === tB;
         isC = isC || c === tC;

         if (isA && isB && isC)
            return true
      }
      return false
   };
}


const mergeTriplets = new Solution().mergeTriplets;
console.log(new Solution().mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) === true)
console.log(new Solution().mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) === false)
console.log(new Solution().mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]) === true)
