#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
   long long countSubarrays(vector<int>& nums, int k) {
      auto max_num = max_element(nums.begin(), nums.end());
      int left = 0;
      long res = 0;

      for (int num : nums)
      {
         if (num == *max_num)
         {
            k--;
         }

         while (k == 0)
         {
            if (nums[left] == *max_num)
            {
               k++;
            }

            left++;
         }

         res += left;
      }

      return res;
   }
};
