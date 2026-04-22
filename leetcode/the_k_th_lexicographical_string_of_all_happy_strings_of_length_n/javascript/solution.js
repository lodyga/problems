class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list, string
    *     A: backtracking
    * @param {number} n
    * @param {number} k
    * @return {}
    */
   getHappyString(n, k) {
      const chars = [];

      const backtrack = (idx, prev) => {
         if (idx == n) {
            k--;
            return !k
         }

         for (const char of "abc") {
            if (char != prev) {
               chars.push(char);

               if (backtrack(idx + 1, char)) {
                  return true
               }

               chars.pop();
            }
         }
      }

      backtrack(0, null)
      return chars.join('')
   };
}


const getHappyString = new Solution().getHappyString;
console.log(new Solution().getHappyString(1, 3) === 'c')
console.log(new Solution().getHappyString(1, 4) === '')
console.log(new Solution().getHappyString(3, 9) === 'cab')
