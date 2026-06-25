class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {number} n
    * @param {number[][]} trust
    * @return {number}
    */
   findJudge(n, trust) {
      // [person: votes]
      const votes = Array(n).fill(0);

      for (const [trusting, trusted] of trust) {
         votes[trusting - 1]--;
         votes[trusted - 1]++;
      }

      for (let idx = 0; idx < n; idx++) {
         if (votes[idx] === n - 1)
            return idx + 1;
      }

      return -1;
   }
}


class Solution {
   /**
    * Time complexity: O(n) 
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, hash set
    *     A: iteration
    * @param {number} n
    * @param {number[][]} trust
    * @return {number}
    */
   findJudge(n, trust) {
      if (n === 1 && trust.length === 0)
         return 1

      const trustFreq = new Map();
      const trusters = new Set();

      for (const [trusting, trusted] of trust) {
         trustFreq.set(trusted, (trustFreq.get(trusted) || 0) + 1);
         trusters.add(trusting);
      }
      for (const [key, val] of trustFreq.entries())
         if (val === n - 1 && !trusters.has(key))
            return key;

      return -1;
   }
}


const findJudge = new Solution().findJudge;
console.log(new Solution().findJudge(2, [[1, 2]]) === 2)
console.log(new Solution().findJudge(3, [[1, 3], [2, 3]]) === 3)
console.log(new Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]) === -1)
console.log(new Solution().findJudge(3, [[1, 2], [2, 3]]) === -1)
console.log(new Solution().findJudge(1, []) === 1)
console.log(new Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) === 3)
