package leetcode.valid_palindrome.java;

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    */
   boolean isPalindrome(String text) {
      if (text.isEmpty()) {
         return true;
      }

      int left = 0;
      int right = text.length() - 1;

      while (left < right) {
         while (left < right &&
               isPunctuation(text.charAt(left))) {
            left++;
         }
         while (left < right &&
               isPunctuation(text.charAt(right))) {
            right--;
         }

         if (Character.toLowerCase(text.charAt(left)) != Character.toLowerCase(text.charAt(right))) {
            return false;
         } else {
            left++;
            right--;
         }
      }
      return true;
   }

   private static boolean isPunctuation(char chr) {
      return !(Character.isDigit(chr) ||
            Character.isLetter(chr));
   }

   
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: regex
    */
   boolean isPalindromeUsingRegex(String text) {
      String cleaned_text = text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
      String reversed_text = new StringBuilder(cleaned_text).reverse().toString();
      return cleaned_text.equals(reversed_text);
   }
}