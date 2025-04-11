package leetcode.split_a_string_in_balanced_strings.java;

public class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    */
   int balancedStringSplit(String sides) {
      int sideCounter = 0;
      int balancedStringCounter = 0;

      for (char side : sides.toCharArray()) {
         if (side == 'R') {
            sideCounter++;
         } else {
            sideCounter--;
         }
         if (sideCounter == 0) {
            balancedStringCounter++;
         }
      }
      return balancedStringCounter;
   }
}
