package leetcode.two_sum.java;

import java.util.Arrays;

public class TwoSum {
   public static void main(String[] args) {
      Solution solution = new Solution();
      System.out.println(Arrays.equals(solution.twoSum(new int[] { 2, 7, 11, 15 }, 9), new int[] { 0, 1 }));
      System.out.println(Arrays.equals(solution.twoSum(new int[] { 3, 2, 4 }, 6), new int[] { 1, 2 }));
      System.out.println(Arrays.equals(solution.twoSum(new int[] { 3, 3 }, 6), new int[] { 0, 1 }));
      System.out.println(Arrays.equals(solution.twoSum(new int[] { 3, 3 }, 7), null));
   }
}
