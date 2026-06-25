#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;


class Solution {
public:
   std::vector<int> twoSum(const std::vector<int>& nums, int target) {
      std::unordered_map<int, int> numIdx;

      for (int idx = 0; idx < nums.size(); idx++) {
         int diff = target - nums[idx];

         if (numIdx.count(diff)) {
            return { numIdx[diff], idx };
         }
         else {
            numIdx[nums[idx]] = idx;
         }
      }

      return {};
   }
};


void printVector(const vector<int>& vector) {
   cout << "[";

   for (int idx = 0; idx < vector.size(); idx++) {
      cout << vector[idx];

      if (idx < vector.size() - 1) {
         cout << ", ";
      }
   }

   cout << "]\n";
}

int main() {
   Solution solution;
   printVector(solution.twoSum({ 2, 7, 11, 15 }, 9));
   printVector(solution.twoSum({ 3, 3 }, 6));
   printVector(solution.twoSum({ 3, 3 }, 7));
   return 0;
}
