class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: hash map
    * @param {string} text
    * @return {number}
    */
   longestPalindrome(text) {
      const letterFrequency = new Map();
      for (const letter of text)
         letterFrequency.set(letter, (letterFrequency.get(letter) || 0) + 1);

      let hasOdd = false;
      let palindromeLenght = 0;

      for (const frequency of letterFrequency.values()) {
         if (frequency % 2) {
            hasOdd = true;
            palindromeLenght += frequency - 1;
         }
         else
            palindromeLenght += frequency;
      }
      return palindromeLenght + hasOdd
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: hash set
    * @param {string} text
    * @return {number}
    */
   longestPalindrome(text) {
      let palindromeLenght = 0;
      const letterSet = new Set();

      for (const letter of text) {
         if (letterSet.has(letter)) {
            palindromeLenght += 2;
            letterSet.delete(letter);
         }
         else
            letterSet.add(letter);
      }

      return palindromeLenght + Boolean(letterSet.size)
   };
}


const longestPalindrome = new Solution().longestPalindrome;
console.log(new Solution().longestPalindrome('abccccdd') === 7)
console.log(new Solution().longestPalindrome('a') === 1)
console.log(new Solution().longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth') === 983)
