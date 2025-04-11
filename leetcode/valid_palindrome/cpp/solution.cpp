# include <string>
# include <cassert>

class Solution {
public:
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    */
   bool isPalindrome(std::string text) {
      if (text.empty()) {
         return true;
      }

      int left = 0;
      int right = text.size() - 1;

      while (left < right) {
         while (left < right && this->isPunctuation(text.at(left))) {
            left++;
         }
         while (left < right && this->isPunctuation(text[right])) {
            right--;
         }

         if (tolower(text.at(left)) != tolower(text[right])) {
            return false;
         }
         else {
            left++;
            right--;
         }
      }
      return true;
   }

private:
   bool isPunctuation(char chr) {
      return !(
         isdigit(chr) || isalpha(chr)
         );
   }
};

int main() {
   Solution solution;
   assert(solution.isPalindrome("A man, a plan, a canal: Panama"));
   assert(!solution.isPalindrome("race a car"));
   assert(solution.isPalindrome(" "));
   assert(!solution.isPalindrome("0P"));
   assert(solution.isPalindrome("ab_a"));
   assert(solution.isPalindrome(""));
   return 0;
}