# include <string>
# include <stack>
# include <unordered_map>
# include <cassert>

class Solution {
public:
   bool isValid(std::string bracketList) {
      if (bracketList.size() % 2 != 0) return false;

      std::stack<char> stackedBrackets;
      std::unordered_map<char, char> closingBracket = {
         {')', '('},
         {']', '['},
         {'}', '{'},
      };

      for (char bracket : bracketList) {
         if (closingBracket.count(bracket)) {
            if (!stackedBrackets.empty() &&
               stackedBrackets.top() == closingBracket[bracket]) {
               stackedBrackets.pop();
            }
            else {
               return false;
            }
         }
         else {
            stackedBrackets.push(bracket);
         }
      }
      return stackedBrackets.empty();
   }
};

int main() {
   Solution solution;
   assert((Solution().isValid("()") == true));
   assert((Solution().isValid("({})") == true));
   assert((Solution().isValid("(]") == false));
   assert((Solution().isValid("(})") == false));
   assert((Solution().isValid("([)") == false));
   assert((Solution().isValid("") == true));
   assert((Solution().isValid("[") == false));
   return 0;
}
