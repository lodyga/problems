# include <vector>
# include <unordered_set>
# include <cassert>

class Solution {
public:
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    */
   std::vector<int> sum_pairs(const std::vector<int>& numbers, int target) {
      std::unordered_set<int> uniqueNumbers;

      for (const int& number : numbers) {
         int complement = target - number;
         if (uniqueNumbers.count(complement)) {
            return { complement, number };
         }
         else {
            uniqueNumbers.insert(number);
         }
      }
      return {};
   }
};

int main() {
   Solution solution;
   assert((solution.sum_pairs({ 10, 5, 2, 3, 7, 5 }, 10) == std::vector<int>{ 3, 7 }));
   assert((solution.sum_pairs({ 1, 4, 8, 7, 3, 15 }, 8) == std::vector<int>{ 1, 7 }));
   assert((solution.sum_pairs({ 1, -2, 3, 0, -6, 1 }, -6) == std::vector<int>{ 0, -6 }));
   assert((solution.sum_pairs({ 10, 5, 2, 3, 7, 5 }, 10) == std::vector<int>{ 3, 7 }));
   assert((solution.sum_pairs({ 1, 2, 3, 4, 1, 0 }, 2) == std::vector<int>{ 1, 1 }));
   assert((solution.sum_pairs({ 4, -2, 3, 3, 4 }, 8) == std::vector<int>{ 4, 4 }));
   assert((solution.sum_pairs({ 0, 2, 0 }, 0) == std::vector<int>{ 0, 0 }));
   assert((solution.sum_pairs({ 5, 9, 13, -3 }, 10) == std::vector<int>{ 13, -3 }));
}