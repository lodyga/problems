class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, hash set
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   countPalindromicSubsequence(text) {
      const palindromeSet = new Set();
      const leftLetters = new Set();
      const rightLetters = new Map();

      for (const letter of text) {
         rightLetters.set(letter, (rightLetters.get(letter) || 0) + 1);
      }

      for (const middleLetter of text) {
         rightLetters.set(middleLetter, rightLetters.get(middleLetter) - 1);

         if (rightLetters.get(middleLetter) === 0) {
            rightLetters.delete(middleLetter);
         }

         for (let i = 0; i < 26; i++) {
            const letter = String.fromCharCode('a'.charCodeAt(0) + i);

            if (
               leftLetters.has(letter) &&
               rightLetters.has(letter)
            ) {
               palindromeSet.add(letter + middleLetter);
            }
         }

         leftLetters.add(middleLetter);
      }

      return palindromeSet.size;
   };
}


const countPalindromicSubsequence = new Solution().countPalindromicSubsequence;
console.log(new Solution().countPalindromicSubsequence('aabca') === 3)
console.log(new Solution().countPalindromicSubsequence('adc') === 0)
console.log(new Solution().countPalindromicSubsequence('bbcbaba') === 4)
console.log(new Solution().countPalindromicSubsequence('zqpppgacudvmqekmefkzyyfrffeylqrwxlupvskyonqsbclwwgnzbktzelwuhehxrxmqcnepxokialxxwciqsetcsqcsszpeobeiwwedtbisyhexyatammupmfrllpawhqvfebjdappicczehrsooztjatixvtvbmdwikffbozncspuslwgoqypmsmvwghfdmutfpkbjufqrgbhotcikoyvfvxmmadelwxmvybnoroapixubdvijnepeduiwshcwjvhnejafcnuxeimwiiucznzfakwdibwwixcttatqffhnurhecyocoohyuoeixobaxbjcksxqrljiftvcxtocusciqtmydxgjexiwimbcmvhjonkscobhlpggembfslzoisertsvcpiclikprpviqbfdptvtrlhqlfwhurxysxzppnwwbxzaozchalpqsklfedovjkhwdaqdxrzdduwxsyqllvkflamtshyoaamjpzcsnwthnnpgqrrroppxnalxoijzhesphugqporhtamdbugqhgtpxtrjeugenazzpvvtkjrsepvbgvbmmmyxgrkgnlhujinycnjvpqhhugplrgrunrziaabknrjsgaqbpxfpdycpjtquecehrblzurruguhbkzgvebzfkqcolpclgabsuamqaakdikasumksvbfjrudnzihbzqjwivthfozrhkcrmxleaazgkuqmzvzaiiskfrnywntgbtmaxqgqaqxvcpvbvcpqbfivtkdroizfbebhtejegpduqjewcaysphsumddhlgerpspcvhkoezzqwznmqfbcdvxmexbjfgqxlcbneanbglpktxfcfgkfxbpblfpejlfjhiaohcmktfheuyxpof') === 676)
