class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    *     Output: O(2^n)
    * Tags:
    *     DS: list
    *     A: DFS with backtracking
    * @param {string} text
    * @return {string[][]}
    */
   partition(text) {
      const isPalindrome = (left, right) => {
         while (left < right) {
            if (text[left] !== text[right]) return false
            left++;
            right--;
         }
         return true
      }

      const partitioned = [];
      const res = [];

      const backtrack = (start) => {
         if (start === text.length) {
            res.push(partitioned.slice());
            return
         }

         for (let idx = start; idx < text.length; idx++) {
            if (isPalindrome(start, idx)) {
               partitioned.push(text.slice(start, idx + 1));
               backtrack(idx + 1);
               partitioned.pop();
            }
         }
      }
      backtrack(0);
      return res
   };
}


const partition = new Solution().partition;
console.log(new Solution().partition('aa').toString() === [['a', 'a'], ['aa']].toString())
console.log(new Solution().partition('a').toString() === [['a']].toString())
console.log(new Solution().partition('ab').toString() === [['a', 'b']].toString())
console.log(new Solution().partition('aaa').toString() === [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']].toString())
console.log(new Solution().partition('aab').toString() === [['a', 'a', 'b'], ['aa', 'b']].toString())
console.log(new Solution().partition('aba').toString() === [['a', 'b', 'a'], ['aba']].toString())
