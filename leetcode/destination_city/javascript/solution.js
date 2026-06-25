class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {string[][]} paths
    * @return {string}
    */
   destCity(paths) {
      const srcCities = new Set();

      for (const [src, ] of paths) {
         srcCities.add(src);
      }
      
      for (const [, dst] of paths) {
         if (!srcCities.has(dst))
            return dst;
      }
   }
}


const destCity = new Solution().destCity;
console.log(new Solution().destCity([['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]) === 'Sao Paulo')
console.log(new Solution().destCity([['B', 'C'], ['D', 'B'], ['C', 'A']]) === 'A')
console.log(new Solution().destCity([['A', 'Z']]) === 'Z')
