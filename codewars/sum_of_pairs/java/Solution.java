package codewars.sum_of_pairs.java;

import java.util.Set;
import java.util.HashSet;

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * 
    * @param numbers
    * @param target
    * @return
    */
   int[] sum_pairs(int[] numbers, int target) {
      Set<Integer> uniqueNumbers = new HashSet<>();

      for (int number : numbers) {
         int complement = target - number;
         if (uniqueNumbers.contains(complement)) {
            return new int[] { complement, number };
         } else {
            uniqueNumbers.add(number);
         }
      }
      return null;
   }
}
