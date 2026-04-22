class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: string, list
    *     A: two pointers
    * @param {string} s
    * @param {number[]} spaces
    * @return {}
    */
   addSpaces(s, spaces) {
      const words = [];
        let start = 0;

        for (const end of spaces) {
           words.push(s.slice(start, end));
           start = end;
         }
           
        words.push(s.slice(start, s.length));

        return words.join(' ')
   };
}


const addSpaces = new Solution().addSpaces;
console.log(new Solution().addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]) === "Leetcode Helps Me Learn")
console.log(new Solution().addSpaces("icodeinpython", [1, 5, 7, 9]) === "i code in py thon")
console.log(new Solution().addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6]) ===" s p a c i n g")
