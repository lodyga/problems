package codewars.directions_reduction.java;

import java.util.Arrays;

public class DirectionsReduction {
      public static void main(String[] args) {
            System.out.println(Arrays.equals(
                        new Solution().dirReduc(
                                    new String[] { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" }),
                        new String[] { "WEST" }));
            System.out.println(Arrays.equals(
                        new Solution().dirReduc(new String[] { "NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST" }),
                        new String[] { "WEST", "WEST" }));
            System.out.println(Arrays.equals(
                        new Solution().dirReduc(new String[] { "NORTH", "WEST", "SOUTH", "EAST" }),
                        new String[] { "NORTH", "WEST", "SOUTH", "EAST" }));
            System.out.println(Arrays.equals(new Solution().dirReduc(
                        new String[] {}),
                        new String[] {}));
      }
}
