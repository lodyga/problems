class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(2^n)
    *     Every dfs call contains new string
    * Tags: iterative dfs with backtracking
    * @param {string} word
    * @return {string[][]}
    */
   partition(word) {
      const partition = [];
      const partitionList = [];

      function isPalindrome(left, right) {
         while (left < right) {
            if (word[left] !== word[right])
               return false
            left++;
            right--;
         }
         return true
      }

      function dfs(start) {
         if (start === word.length) {
            partitionList.push(partition.slice());
            return
         }
         for (let index = start; index < word.length; index++) {
            if (isPalindrome(start, index)) {
               partition.push(word.slice(start, index + 1));
               dfs(index + 1)
               partition.pop();
            }
         }
      }

      dfs(0);
      return partitionList
   };
}


console.log(new Solution().partition('aa'), [['a', 'a'], ['aa']])
console.log(new Solution().partition('a'), [['a']])
console.log(new Solution().partition('ab'), [['a', 'b']])
console.log(new Solution().partition('aaa'), [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']])
console.log(new Solution().partition('aab'), [['a', 'a', 'b'], ['aa', 'b']])
console.log(new Solution().partition('aba'), [['a', 'b', 'a'], ['aba']])