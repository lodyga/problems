class Solution {
   /**
    * Time complexity: O(n4^n)
    *     Up to 4 letters in one digit
    * Auxiliary space complexity: O(n)
    * Tags: iteration dfs with backtracking
    * @param {string} digits
    * @return {}
    */
   letterCombinations(digits) {
      if (digits.length === 0)
         return []
      const combination = [];
      const combinationList = [];
      const digitToLetter = new Map([
         ['2', 'abc'],
         ['3', 'def'],
         ['4', 'ghi'],
         ['5', 'jkl'],
         ['6', 'mno'],
         ['7', 'pqrs'],
         ['8', 'tuv'],
         ['9', 'wxyz']
      ]);

      dfs(0);
      return combinationList

      function dfs(index) {
         if (index === digits.length) {
            combinationList.push(combination.join(''))
            return
         }

         const digit = digits[index];
         for (const letter of digitToLetter.get(digit)) {
            combination.push(letter);
            dfs(index + 1)
            combination.pop();
         }
      }
   };
}


console.log(new Solution().letterCombinations('2'), ['a', 'b', 'c'])
console.log(new Solution().letterCombinations('23'), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
console.log(new Solution().letterCombinations(''), [])