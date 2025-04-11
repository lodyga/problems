# include <string>
# include <cassert>

class Solution {
public:
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    */
   int balancedStringSplit(const std::string& sides) {
      int sideCounter = 0;
      int balancedStringCounter = 0;

      for (const char& side : sides) {
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
};

int main() {
   Solution solution;
   assert((solution.balancedStringSplit("RLRRLLRLRL"), 4));
   assert((solution.balancedStringSplit("RLRRRLLRLL"), 2));
   assert((solution.balancedStringSplit("LLLLRRRR"), 1));
   return 0;
}