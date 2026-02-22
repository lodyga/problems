class Solution {
   /**
    * Time complexity: O(n)
    *     n: brick count
    * Auxiliary space complexity: O(m)
    *     m: distinct crack count
    * Tags:
    *     DS: hash map
    *     A: prefix sum
    * @param {number[][]} wall
    * @return {number}
    */
   leastBricks(wall) {
      // {crack position: vertical crack count}
      const crackFreq = new Map([[0, 0]]);
      
      for (const brickRow of wall) {
         let prefix = 0;

         for (let index = 0; index < brickRow.length - 1; index++) {
            prefix += brickRow[index];
            crackFreq.set(prefix, (crackFreq.get(prefix) || 0) + 1);
         }
      }
      
      return wall.length - Math.max(...crackFreq.values())
   };
}


const leastBricks = new Solution().leastBricks;
console.log(new Solution().leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]) === 2)
console.log(new Solution().leastBricks([[1], [1], [1]]) === 3)
console.log(new Solution().leastBricks([[2147483647, 2147483647, 2147483647, 2147483647]]) === 0)
console.log(new Solution().leastBricks([[1]]) === 1)
console.log(new Solution().leastBricks([[1000]]) === 1)
console.log(new Solution().leastBricks([[100000000, 100000000], [100000000, 100000000]]) === 0)
console.log(new Solution().leastBricks([[2], [2], [2]]) === 3)
