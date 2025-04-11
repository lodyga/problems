package leetcode.valid_anagram.java;

public class Valid_Anagram {
   public static void main(String[] args) {
      Solution solution = new Solution();
      System.out.println(solution.isAnagramUsingHashArray("anagram", "nagaram") == true);
      System.out.println(solution.isAnagramUsingHashArray("rat", "car") == false);
      System.out.println(solution.isAnagramUsingHashArray("", "") == true);
   }
}
