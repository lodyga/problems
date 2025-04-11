package leetcode.valid_anagram.java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Algorithm: Hash Array Frequency Counter
    */
   protected boolean isAnagramUsingHashArray(String text1, String text2) {
      if (text1.length() != text2.length())
         return false;

      int[] frequencies = new int[26];
      for (int index = 0; index < text1.length(); index++) {
         frequencies[text1.charAt(index) - 'a']++;
         frequencies[text2.charAt(index) - 'a']--;
      }

      for (int frequency : frequencies) {
         if (frequency != 0)
            return false;
      }

      return true;
   }

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1) | (lowercase English letters)
    * Algorithm: HashMap Frequency Counter
    */
   protected boolean isAnagramUsingHashMap(String text1, String text2) {
      if (text1.length() != text2.length())
         return false;
      Map<Character, Integer> text1LetterCounter = counter(text1);
      Map<Character, Integer> text2LetterCounter = counter(text2);
      return text1LetterCounter.equals(text2LetterCounter);
   }

   Map<Character, Integer> counter(String text) {
      Map<Character, Integer> letterCounter = new HashMap<>();
      for (char key : text.toCharArray()) {
         int frequency = letterCounter.getOrDefault(key, 0) + 1;
         letterCounter.put(key, frequency);
      }
      return letterCounter;
   }

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Algorithm: Sorting Comparison
    */
   protected boolean isAnagram_Using_Sorting(String text1, String text2) {
      if (text1.length() != text2.length())
         return false;
      char[] text1Array = text1.toCharArray();
      char[] text2Array = text2.toCharArray();
      Arrays.sort(text1Array);
      Arrays.sort(text2Array);
      return Arrays.equals(text1Array, text2Array);
   }
}