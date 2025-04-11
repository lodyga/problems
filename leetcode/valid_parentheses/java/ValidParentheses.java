package leetcode.valid_parentheses.java;

public class ValidParentheses {
   public static void main(String[] args) {
      System.out.println(new Solution().isValid("()") == true);
      System.out.println(new Solution().isValid("({})") == true);
      System.out.println(new Solution().isValid("(]") == false);
      System.out.println(new Solution().isValid("(})") == false);
      System.out.println(new Solution().isValid("([)") == false);
      System.out.println(new Solution().isValid("") == true);
      System.out.println(new Solution().isValid("[") == false);
   }
}
