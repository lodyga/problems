# include <string>
# include <vector>
# include <stack>
# include <unordered_map>
# include <cassert>

class Solution {
public:
   /**
   * Time complexity: O(n)
   * Auxiliary space complexity: O(n)
   * Tags: stack
   */
   std::vector<std::string> dirReduc(const std::vector<std::string>& directionList) {
      std::stack<std::string> visitedDirections;
      std::unordered_map<std::string, std::string> oppositeDirection = {
         {"NORTH", "SOUTH"},
         {"SOUTH", "NORTH"},
         {"EAST", "WEST"},
         {"WEST", "EAST"} };

      for (const std::string& direction : directionList) {
         if (!visitedDirections.empty() &&
            visitedDirections.top() == oppositeDirection[direction]) {
            visitedDirections.pop();
         }
         else {
            visitedDirections.push(direction);
         }
      }
      // Convert stack to vector
      std::vector<std::string> visitedDirectionsVector;
      while (!visitedDirections.empty()) {
         visitedDirectionsVector.insert(visitedDirectionsVector.begin(), visitedDirections.top());
         visitedDirections.pop();
      }
      return visitedDirectionsVector;
   }
};

int main() {
   assert((Solution().dirReduc({ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" }) == std::vector<std::string> { "WEST" }));
   assert((Solution().dirReduc({ "NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST" }) == std::vector<std::string> {  "WEST", "WEST" }));
   assert((Solution().dirReduc({ "NORTH", "WEST", "SOUTH", "EAST" }) == std::vector<std::string> { "NORTH", "WEST", "SOUTH", "EAST" }));
   assert((Solution().dirReduc({}) == std::vector<std::string> {}));
   return 0;
}
