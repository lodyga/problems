class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number} n
    * @param {number} k
    * @return {number}
    */
   kthGrammar(n, k) {
      k--;
      let left = 0;
      let right = 2 ** (n - 1) - 1;
      let res = 0;

      while (left < right) {
         const mid = (left + right) >> 1;

         if (k <= mid)
            right = mid;
         else {
            res = res ? 0 : 1;
            left = mid + 1;
         }
      }
      return res
   };
}


const kthGrammar = new Solution().kthGrammar;
console.log(new Solution().kthGrammar(1, 1) === 0)
console.log(new Solution().kthGrammar(2, 1) === 0)
console.log(new Solution().kthGrammar(2, 2) === 1)
console.log(new Solution().kthGrammar(30, 434991989) === 0)
