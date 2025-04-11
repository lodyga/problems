package leetcode.valid_palindrome.java;

public class ValidPalindrome {
   public static void main(String[] args) {
      Solution solution = new Solution();
      System.out.println(! solution.isPalindrome("race a car"));
      System.out.println(solution.isPalindrome(" "));
      System.out.println(! solution.isPalindrome("0P"));
      System.out.println(solution.isPalindrome("ab_a"));
   }
}