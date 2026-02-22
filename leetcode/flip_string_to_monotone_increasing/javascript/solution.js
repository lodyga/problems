class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: array
    *     A: top-down
    * @param {string} text
    * @return {number}
    */
   minFlipsMonoIncr(text) {
      const memo = Array.from({ length: text.length }, () => [-1, -1]);
      memo.push([0, 0]);

      const dfs = (index, canFlipTo1) => {
         const flipIndex = canFlipTo1 ? 1 : 0;
         if (memo[index][flipIndex] !== -1) {
            return memo[index][flipIndex]
         }

         const letter = text[index];
         let res;

         if (letter === '0') {
            if (canFlipTo1) {
               res = dfs(index + 1, true);
            } else {
               res = 1 + dfs(index + 1, false);
            }
         } else if (letter === '1') {
            res = dfs(index + 1, false);

            if (canFlipTo1) {
               res = Math.min(res, 1 + dfs(index + 1, true));
            }
         }

         memo[index][flipIndex] = res
         return res
      }

      return dfs(0, true)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {string} text
    * @return {number}
    */
   minFlipsMonoIncr(text) {
      let ones = 0;
      let res = 0;
      
      for (const char of text)
         char === '1' ? ones += 1 : res = Math.min(ones, res + 1)
      return res
   };
}


const minFlipsMonoIncr = new Solution().minFlipsMonoIncr;
console.log(new Solution().minFlipsMonoIncr('00') === 0)
console.log(new Solution().minFlipsMonoIncr('11') === 0)
console.log(new Solution().minFlipsMonoIncr('00110') === 1)
console.log(new Solution().minFlipsMonoIncr('010110') === 2)
console.log(new Solution().minFlipsMonoIncr('00011000') === 2)
console.log(new Solution().minFlipsMonoIncr('0101100011') === 3)
console.log(new Solution().minFlipsMonoIncr('10011111110010111011') === 5)
