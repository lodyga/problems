package codewars.directions_reduction.java;

import java.util.Stack;
import java.util.Map;

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    */
   public String[] dirReduc(String[] directionList) {
      Stack<String> visitedDirections = new Stack<>();
      Map<String, String> oppositeDirection = Map.of(
            "NORTH", "SOUTH",
            "SOUTH", "NORTH",
            "EAST", "WEST",
            "WEST", "EAST");

      for (String direction : directionList) {
         if (!visitedDirections.isEmpty() &&
               visitedDirections.peek().equals(oppositeDirection.get(direction))) {
            visitedDirections.pop();
         } else {
            visitedDirections.push(direction);
         }
      }
      return visitedDirections.toArray(new String[0]);
   }
}
