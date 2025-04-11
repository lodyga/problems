#include <iostream>
#include <vector>
#include <unordered_set>
#include <cassert>

class Solution {
public:
   bool containsDuplicate(const std::vector<int>& numbers) {
      std::unordered_set<int> uniqueNumbers;
      for (const int& number : numbers) {
         if (uniqueNumbers.count(number)) {
            return true;
         }
         uniqueNumbers.insert(number);
      }
      return false;
   }
};

int main() {
   assert((Solution().containsDuplicate(std::vector<int>{1, 2, 3, 1}) == true));
   assert((Solution().containsDuplicate(std::vector<int>{1, 2, 3}) == false));
   assert((Solution().containsDuplicate(std::vector<int>{1, 2, 3, 4}) == false));
   assert((Solution().containsDuplicate(std::vector<int>{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}) == true));
   return 0;
}