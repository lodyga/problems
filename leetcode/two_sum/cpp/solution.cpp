#include <vector>
#include <unordered_map>
#include <cassert>

class Solution {
public:
   std::vector<int> twoSum(const std::vector<int>& numbers, int target) {
      std::unordered_map<int, int> seenNumbers;
      for (int i = 0; i < numbers.size(); ++i) {
         int complement = target - numbers[i];
         if (seenNumbers.count(complement)) {
            return { seenNumbers[complement], i };
         }
         seenNumbers[numbers[i]] = i;
      }
      return {};
   }
};

int main() {
   Solution solution;
   assert((Solution().twoSum({ 2, 7, 11, 15 }, 9) == std::vector<int>{0, 1}));
   assert((Solution().twoSum({ 3, 2, 4 }, 6) == std::vector<int>{1, 2}));
   assert((Solution().twoSum({ 3, 3 }, 6) == std::vector<int>{0, 1}));
   assert((Solution().twoSum({ 3, 3 }, 7) == std::vector<int>{}));
   return 0;
}
