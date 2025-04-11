package leetcode.contains_duplicate.java;

import java.util.HashSet;
import java.util.Set;

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    */
   public boolean containsDuplicate(int[] numbers) {
      Set<Integer> uniqueNumbers = new HashSet<>();
      for (int number : numbers) {
         if (uniqueNumbers.contains(number)) {
            return true;
         } else {
            uniqueNumbers.add(number);
         }
      }
      return false;
   }
}
