#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
   bool search(const vector<int>& nums, int target) {
      auto it = find(nums.begin(), nums.end(), target);
      if (it != nums.end()) {
         return true;
      }

      return false;
   }
};

int main() {
   Solution solution;
   cout << solution.search({2, 5, 6, 0, 0, 1, 2}, 0) << endl;
   cout << solution.search({2, 5, 6, 0, 0, 1, 2}, 3) << endl;
}
