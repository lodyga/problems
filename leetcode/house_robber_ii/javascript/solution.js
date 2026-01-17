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
      if (houses.length <= 3) {
         return Math.max(...houses)
      }
      const rob2 = (houses) => {
         const cache = [0, 0];
         for (let index = houses.length - 1; index > -1; index--) {
            const house = houses[index];
            const skipHouse = cache[0];
            const robHouse = house + cache[1];
            [cache[0], cache[1]] = [Math.max(skipHouse, robHouse), cache[0]];
         }
         return cache[0]
      };

      return Math.max(
         rob2(houses.slice(0, -1)),
         rob2(houses.slice(1,))
      )
   };
}


const rob = new Solution().rob;
console.log(new Solution().rob([2, 3, 2]) === 3)
console.log(new Solution().rob([1, 2, 3, 1]) === 4)
console.log(new Solution().rob([1, 2, 3]) === 3)
console.log(new Solution().rob([1]) === 1)
console.log(new Solution().rob([0, 0]) === 0)
console.log(new Solution().rob([1, 3, 1, 3, 100]) === 103)
