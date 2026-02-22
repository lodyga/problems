class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     hash map
    * @param {string} text
    * @return {number}
    */
   longestPalindrome(text) {
      const letterFreq = new Map();
      let isOdd = 0;
      let res = 0;

      for (const letter of text)
         letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);

      for (const freq of letterFreq.values()) {
         if (freq % 2) {
            res += freq - 1;
            isOdd = 1;
         }
         else
            res += freq;
      }
      return res + isOdd
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     hash set
    * @param {string} text
    * @return {number}
    */
   longestPalindrome(text) {
      let res = 0;
      const letterSet = new Set();

      for (const letter of text) {
         if (letterSet.has(letter)) {
            res += 2;
            letterSet.delete(letter);
         } else {
            letterSet.add(letter);
         }
      }

      return res + Boolean(letterSet.size)
   };
}


const longestPalindrome = new Solution().longestPalindrome;
console.log(new Solution().longestPalindrome('abccccdd') === 7)
console.log(new Solution().longestPalindrome('a') === 1)
console.log(new Solution().longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth') === 983)
