class Solution {
   /**
    * Time complexity: O(n)
    *     n: brick count
    * Auxiliary space complexity: O(m)
    *     m: distinct crack count
    * Tags: hash map
    * @param {number[][]} wall
    * @return {number}
    */
   leastBricks(wall) {
      // {crack position: vertical crack count}
      const cracks = new Map([[0, 0]]);
      for (const row of wall) {
         let crack = 0;
         for (const brick of row.slice(0, row.length - 1)) {
            crack += brick;
            cracks.set(crack, (cracks.get(crack) || 0) + 1);
         }
      }
      return wall.length - Math.max(...cracks.values())
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
