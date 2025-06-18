class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number} n
    * @param {number} k
    * @return {number}
    */
   kthGrammar(n, k) {
      let left = 1;
      let right = 2 ** (n - 1);
      let value = 0;

      while (left < right) {
         const middle = (left + right) >> 1;

         if (k <= middle)
            right = middle;
         else {
            left = middle + 1;
            value = value ? 0 : 1;
         }
      }
      return value
   };
}


console.log(new Solution().kthGrammar(1, 1) === 0)
console.log(new Solution().kthGrammar(2, 1) === 0)
console.log(new Solution().kthGrammar(2, 2) === 1)
console.log(new Solution().kthGrammar(30, 434991989) === 0)