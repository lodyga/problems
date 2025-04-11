package codewars.sum_of_pairs.java;

import java.util.Arrays;

public class SumOfPairs {
   public static void main(String[] args) {
      Solution solution = new Solution();
      System.out.println(Arrays.equals(solution.sum_pairs(new int[] { 10, 5, 2, 3, 7, 5 }, 10), new int[] { 3, 7 }));
      System.out.println(Arrays.equals(solution.sum_pairs(new int[] { 1, 4, 8, 7, 3, 15 }, 8), new int[] { 1, 7 }));
      System.out.println(Arrays.equals(solution.sum_pairs(new int[] { 1, -2, 3, 0, -6, 1 }, -6), new int[] { 0, -6 }));
      System.out.println(Arrays.equals(solution.sum_pairs(new int[] { 20, -13, 40 }, -7), null));
      System.out.println(Arrays.equals(solution.sum_pairs(new int[] { 1, 2, 3, 4, 1, 0 }, 2), new int[] { 1, 1 }));
      System.out.println(Arrays.equals(solution.sum_pairs(new int[] { 4, -2, 3, 3, 4 }, 8), new int[] { 4, 4 }));
      System.out.println(Arrays.equals(solution.sum_pairs(new int[] { 0, 2, 0 }, 0), new int[] { 0, 0 }));
      System.out.println(Arrays.equals(solution.sum_pairs(new int[] { 5, 9, 13, -3 }, 10), new int[] { 13, -3 }));

   }
}