class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {string[][]} paths
    * @return {string}
    */
   destCity(paths) {
      const originCities = new Set();
      const destinationCities = new Set();

      for (const [originCity, destinationCity] of paths) {
         originCities.add(originCity);
         destinationCities.add(destinationCity);
      }

      for (const destinationCity of destinationCities) {
         if (!originCities.has(destinationCity))
            return destinationCity
      }
   };
}
const destCity = new Solution().destCity;


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {string[][]} paths
    * @return {string}
    */
   destCity = function (paths) {
      const originCities = new Set(paths.map(([originCity, _]) => originCity));
      const destinationCities = new Set(paths.map(([_, destinationCity]) => destinationCity));

      for (const destinationCity of destinationCities)
         if (!originCities.has(destinationCity))
            return destinationCity
   };
}
const destCity = new Solution().destCity;


console.log(new Solution().destCity([['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]), 'Sao Paulo')
console.log(new Solution().destCity([['B', 'C'], ['D', 'B'], ['C', 'A']]), 'A')
console.log(new Solution().destCity([['A', 'Z']]), 'Z')