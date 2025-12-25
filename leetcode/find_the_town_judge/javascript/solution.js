class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: hash map, hash set
    *     A: iteration
    * @param {number} n
    * @param {number[][]} trustList
    * @return {number}
    */
   findJudge(n, trustList) {
      if (n === 1 && trustList.length === 0)
         return 1

      const trustFreq = new Map();
      const trusters = new Set();

      for (const [a, b] of trustList) {
         trustFreq.set(b, (trustFreq.get(b) || 0) + 1);
         trusters.add(a);
      }
      for (const [key, val] of trustFreq.entries())
         if (val === n - 1 && !trusters.has(key))
            return key

      return -1
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: array
    *     A: iteration
    * @param {number} n
    * @param {number[][]} trustList
    * @return {number}
    */
   findJudge(n, trustList) {
      // [person: votes]
      const votes = Array(n).fill(0);

      for (const [a, b] of trustList) {
         votes[a - 1] = -1;
         if (votes[b - 1] !== -1)
            votes[b - 1]++;
      }

      for (let index = 0; index < n; index++) {
         if (votes[index] === n - 1)
            return index + 1
      }
      return -1
   };
}


const findJudge = new Solution().findJudge;
console.log(new Solution().findJudge(2, [[1, 2]]) === 2)
console.log(new Solution().findJudge(3, [[1, 3], [2, 3]]) === 3)
console.log(new Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]) === -1)
console.log(new Solution().findJudge(3, [[1, 2], [2, 3]]) === -1)
console.log(new Solution().findJudge(1, []) === 1)
console.log(new Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) === 3)
