class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const N = houses.length;
      const memo = Array(N + 2).fill(-1);
      memo[N + 1] = 0;
      memo[N] = 0;

      const dfs = (idx) => {
         if (memo[idx] !== -1) {
            return memo[idx];
         }

         const house = houses[idx];
         const skip = dfs(idx + 1);
         const rob = house + dfs(idx + 2);
         
         memo[idx] = Math.max(rob, skip);
         return memo[idx];
      }

      return dfs(0);
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const N = houses.length;
      const cache = Array(N + 2).fill(0);

      for (let idx = N - 1; idx > -1; idx--) {
         const house = houses[idx];
         const skipHouse = cache[idx + 1];
         const robHouse = house + cache[idx + 2];
         cache[idx] = Math.max(robHouse, skipHouse);
      }

      return cache[0];
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const N = houses.length;
      const cache = [0, 0];

      for (let idx = N - 1; idx > -1; idx--) {
         const house = houses[idx];
         const idx1 = (N - idx) % 2;
         const idx2 = (N - 1 - idx) % 2;
         const skipHouse = cache[idx2];
         const robHouse = house + cache[idx1];
         cache[idx1] = Math.max(robHouse, skipHouse);
      }

      return cache[N % 2];
   }
}


const rob = new Solution().rob;
console.log(new Solution().rob1([2]) === 2)
console.log(new Solution().rob1([0]) === 0)
console.log(new Solution().rob1([2, 1]) === 2)
console.log(new Solution().rob1([2, 100, 9, 3, 100]) === 200)
console.log(new Solution().rob1([100, 9, 3, 100, 2]) === 200)
console.log(new Solution().rob1([1, 2, 3, 1]) === 4)
console.log(new Solution().rob1([2, 7, 9, 3, 1]) === 12)
console.log(new Solution().rob1([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]) === 3365)
console.log(new Solution().rob1([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) === 0)
