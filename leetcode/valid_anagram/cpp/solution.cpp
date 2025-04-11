# include <iostream>
# include <string>
# include <cassert>
# include <algorithm>
# include <unordered_map>
# include <map>


class Solution {
public:
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Algorithm: Hash Array Frequency Counter
    */
   bool isAnagramUsingHashArray(std::string text1, std::string text2) {
      if (text1.length() != text2.length()) return false;
      int frequencies[26] = { 0 };
      for (int index = 0; index < text1.length(); index++) {
         frequencies[text1[index] - 'a']++;
         frequencies[text2[index] - 'a']--;
      }
      for (const int frequency : frequencies) {
         if (frequency != 0) return false;
      }
      return true;
   }

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Algorithm: HashMap Frequency Counter
    */
   bool isAnagramUsingHashMap(std::string text1, std::string text2) {
      if (text1.length() != text2.length()) return false;
      std::unordered_map<char, int> text1LetterCounter = counter(text1);
      std::unordered_map<char, int> text2LetterCounter = counter(text2);
      if (text1LetterCounter.size() != text2LetterCounter.size()) return false;
      return text1LetterCounter == text2LetterCounter;
   }

   std::unordered_map<char, int> counter(std::string text) {
      std::unordered_map<char, int> letterCounter;
      for (const char& letter : text) {
         letterCounter[letter]++;
      }
      return letterCounter;
   }

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Algorithm: Sorting Comparison
    */
   bool isAnagramUsingSorting(std::string text1, std::string text2) {
      if (text1.length() != text2.length()) return false;
      std::sort(text1.begin(), text1.end());
      std::sort(text2.begin(), text2.end());
      return text1 == text2;
   }
};


int main() {
   Solution solution;
   assert((solution.isAnagramUsingHashArray("anagram", "nagaram") == true));
   assert((solution.isAnagramUsingHashArray("rat", "car") == false));
   assert((solution.isAnagramUsingHashArray("", "") == true));
   return 0;
}