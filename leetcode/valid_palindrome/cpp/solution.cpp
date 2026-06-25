# include <iostream>
# include <string>
using namespace std;


class Solution {
public:
   bool isPalindrome(std::string text) {
      int left = 0;
      int right = text.size() - 1;

      while (left < right) {
         while (left < right && !isalnum(text.at(left))) {
            left++;
         }

         while (left < right && !isalnum(text[right])) {
            right--;
         }

         if (tolower(text.at(left)) == tolower(text[right])) {
            left++;
            right--;
         }
         else {
            return false;
         }
      }

      return true;
   }
};


int main() {
   Solution solution;
   cout << solution.isPalindrome("A man, a plan, a canal: Panama");
   // assert(solution.isPalindrome("A man, a plan, a canal: Panama"));
   // assert(!solution.isPalindrome("race a car"));
   // assert(solution.isPalindrome(" "));
   // assert(!solution.isPalindrome("0P"));
   // assert(solution.isPalindrome("ab_a"));
   // assert(solution.isPalindrome(""));
   return 0;
}