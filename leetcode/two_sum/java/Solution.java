package leetcode.two_sum.java;

import java.util.HashMap;

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * 
    * @param numbers
    * @param target
    * @return
    */
   int[] twoSum(int[] numbers, int target) {
      HashMap<Integer, Integer> seenNumbers = new HashMap<>();
      for (int index = 0; index < numbers.length; index++) {
         int number = numbers[index];
         int complement = target - number;
         if (seenNumbers.containsKey(complement)) {
            return new int[] { seenNumbers.get(complement), index };
         } else {
            seenNumbers.put(number, index);
         }
      }
      return null;
   }
}
