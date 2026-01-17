class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: brute-force
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const dfs = (index) => {
         if (
            index === houses.length || 
            index === houses.length + 1
         )
            return 0
         
         const house = houses[index];
         const skipHouse = dfs(index + 1);
         const robHouse = house + dfs(index + 2);
         return Math.max(robHouse, skipHouse)
      }
      return dfs(0)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const memo = new Map(
         [[houses.length, 0], [houses.length + 1, 0]]
      );

      const dfs = (index) => {
         if (memo.has(index))
            return memo.get(index)
         
         const house = houses[index];
         const skipHouse = dfs(index + 1);
         const robHouse = house + dfs(index + 2);
         memo.set(index, Math.max(robHouse, skipHouse));
         return memo.get(index)
      }
      return dfs(0)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} houses
    * @return {number}
    */
   rob1(houses) {
      const memo = Array(houses.length + 2).fill(-1);
      memo[houses.length] = 0
      memo[houses.length + 1] = 0

      const dfs = (index) => {
         if (memo[index] !== -1)
            return memo[index]
         
         const house = houses[index];
         const skipHouse = dfs(index + 1);
         const robHouse = house + dfs(index + 2);
         memo[index] = Math.max(robHouse, skipHouse);
         return memo[index]
      }
      return dfs(0)
   };

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
      const cache = Array(houses.length + 2).fill(0);

      for (let index = houses.length - 1; index > -1; index--) {
         const house = houses[index];
         const skipHouse = cache[index + 1]
         const robHouse = houses[index] + cache[index + 2];
         cache[index] = Math.max(robHouse, skipHouse);
      }
      return cache[0]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const cache = [0, 0];
      const N = houses.length;

      for (let index = houses.length - 1; index > -1; index--) {
         const house = houses[index]
            const index1 = (N - index) % 2
            const index2 = (N - 1 - index) % 2
            const skipHouse = cache[index2];
            const robHouse = house + cache[index1];
            cache[index1] = Math.max(robHouse, skipHouse);
      }
      return cache[N % 2]
   };
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
