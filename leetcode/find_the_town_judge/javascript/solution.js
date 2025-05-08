class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set, hash map
    * @param {number} peopleCount
    * @param {number[][]} trustList
    * @return {number}
    */
   findJudge(peopleCount, trustList) {
      if (peopleCount === 1 && trustList.length === 0)
         return 1

      const trustees = new Set();
      const trusters = new Map();

      for (const [trustee, truster] of trustList) {
         trustees.add(trustee);
         trusters.set(truster, (trusters.get(truster) || 0) + 1)
      }

      for (const [truster, trustier_approval] of trusters.entries()) {
         if (
            !trustees.has(truster) &&
            trusters.get(truster) === peopleCount - 1
         ) {
            return truster
         }
      }
      return -1
   };
}
const findJudge = new Solution().findJudge;


console.log(new Solution().findJudge(2, [[1, 2]]), 2)
console.log(new Solution().findJudge(3, [[1, 3], [2, 3]]), 3)
console.log(new Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]), -1)
console.log(new Solution().findJudge(3, [[1, 2], [2, 3]]), -1)
console.log(new Solution().findJudge(1, []), 1)
console.log(new Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]), 3)