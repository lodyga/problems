package leetcode.valid_parentheses.java;

import java.util.Stack;
import java.util.Map;

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * 
    * @param numbers
    * @param target
    * @return
    */
   public boolean isValid(String bracketList) {
      if (bracketList.length() % 2 != 0) {
         return false;
      }

      Stack<Character> stackedBrackets = new Stack<>();
      Map<Character, Character> closingBracket = Map.of(
            ')', '(',
            ']', '[',
            '}', '{');
      for (char bracket : bracketList.toCharArray()) {
         if (closingBracket.containsKey(bracket)) {
            if (!stackedBrackets.isEmpty() &&
                  stackedBrackets.peek() == closingBracket.get(bracket)) {
               stackedBrackets.pop();
            } else {
               return false;
            }
         } else {
            stackedBrackets.push(bracket);
         }
      }
      return stackedBrackets.isEmpty();
   }
}
