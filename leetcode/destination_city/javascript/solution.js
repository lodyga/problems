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
      const srcs = new Set();
      const dsts = new Set();

      for (const [src, dst] of paths) {
         srcs.add(src);
         dsts.add(dst);
      }

      for (const dst of dsts) {
         if (!srcs.has(dst))
            return dst
      }
   };
}


const destCity = new Solution().destCity;
console.log(new Solution().destCity([['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]) === 'Sao Paulo')
console.log(new Solution().destCity([['B', 'C'], ['D', 'B'], ['C', 'A']]) === 'A')
console.log(new Solution().destCity([['A', 'Z']]) === 'Z')
