class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: hash map
    *     A: top-down
    * @param {number} num
    * @return {number}
    */
   tribonacci(num) {
      const memo = new Map([[0, 0], [1, 1], [2, 1]]);

      const dfs = (num) => {
         if (memo.has(num)) {
            return memo.get(num)
         }
         const triplet = dfs(num - 1) + dfs(num - 2) + dfs(num - 3);
         memo.set(num, triplet);
         return triplet
      }
      return dfs(num)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: list
    *     A: bottom-up
    * @param {number} num
    * @return {number}
    */
   tribonacci(num) {
      const cache = [0, 1, 1];

      for (let index = 3; index < num + 1; index++) {
         cache.push(
            cache[index - 1] +
            cache[index - 2] +
            cache[index - 3]
         );
      }
      return cache[num]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: array
    *     A: bottom-up
    * @param {number} number
    * @return {number}
    */
   tribonacci(number) {
      const cache = [0, 1, 1];

      for (let index = 3; index < number + 1; index++) {
         cache[index % 3] = cache[0] + cache[1] + cache[2];
      }
      return cache[number % 3]
   };
}


const tribonacci = new Solution().tribonacci;
console.log(new Solution().tribonacci(0) === 0)
console.log(new Solution().tribonacci(3) === 2)
console.log(new Solution().tribonacci(4) === 4)
console.log(new Solution().tribonacci(25) === 1389537)
console.log(new Solution().tribonacci(31) === 53798080)
console.log(new Solution().tribonacci(35) === 615693474)
