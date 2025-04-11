package leetcode.split_a_string_in_balanced_strings.java;

public class SplitAStringInBalancedStrings {
   public static void main(String[] args) {
      Solution solution = new Solution();
      System.out.println(solution.balancedStringSplit("RLRRLLRLRL") == 4);
      System.out.println(solution.balancedStringSplit("RLRRRLLRLL") == 2);
      System.out.println(solution.balancedStringSplit("LLLLRRRR") == 1);
   }
}