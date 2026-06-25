# include <iostream>
# include <string>
using namespace std;


class Solution {
public:
   int balancedStringSplit(const string& text) {
      int counter = 0;
      int res = 0;

      for (const char& chr : text) {
         counter += chr == 'R' ? 1 : -1;

         if (counter == 0) {
            res++;
         }
      }

      return res;
   }
};


int main() {
   Solution solution;
   cout << solution.balancedStringSplit("RLRRLLRLRL");
   return 0;
}